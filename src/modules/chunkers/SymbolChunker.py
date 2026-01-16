from src.interfaces.IChunker import IChunker
from src.interfaces import IParser
from typing import Optional


class SymbolChunker(IChunker):
    """
    Chunker that splits text into chunks by a specified number of symbols (characters).
    Maintains overlap between chunks for context preservation.
    Args:
        parser (IParser): Parser instance to read the file.
        file_name (str): Path to the file to chunk.
        chunk_size (int): Target size of each chunk (in symbols).
        overlap_size (int): Number of symbols to overlap between chunks.
    """
    # is more text to get from file
    is_more_text = True
    # buffer for text from file
    input_text_buffer = ""
    # overlap from previous chunk
    prev_chunk_overlap = ""
    # chunk to be returned after next in the iteration
    new_chunk = ""

    def __init__(self, parser: IParser, file_name:str, chunk_size:int, overlap_size:int) -> None:
        """
        Initialize the SymbolChunker.
        Args:
            parser (IParser): Parser instance.
            file_name (str): File to chunk.
            chunk_size (int): Number of symbols per chunk.
            overlap_size (int): Number of overlapping symbols.
        Raises:
            ValueError: If chunk_size or overlap_size are invalid.
        """
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")
        if overlap_size < 0:
            raise ValueError("overlap_size cannot be negative")
        if overlap_size > chunk_size:
            raise ValueError("overlap_size cannot be larger than chunk_size")
        super().__init__(parser, file_name, chunk_size, overlap_size)

    def open(self) -> None:
        """
        Open the file for chunking.
        Raises:
            Exception: If file location is incorrect or cannot be opened.
        """
        try:
            if self.file_name is None:
                raise Exception("File location is incorrect")
            self.parser.open(self.file_name)
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

        if len(self.input_text_buffer) < self.chunk_size - self.overlap_size:
            self.expand_input_text_buffer()

        if not self.is_more_text and self.input_text_buffer == "":
            return None

        self.new_chunk = self.prev_chunk_overlap
        self.new_chunk += self.input_text_buffer[:self.chunk_size - len(self.prev_chunk_overlap)]
        
        self.input_text_buffer = self.input_text_buffer[self.chunk_size - len(self.prev_chunk_overlap):]
        self.prev_chunk_overlap = self.new_chunk[self.chunk_size - self.overlap_size:]
        
        return self.new_chunk



