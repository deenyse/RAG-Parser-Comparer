# PDF Chunking and Parsing Tool

This project provides a modular system for parsing PDF files and chunking their content for further processing, such as feeding into language models or other downstream tasks. It is designed with extensibility in mind, using interface-based architecture for parsers and chunkers.

## Features
- **PDF Parsing**: Uses `pdfplumber` to extract text from PDF files.
- **Chunking**: Splits text into chunks of configurable size, with optional overlap between chunks.
- **Configurable**: API keys and other settings are managed via a YAML config file or environment variables.
- **Extensible**: Easily add new parsers or chunkers by implementing the provided interfaces.

## Project Structure
- `main.py`: Example usage and entry point.
- `Parsers/`: Contains PDF parser implementations (e.g., `PdfPlumber.py`).
- `Tools/Chunkers/`: Contains chunker implementations (e.g., `SymbolChunker.py`).
- `ClassInterfaces/`: Abstract base classes for parsers and chunkers.
- `Tools/config.py`: Configuration loader.
- `config.exmaple.yaml`: Example configuration file.

## Usage

1. **Install dependencies** (requires Python 3.7+):
   ```bash
   pip install pdfplumber pyyaml google-genai chromadb
   ```

2. **Prepare your config file**:
   - Copy `config.exmaple.yaml` to `config.yaml` and fill in your API key if needed.

3. **Run the example**:
   - Place a PDF file (e.g., `TestFiles/OverlapTest.pdf`) in the appropriate directory.
   - Run:
     ```bash
     python main.py
     ```
   - The script will parse the PDF and print out text chunks.

## Configuration

Configuration is loaded from `config.yaml` or environment variables. Example:

```yaml
gemini_api:
  key: your_gemini_api_key_here
```

## Extending
- **Add a new parser**: Implement the `IParser` interface in `ClassInterfaces/IParser.py`.
- **Add a new chunker**: Implement the `IChunker` interface in `ClassInterfaces/IChunker.py`.
- **Add a new LLM**: Implement the `ILLM` interface in `ClassInterfaces/ILLM.py`.