from ClassInterfaces import IChunker, IParser
from typing import Optional

#TODO this is a strict chunker, which chunks by adding not symbol amount, but whole paragraphs to next chunk
class Chunker:
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
       pass


    def close(self) -> None:
        self.parser.close()


    def expand_input_text_buffer(self) -> bool:
        pass

    def expand_chunk_buffer(self) -> bool:
        pass


    def get_next_chunk(self) -> str or None:
        pass



