import pdfplumber
from typing import Optional
from ClassInterfaces.IParser import IParser

class ParsByPdfPlumber(IParser):
    #place to keep opened file
    file = None
    #palce to keep pages iterator retrieved from files
    page_iterator = None

    def __init__(self, file_name:Optional[str] = None) -> None:
        super().__init__(file_name)

    def open(self, file_name:str) -> None:
        try:
            self.file_name = file_name

            self.file = pdfplumber.open(self.file_name)
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
