# BitNet b1.58 Server

This is a HTTP server for communicating with Microsoft's bitnet-b1.58-2B-4T model using HuggingFaces transformers package. It is built using Flask.

## Description

This project contains a Python server (`server.py`) and associated configurations. The goal is to provide a backend service for LLM inference.

## Getting Started

### Prerequisites

*   Python 3.7+
*   `pip` package installer

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/bitnet-project.git
    cd bitnet-project
    ```
2.  Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

To start the server, run the following command:
```bash
python api/index.py
```
The server will start and listen for incoming requests on a default port. Refer to `server.py` for specific configuration details.

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.