import pdfplumber

from ClassInterfaces.IParser import IParser

class ParsByPdfPlumber(IParser):
    file = None
    page_iterator = None

    def __init__(self, file_name: str) -> None:
        super().__init__(file_name)


    def get_next_text_block(self) -> str or None:
        try:
            if self.file is None:
                raise Exception("file is not open")
            text = next(self.page_iterator).extract_text()
            return text
        except StopIteration:
            return None

    def _open(self):
        try:
            self.file = pdfplumber.open(self.file_name)
            self.page_iterator = iter(self.file.pages)
        except Exception as e:
            raise Exception(f"Error opening file: {e}")

    def _close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
            self.page_iterator = None
