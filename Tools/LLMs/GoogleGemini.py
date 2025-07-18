from google import genai
from typing import Optional, Union, List
from enum import Enum
from ClassInterfaces.ILLM import ILLM


class TaskType(Enum):
    DOCUMENT = "RETRIEVAL_DOCUMENT"
    QUERY = "RETRIEVAL_QUERY"

class Gemini(ILLM):
    def __init__(self, gemini_conf:dict) -> None:
        super().__init__(gemini_conf)
        self.embedding_model = gemini_conf["embedding_model"]
        self.query_model = gemini_conf["query_model"]

        self.client = genai.Client(api_key=gemini_conf["api_key"])

    def get_chunks(self, task_type:TaskType, chunks:list[str], model:Optional[str] = None) -> list[str]:


        if model is None:
            model = self.embedding_model

        try:
            response = self.client.models.embed_content(
                model=model,
                contents=chunks,
                config={
                    "task_type": task_type.value
                }
            )

            return [e.values for e in response.embeddings]
        except Exception as e:
            raise ValueError(f"Failed to generate embeddings: {str(e)}")

    def get_retrieval_embeddings_for_list_of_chunks(self, chunks:list[str], model:Optional[str] = None) -> list[str]:
        return self.get_chunks(TaskType.DOCUMENT, chunks, model)

    def get_query_embeddings_for_list_of_chunks(self, chunks:list[str], model:Optional[str] = None) -> list[str]:
        return self.get_chunks(TaskType.QUERY, chunks, model)

    def get_response_based_on_context(self, queries:Union[List[str], str], model:Optional[str] = None, context:Optional[list[str]] = None) -> List[str]:

        if type(queries) == list:
            queries = "\n\n".join([f"Question {i + 1}: {text}" for i, text in enumerate(queries)])

        if context is None:
            context = "is not provided"
        else:
            context = "\n\n".join([f"Chunk {i + 1}: {chunk}" for i, chunk in enumerate(context)])

        if model is None:
            model = self.query_model

        prompt = \
        f"""
        Answer questions based on given context

        CONTEXT: '{context}'
        QUESTIONS: '{queries}'

        Write answer
        ANSWER:
        """
            # f"""You are a helpful and informative bot that answers questions using text from the reference passage included below. \
            # Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
            # However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
            # strike a friendly and conversational tone. \
            # If the passage is irrelevant to the answer, you may ignore it.


        try:
            response = self.client.models.generate_content(
                model=model,
                contents=prompt,
                config={
                    "response_mime_tpye": "application/list",
                    "response_schema": list[str],
                }
            )
        #TODO SOLVE Expected type 'Union[GenerateContentConfig, GenerateContentConfigDict, None]', got 'dict[str, Union[str, type[list[str]]]]' instead
            return response.parsed

        except Exception as e:
            print(e)

