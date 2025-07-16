from abc import ABC

import pdfplumber

from ClassInterfaces.IParser import IParser

class ParsByPdfPlumber(IParser): #later add support to IParser
    file = None
    page_iterator = None

    def __init__(self) -> None:
        super().__init__()

    def get_next_text_block(self) -> str or None:
        try:
            if self.file is None:
                raise Exception("file is not open")
            text = next(self.page_iterator).extract_text()
            return text
        except StopIteration:
            return None

    def open(self, file_path:str):
        try:
            self.file = pdfplumber.open(file_path)
            self.page_iterator = iter(self.file.pages)
        except Exception as e:
            print(f"Error during file opening: {e}")

    def close(self):
        self.file.close()

