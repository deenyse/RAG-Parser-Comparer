from abc import ABC, abstractmethod, abstractproperty
from typing import Optional, Iterator

class IParser(ABC):
    def __init__(self) -> None:
        """Initialize the parser with the file path."""

    @abstractmethod
    def open(self, file_path:str) -> None:
        """Initialize the parser and open the file for reading, setting up for minimal memory usage."""
        pass

    @abstractmethod
    def close(self) -> None:
        """Close the file and clean up resources to prevent memory leaks."""
        pass

    @abstractmethod
    def get_next_text_block(self) -> str or None: ## this thing will be needed to reimplement for each parser individually(even though the code is almost the same. I NEED OT DO SEPARETE CHUNKER CLASS
        """Retrieve the next block of text from the file, loading only one chunk at a time. Returns None if no more chunks."""
        pass

    def __enter__(self) -> "IParser":
        """Enter method for context manager support, opens the parser with proper resource management."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit method for context manager support, ensures resources are cleaned up to free memory."""

    def __iter__(self) -> Iterator[str]:
        """Make the parser iterable, yielding chunks one at a time to minimize memory usage."""
        while True:
            chunk = self.get_next_text_block()
            if chunk is None:
                break
            yield chunk