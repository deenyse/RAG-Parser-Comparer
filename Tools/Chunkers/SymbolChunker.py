from ClassInterfaces.IChunker import IChunker
from ClassInterfaces import  IParser
from typing import Optional

#this is a strict chunker, which chunks by symbol amount
class SymbolChunker(IChunker):
    #is more text to retrieve from file
    is_more_text = True
    #buffer for text from file
    input_text_buffer = ""

    #ocverlap from previous chunk
    prev_chunk_overlap = ""
    #chunk to be returned after next in the iteration
    new_chunk = ""

    iterable_parsed_file = None
    def __init__(self, parser: IParser, file_name:str, chunk_size:int, overlap_size:int) -> None:
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")
        if overlap_size < 0:
            raise ValueError("overlap_size cannot be negative")
        if overlap_size > chunk_size:
            raise ValueError("overlap_size cannot be larger than chunk_size")

        super().__init__(parser, file_name, chunk_size, overlap_size)

    def open(self) -> None:
        try:
            if self.file_name is None:
                raise Exception("File location is incorrect")

            self.iterable_parsed_file = self.parser(self.file_name)
        except Exception as e:
            raise Exception(f"Error opening file: {e}")


    def close(self) -> None:
        self.iterable_parsed_file.close()

    def expand_input_text_buffer(self) -> None:
        next_text = self.iterable_parsed_file.get_next_text_block()
        if next_text is None:
            self.is_more_text = False
            return

        self.input_text_buffer += next_text


    def get_next_chunk(self) -> Optional[str]:
        if self.iterable_parsed_file is None:
            raise RuntimeError("File is not open")

        if len(self.input_text_buffer) < self.chunk_size - self.overlap_size:
            self.expand_input_text_buffer()

        if not self.is_more_text and self.input_text_buffer == "":
            return None

        self.new_chunk = self.prev_chunk_overlap
        self.new_chunk += self.input_text_buffer[:self.chunk_size - len(self.prev_chunk_overlap)]

        self.input_text_buffer = self.input_text_buffer[self.chunk_size - len(self.prev_chunk_overlap):]

        self.prev_chunk_overlap = self.new_chunk[self.chunk_size - self.overlap_size:]

        return self.new_chunk



