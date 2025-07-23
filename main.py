from PIL.PdfParser import PdfParser

from Parsers.LlamaParse import LlamaParser
from Tools.config import get_config
from LLMs.GoogleGemini import Gemini
from Tools.RAGPipline import RagPipline
from Chunkers.SymbolChunker import SymbolChunker
from Parsers.PdfPlumber import ParsByPdfPlumber
from DBs.ChromaDB import ChromaDB

if __name__ == "__main__":
    # Load configuration
    config = get_config()

    file_names = ["TestFiles/biography.pdf","TestFiles/biography2.pdf"]
    questions = [
        "Чё Ваня Петров делал для природы где-то в Сибири?",
        "Иван Петров тусовался с исследованиями про климат и всякое такое?",
        "Какую штуку для лесов придумал Ваня Петров?",
        "Давали ли Ивану Петрову какие-нибудь награды за экологию?",
        "Ваня Петров писал что-нибудь про сибирскую природу?",
        "Когда Иван Петров начал копаться в науке про экологию?",
        "Как Ваня Петров в интернете про науку заливал?",
        "Какую движуху для школьников замутал Иван Петров?",
        "Чё Ваня Петров делал, чтобы животных спасти?",
        "Тусил ли Иван Петров на каком-нибудь форуме про природу?"
    ]

#TODO: Unify parser interface, to be able treated as same module
    rag_client = RagPipline(ParsByPdfPlumber, LlamaParser(config["llama_parse"]).get_parser(), ChromaDB, Gemini, config["gemini_config"], file_names, questions)
    answers = rag_client.process()
    print("\n\n".join(answers))




    # parser = LlamaParser(config["llama_parse"], "TestFiles/Monopoly.pdf")



    # parser = LlamaParser(config["llama_parse"],"TestFiles/Monopoly.pdf")
    # text = parser.get_next_text_block()
    # while text is not None:
    #     print(text)
    #     text = parser.get_next_text_block()

#TODO:
# ----------FUTURE_PLANS----------
# 6. Implement further parsers.
# 7. Check how systems are interchangeable(i mean parsers, DBs, LLMs, etc.)
# ----------STRUCTURE_SIMPLIFICATION----------
# 3. Do i really need all those chunkers(i assume yes, because the way i treat context can influence output)
