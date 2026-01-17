import pymupdf
from typing import Optional, Iterator
from src.interfaces.BaseParser import BaseParser
from src.interfaces.parser import ParserInfo, FileType, Connectivity


class PyMuPdfRaw(BaseParser):
    info = ParserInfo(
        name= "pymupdf_raw",
        supported_types= [FileType.PDF],
        connectivity=Connectivity.OFFLINE,
        is_ocr=False,
    )

    doc = None
    pages_iterator: Optional[Iterator] = None

    def __init__(self, config: Optional[dict] = None) -> None:
        super().__init__(config)

    def open(self, file_name: Optional[str]) -> None:
        try:
            if not file_name:
                raise ValueError("File name is required")

            self.file_name = file_name
            # Open the document using pymupdf directly
            self.doc = pymupdf.open(self.file_name)
            self.pages_iterator = iter(self.doc)
        except Exception as e:
            raise Exception(f"Error opening file with PyMuPDF: {e}")

    def get_next_text_block(self) -> Optional[str]:
        try:
            if self.pages_iterator is None:
                raise Exception("File is not open")

            page = next(self.pages_iterator)

            return page.get_text()

        except StopIteration:
            return None
        except Exception as e:
            print(f"Error reading page: {e}")
            return None

    def close(self) -> None:
        if self.doc:
            self.doc.close()
            self.doc = None
            self.pages_iterator = None