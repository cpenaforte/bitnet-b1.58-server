from flask import Flask, request, jsonify
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Initialize Flask app
app = Flask(__name__)

# Global variables for model and tokenizer
tokenizer = None
model = None
model_id = "microsoft/bitnet-b1.58-2B-4T"

def load_model():
    global tokenizer, model
    print("Loading model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16
    )
    # Move model to GPU if available
    if torch.cuda.is_available():
        model.to('cuda')
    elif torch.backends.mps.is_available():
        model.to('mps')
    print("Model and tokenizer loaded.")

@app.route('/generate', methods=['POST'])
def generate_text():
    if not model or not tokenizer:
        return jsonify({"error": "Model not loaded. Please ensure the server has started correctly."}), 503

    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({"error": "Invalid request. 'prompt' field is required."}), 400

    user_prompt = data['prompt']
    
    # Prepare messages for chat template
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": user_prompt},
    ]
    
    try:
        prompt_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        chat_input = tokenizer(prompt_text, return_tensors="pt").to(model.device)

        # Generate response
        chat_outputs = model.generate(**chat_input, max_new_tokens=100) # Increased max_new_tokens for better responses
        response_text = tokenizer.decode(chat_outputs[0][chat_input['input_ids'].shape[-1]:], skip_special_tokens=True)

        return jsonify({"response": response_text.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    load_model() # Load model on server startup
    # Use host='0.0.0.0' to make the server accessible externally
    # Use debug=True for development, but set to False for production
    app.run(host='0.0.0.0', port=5000, debug=True)
