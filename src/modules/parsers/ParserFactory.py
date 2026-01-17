from azure.core.credentials import AzureKeyCredential
from llama_cloud_services import LlamaParse

from src.modules.parsers.AzureParse import AzureDocumentParser
from src.modules.parsers.DoclingParse import DoclingParser
from src.modules.parsers.PdfPlumber import PdfPlumber
from src.modules.parsers.PyMuPdf4LLM import PyMuPdf4LLM
from src.modules.parsers.PyMuPdfRaw import PyMuPdfRaw
from src.utils.Config import Config


class ParserFactory:
    @staticmethod
    def azure():
        return AzureDocumentParser(
            api_key=Config.get_value("azure", "api_key"),
            endpoint=Config.get_value("azure", "endpoint"),
        )

    @staticmethod
    def docling():
        return DoclingParser()

    @staticmethod
    def docx_default():
        return DoclingParser()

    @staticmethod
    def llama():
        return LlamaParse(
            api_key=Config.get_value("llama_parse", "api_key"),
        )

    @staticmethod
    def pdf_plumber():
        return PdfPlumber()

    @staticmethod
    def py_mu_pfd_4_llm():
        return PyMuPdf4LLM()

    @staticmethod
    def py_mu_pfd_raw():
        return PyMuPdfRaw()

