from src.interfaces.IParser import IParser
from typing import Optional, Iterator
from docling.document_converter import DocumentConverter


class DoclingParser(IParser):
    converter: Optional[DocumentConverter] = None
    pages_iterator: Optional[Iterator[str]] = None

    def __init__(self) -> None:
        try:
            self.converter = DocumentConverter()

        except Exception as e:
            raise Exception(f"Failed to initialize Docling converter: {e}")

    def open(self, file_name: Optional[str]) -> None:
        try:
            if not file_name:
                raise ValueError("File name is required")

            print(f"Processing {file_name} with Docling (this might take a moment)...")

            conversion_result = self.converter.convert(file_name)
            doc = conversion_result.document

            full_markdown = doc.export_to_markdown()

            self.pages_iterator = iter([full_markdown])

        except Exception as e:
            raise Exception(f"Error processing file with Docling: {e}")

    def get_next_text_block(self) -> Optional[str]:
        try:
            if self.pages_iterator is None:
                raise Exception("File is not open. Call open() first.")

            return next(self.pages_iterator)

        except StopIteration:
            return None
        except Exception as e:
            print(f"Error reading block: {e}")
            return None

    def close(self) -> None:
        self.pages_iterator = None