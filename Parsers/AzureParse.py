from ClassInterfaces.IParser import IParser
from typing import Optional, Iterator

from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient


class AzureDocumentParser(IParser):
    client: Optional[DocumentIntelligenceClient] = None
    pages_iterator: Optional[Iterator[str]] = None

    def __init__(self, config: Optional[dict] = None) -> None:

        endpoint = config["azure"]["endpoint"]
        api_key = config["azure"]["api_key"]

        if not endpoint or not api_key:
            raise ValueError("Azure Endpoint or API Key is missing in config or env variables.")

        try:
            self.client = DocumentIntelligenceClient(
                endpoint=endpoint,
                credential=AzureKeyCredential(api_key)
            )
        except Exception as e:
            raise Exception(f"Failed to initialize Azure client: {e}")

    def open(self, file_name: Optional[str]) -> None:
        try:
            if not file_name:
                raise ValueError("File name is required")

            print(f"Sending {file_name} to Azure AI Document Intelligence...")

            with open(file_name, "rb") as f:
                file_content = f.read()

            poller = self.client.begin_analyze_document(
                model_id="prebuilt-layout",
                body=file_content,
                content_type="application/octet-stream",
                output_content_format="markdown"
            )

            result = poller.result()

            self.pages_iterator = self._split_content_by_pages(result)

        except Exception as e:
            raise Exception(f"Error processing file with Azure: {e}")

    def _split_content_by_pages(self, result) -> Iterator[str]:
        full_content = result.content

        if not result.pages:
            yield full_content
            return

        for page in result.pages:
            page_text_parts = []
            if page.spans:
                for span in page.spans:
                    start = span.offset
                    end = span.offset + span.length
                    page_text_parts.append(full_content[start:end])

            yield "".join(page_text_parts)

    def get_next_text_block(self) -> Optional[str]:
        try:
            if self.pages_iterator is None:
                raise Exception("File is not open. Call open() first.")

            return next(self.pages_iterator)

        except StopIteration:
            return None
        except Exception as e:
            print(f"Error reading next block: {e}")
            return None

    def close(self) -> None:
        self.pages_iterator = None