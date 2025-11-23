import pymupdf4llm
from typing import Optional, Iterator
from ClassInterfaces.IParser import IParser


class PyMuPdf4LLM(IParser):
    # Iterator for parsed pages
    pages_iterator: Optional[Iterator[dict]] = None

    def __init__(self) -> None:
        pass

    def open(self, file_name: str) -> None:
        try:
            if not file_name:
                raise ValueError("File name must be provided.")

            # pymupdf4llm.to_markdown with page_chunks=True returns a list of dictionaries.
            # Each dictionary contains metadata and the 'text' (markdown content) of the page.
            # This allows us to yield content page-by-page, fitting the IParser interface.
            md_pages = pymupdf4llm.to_markdown(file_name, page_chunks=True)

            self.pages_iterator = iter(md_pages)

        except Exception as e:
            raise Exception(f"Error opening or parsing file with PyMuPDF4LLM: {e}")

    def get_next_text_block(self) -> Optional[str]:
        try:
            if self.pages_iterator is None:
                raise Exception("File is not open. Call open() first.")

            page_data = next(self.pages_iterator)

            return page_data["text"]

        except StopIteration:
            return None
        except Exception as e:
            print(f"Error reading next block: {e}")
            return None

    def close(self) -> None:
        self.pages_iterator = None