from abc import ABC, abstractmethod
from typing import List, Union, Optional, Any

class BaseLLM(ABC):
    """
    Abstract base class for Large Language Model (LLM) interfaces.
    Provides a method for generating responses based on context.
    """

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

    @abstractmethod
    def get_int_response(self, query:str) -> Any:
        pass
