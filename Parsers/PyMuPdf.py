from ClassInterfaces.IParser import IParser
from llama_cloud_services import LlamaParse
from typing import Optional


class PyMuPdf(IParser):
    #place to keep opened file
    file = None
    #palce to keep pages iterator retrieved from files
    page_iterator = None

    def __init__(self, config:dict, file_name: Optional[str] = None ) -> None:
        super().__init__(file_name)



    def get_next_text_block(self) -> Optional[str]:
        try:
            if self.file is None:
                raise Exception("File is not open")
            return next(self.page_iterator).text.replace("\n\n", " ").replace("\t", "")
        except StopIteration:
            return None

    def open(self, file_name:str) -> None:
        try:
            self.file_name = file_name

            self.page_iterator = iter(self.file.pages)
        except Exception as e:
            raise Exception(f"Error opening file: {e}")

    def close(self):
        if self.file is not None:
            self.file = None
            self.page_iterator = None