from ClassInterfaces import IChunker, IParser
from typing import Optional

#this is a strict chunker, which chunks by symbol amount
class SymbolChunker:
    is_more_text = True
    input_text_buffer = ""

    prev_chunk_overlap = ""
    new_chunk = ""

    iterable_parsed_file = None
    def __init__(self, parser: IParser, file_name:str, chunk_size:int, overlap_size:int) -> None:
        self.parser = parser
        self.file_name = file_name
        self.chunk_size = chunk_size
        self.overlap_size = overlap_size

    def open(self, file_name:Optional[str] = None) -> None:
        try:
            if file_name is not None:
                self.file_name = file_name

            if self.file_name is None:
                raise Exception("File location is incorrect")

            self.iterable_parsed_file = self.parser()
            self.iterable_parsed_file.open(self.file_name)
            self.iterable_parsed_file = iter(self.iterable_parsed_file)

        except Exception as e:
            raise Exception(f"Error opening file: {e}")


    def close(self) -> None:
        self.parser.close()


    def expand_input_text_buffer(self) -> None:
        next_text = next(self.iterable_parsed_file)

        if next_text is None:
            self.is_more_text = False
            return

        self.input_text_buffer += next_text


    def get_next_chunk(self) -> Optional[str]:
        if len(self.input_text_buffer) < self.chunk_size - self.overlap_size:
            self.expand_input_text_buffer()

        if not self.is_more_text and self.input_text_buffer == "":
            return None

        self.new_chunk = self.prev_chunk_overlap
        self.new_chunk += self.input_text_buffer[:self.chunk_size - len(self.prev_chunk_overlap)]

        self.input_text_buffer = self.input_text_buffer[self.chunk_size - len(self.prev_chunk_overlap):]

        self.prev_chunk_overlap = self.new_chunk[self.chunk_size - self.overlap_size:]

        return self.new_chunk



