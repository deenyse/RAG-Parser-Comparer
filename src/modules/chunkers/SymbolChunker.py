from src.interfaces.BaseChunker import BaseChunker, ChunkerParams
from src.interfaces import BaseParser
from typing import Optional


class SymbolChunker(BaseChunker):
    """
    Chunker that splits text into chunks by a specified number of symbols (characters).
    Maintains overlap between chunks for context preservation.
    """

    name = "symbol"

    # is more text to get from file
    is_more_text = True
    # buffer for text from file
    input_text_buffer = ""
    # overlap from previous chunk
    prev_chunk_overlap = ""
    # chunk to be returned after next in the iteration
    new_chunk = ""

    parser = None

    def __init__(self,  params: ChunkerParams) -> None:
        super().__init__(params)

    def open(self, parser:BaseParser, file_name:str) -> None:
        """
        Open the file for chunking.
        Raises:
            Exception: If file location is incorrect or cannot be opened.
        """
        self.parser = parser
        try:
            if file_name is None:
                raise Exception("File location is incorrect")
            self.parser.open(file_name)
        except Exception as e:
            raise Exception(f"Error opening file: {e}")

    def close(self) -> None:
        """
        Close the file and release resources.
        """
        self.parser.close()

    def expand_input_text_buffer(self) -> None:
        """
        Expand the internal buffer with more text from the file.
        Sets is_more_text to False if end of file is reached.
        """
        next_text = self.parser.get_next_text_block()
        if next_text is None:
            self.is_more_text = False
            return
        self.input_text_buffer += next_text

    def get_next_chunk(self) -> Optional[str]:
        """
        Get the next chunk of text (symbols).
        Returns:
            Optional[str]: The next chunk, or None if no more chunks.
        Raises:
            RuntimeError: If file is not open.
        """
        if self.parser is None:
            raise RuntimeError("File is not open")

        if len(self.input_text_buffer) < self.params.chunk_size - self.params.chunk_overlap:
            self.expand_input_text_buffer()

        if not self.is_more_text and self.input_text_buffer == "":
            return None

        self.new_chunk = self.prev_chunk_overlap
        self.new_chunk += self.input_text_buffer[:self.params.chunk_size - len(self.prev_chunk_overlap)]
        
        self.input_text_buffer = self.input_text_buffer[self.params.chunk_size - len(self.prev_chunk_overlap):]
        self.prev_chunk_overlap = self.new_chunk[self.params.chunk_size - self.params.chunk_overlap:]
        
        return self.new_chunk



