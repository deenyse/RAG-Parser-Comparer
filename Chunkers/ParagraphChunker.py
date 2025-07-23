from ClassInterfaces.IChunker import IChunker
from ClassInterfaces import IParser
from typing import Optional

#TODO this is a strict chunker, which chunks by adding not symbol amount, but whole paragraphs to next chunk
class ParagraphChunker(IChunker):
    """
    Chunker that splits text into chunks by whole paragraphs, not by symbol count.
    Args:
        parser (IParser): Parser instance to read the file.
        file_name (str): Path to the file to chunk.
        chunk_size (int): Target size of each chunk (in paragraphs).
        overlap_size (int): Number of paragraphs to overlap between chunks.
    """
    def __init__(self, parser: IParser, file_name:str, chunk_size:int, overlap_size:int) -> None:
        """
        Initialize the ParagraphChunker.
        Args:
            parser (IParser): Parser instance.
            file_name (str): File to chunk.
            chunk_size (int): Number of paragraphs per chunk.
            overlap_size (int): Number of overlapping paragraphs.
        """
        pass

    def open(self, file_name:Optional[str] = None) -> None:
        """
        Open the file for chunking. Optionally specify a new file name.
        Args:
            file_name (Optional[str]): File to open.
        """
        pass

    def close(self) -> None:
        """
        Close the file and release resources.
        """
        pass

    def expand_input_text_buffer(self) -> bool:
        """
        Expand the internal buffer with more text from the file.
        Returns:
            bool: True if buffer was expanded, False if end of file.
        """
        pass

    def expand_chunk_buffer(self) -> bool:
        """
        Expand the chunk buffer with additional paragraphs if needed.
        Returns:
            bool: True if buffer was expanded, False otherwise.
        """
        pass

    def get_next_chunk(self) -> str or None:
        """
        Get the next chunk of text (paragraphs).
        Returns:
            str or None: The next chunk, or None if no more chunks.
        """
        pass



