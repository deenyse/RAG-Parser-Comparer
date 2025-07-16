from abc import ABC, abstractmethod
from typing import Optional, Iterator

class iParser(ABC):
    def __init__(self, file_path: str):
        """Initialize the parser with the file path."""
        self.file_path = file_path
        self._is_open = False

    @abstractmethod
    def open(self) -> None:
        """Initialize the parser and open the file for reading, setting up for minimal memory usage."""
        pass

    @abstractmethod
    def close(self) -> None:
        """Close the file and clean up resources to prevent memory leaks."""
        pass

    @abstractmethod
    def get_next_chunk(self) -> Optional[str]:
        """Retrieve the next chunk of text from the file, loading only one chunk at a time. Returns None if no more chunks."""
        pass

    def __enter__(self):
        """Enter method for context manager support, opens the parser with proper resource management."""
        self.open()
        self._is_open = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit method for context manager support, ensures resources are cleaned up to free memory."""
        self.close()
        self._is_open = False

    def __iter__(self) -> Iterator[str]:
        """Make the parser iterable, yielding chunks one at a time to minimize memory usage."""
        while True:
            chunk = self.get_next_chunk()
            if chunk is None:
                break
            yield chunk