# Modular RAG Pipeline for PDF Parsing and Chunking

This project is a universal, modular pipeline for Retrieval-Augmented Generation (RAG) workflows with PDF files. It supports pluggable parsers, chunkers, large language models (LLMs), and vector databases, making it easy to experiment with different components and architectures for document question answering and information retrieval.

## Features
- **PDF Parsing**: Uses `pdfplumber` to extract text from PDF files.
- **Chunking**: Splits text into chunks of configurable size (by symbols, paragraphs, or tokens), with optional overlap between chunks.
- **Configurable**: API keys and other settings are managed via a YAML config file or environment variables.
- **Extensible**: Easily add new parsers, chunkers, LLMs, or databases by implementing the provided interfaces.
- **Well-Documented**: All core classes and methods are now documented with concise docstrings for easier understanding and extension.

## Project Structure
- `main.py`: Example usage and entry point.
- `Parsers/`: Contains parser implementations (e.g., `PdfPlumber.py`).
- `Chunkers/`: Contains chunker implementations (e.g., `SymbolChunker.py`, `ParagraphChunker.py`, `TokenChunker.py`).
- `DBs/`: Contains vector database implementations (e.g., `ChromaDB.py`).
- `LLMs/`: Contains LLM implementations (e.g., `GoogleGemini.py`).
- `ClassInterfaces/`: Abstract base classes for parsers, chunkers, LLMs, and databases.
- `Tools/config.py`: Configuration loader.
- `Tools/RAGPipline.py`: Universal RAG pipeline function.
- `config.exmaple.yaml`: Example configuration file.
gti
## Usage

1. **Install dependencies** (requires Python 3.7+):
   ```bash
   pip install pdfplumber pyyaml google-genai chromadb
   ```

2. **Prepare your config file**:
   - Copy `config.exmaple.yaml` to `config.yaml` and fill in your API key if needed.

3. **Run the example**:
   - Place a PDF file (e.g., `TestFiles/biography-cz.pdf`) in the appropriate directory.
   - Run:
     ```bash
     python main.py
     ```
   - The script will parse the PDF and print out answers to the provided questions using the RAG pipeline.

## Configuration

Configuration is loaded from `config.yaml` or environment variables. Example:

```yaml
gemini_config:
  key: your_gemini_api_key_here
```

## Extending
- **Add a new parser**: Implement the `IParser` interface in `ClassInterfaces/IParser.py` and place your implementation in `Parsers/`.
- **Add a new chunker**: Implement the `IChunker` interface in `ClassInterfaces/IChunker.py` and place your implementation in `Chunkers/`.
- **Add a new LLM**: Implement the `ILLM` interface in `ClassInterfaces/ILLM.py` and place your implementation in `LLMs/`.
- **Add a new database**: Implement the `IDatabase` interface in `ClassInterfaces/IDatabase.py` and place your implementation in `DBs/`.

All interfaces and core classes are now documented with clear docstrings for easier development and onboarding.