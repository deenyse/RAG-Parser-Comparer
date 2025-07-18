import pdfplumber
from typing import Optional
from ClassInterfaces.IParser import IParser

class ParsByPdfPlumber(IParser):
    file = None
    page_iterator = None

    def __init__(self, file_name:Optional[str] = None) -> None:
        super().__init__(file_name)
        self.open(self.file_name)

    def get_next_text_block(self) -> str or None:
        try:
            if self.file is None:
                raise Exception("File is not open")
            return next(self.page_iterator).extract_text()
        except StopIteration:
            return None

    def open(self, file_name:Optional[str] = None) -> None:
        try:
            if file_name is not None:
                self.file_name = file_name

            if self.file_name is None:
                raise Exception("File location is not given")

            self.file = pdfplumber.open(self.file_name)
            self.page_iterator = iter(self.file.pages)
        except Exception as e:
            raise Exception(f"Error opening file: {e}")

    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
            self.page_iterator = None
