from src.modules.parsers.ParserFactory import ParserFactory
from src.utils.Config import Config
from src.piplenes.RAGPipline import RagPipline
from src.modules.llms.GoogleGemini import Gemini
from src.modules.vector_dbs.ChromaDB import ChromaDB
from src.modules.chunkers.SymbolChunker import SymbolChunker
from src.utils.MongoDBHandler import MongoDBHandler
if __name__ == "__main__":


    mongo = MongoDBHandler(Config.get_value("mongodb", "uri"), Config.get_value("mongodb", "db_name"))
    file_names = ["data/UNKyrgystan.PDF"]
    questions = mongo.getFileQuestions("UNKyrgystan.PDF")
    rag_client = RagPipline(ParserFactory.py_mu_pfd_4_llm(), SymbolChunker, ChromaDB, Gemini(Config.get_value("gemini_config")), file_names, questions)
    answers = rag_client.process()
    print("\n\n".join(answers))


    # fm = FileManager()
    # fm.reinitFiles()
    # fm.updateFiles(mongo)
    # print()