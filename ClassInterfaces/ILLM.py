from abc import ABC, abstractmethod
from typing import List, Union, Optional

class ILLM(ABC):
    """
    Abstract base class for Large Language Model (LLM) interfaces.
    Provides a method for generating responses based on context.
    """
    def __init__(self, gemini_conf:dict) -> None:
        """
        Initialize the LLM interface with configuration.
        Args:
            gemini_conf (dict): Configuration for the LLM.
        """
        pass

    @abstractmethod
    def get_response_based_on_context(self, queries:Union[List[str], str], context:Optional[list[str]] = None, model:Optional[str] = None ) -> Optional[list[str]]:
        """
        Generate responses to queries using the provided context.
        Args:
            queries (Union[List[str], str]): List of queries or a single query string.
            context (Optional[list[str]]): Contextual information for the LLM.
            model (Optional[str]): Model name or identifier.
        Returns:
            Optional[list[str]]: List of responses or None if not applicable.
        """
        pass

