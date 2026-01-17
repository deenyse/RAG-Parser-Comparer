from src.interfaces.BaseParser import BaseParser
from llama_cloud_services import LlamaParse
from typing import Optional, Iterator
import nest_asyncio
from src.interfaces.parser import ParserInfo, FileType, Connectivity

nest_asyncio.apply()


class LlamaParseMd(BaseParser):
    info = ParserInfo(
        name= "llama_parse",
        supported_types= [FileType.PDF, FileType.DOCX],
        connectivity=Connectivity.ONLINE,
        is_ocr=True,
    )

    documents_iterator: Optional[Iterator] = None
    parser: Optional[LlamaParse] = None

    def __init__(self, api_key:str) -> None:
        if not api_key:
            raise ValueError("API Key for LlamaCloud is missing in config or env variables.")

        try:
            self.parser = LlamaParse(
                api_key=api_key,
                result_type="markdown",
                verbose=True,
                num_workers=4
            )
        except Exception as e:
            raise Exception(f"Failed to initialize LlamaParse client: {e}")

    def open(self, file_name: Optional[str]) -> None:
        try:
            if not file_name:
                raise ValueError("File name is required")

            if self.parser is None:
                raise RuntimeError("LlamaParse client is not initialized.")

            print(f"Sending {file_name} to LlamaCloud...")

            documents = self.parser.load_data(file_name)

            if not documents:
                print("Warning: LlamaParse returned no content.")
                self.documents_iterator = iter([])
            else:
                self.documents_iterator = iter(documents)

        except Exception as e:
            raise Exception(f"Error processing file {file_name} with LlamaParse: {e}")

    def get_next_text_block(self) -> Optional[str]:
        try:
            if self.documents_iterator is None:
                raise Exception("File is not open. Call open() first.")

            document = next(self.documents_iterator)

            return document.text

        except StopIteration:
            return None
        except Exception as e:
            print(f"Error reading next block: {e}")
            return None

    def close(self) -> None:
        self.documents_iterator = None