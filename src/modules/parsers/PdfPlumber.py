import pdfplumber
from typing import Optional
from src.interfaces.IParser import IParser
from src.interfaces.parser import ParserInfo, FileType, Connectivity

class PdfPlumber(IParser):
    info = ParserInfo(
        name= "pdf_plumber",
        supported_types= [FileType.PDF],
        connectivity=Connectivity.OFFLINE,
        is_ocr=False,
    )

    #place to keep opened file
    file = None
    #palce to keep pages iterator retrieved from files
    page_iterator = None

    def __init__(self) -> None:
        pass

    def open(self, file_name:str) -> None:
        try:
            self.file = pdfplumber.open(file_name)
            self.page_iterator = iter(self.file.pages)
        except Exception as e:
            raise Exception(f"Error opening file: {e}")

    def get_next_text_block(self) -> Optional[str]:
        try:
            if self.file is None:
                raise Exception("File is not open")
            return next(self.page_iterator).extract_text()
        except StopIteration:
            return None

    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
            self.page_iterator = None
