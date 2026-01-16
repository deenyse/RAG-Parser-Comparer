from PIL.PdfParser import PdfParser

from Parsers.LlamaParse import LlamaParseMd
from Tools.config import get_config
from Tools.RAGPipline import RagPipline
from LLMs.GoogleGemini import Gemini
from DBs.ChromaDB import ChromaDB
from Chunkers.SymbolChunker import SymbolChunker
from Tools.MongoDBHandler import MongoDBHandler
from Tools.FileManager import FileManager
from Parsers.PdfPlumber import PdfPlumber
from Parsers.PyMuPdf4LLM import PyMuPdf4LLM
from Parsers.PyMuPdfRaw import PyMuPdfRaw
from Parsers.DoclingParse import DoclingParser
from Parsers.AzureParse import AzureDocumentParser


if __name__ == "__main__":
    # Load configuration
    config = get_config()

    # file_names = ["TestFiles/2025pb-web.pdf"]
    # questions = [
    #     "How did the share of Asia (excluding China) in the world Total Energy Supply change between 1990 and 2022, and what was the absolute TES growth (in EJ) over this period?",
    #     "Compare the energy intensity (GJ per thousand dollars) of China and Iceland in 2022. By how many times is Iceland more energy-intensive than China?",
    #     "For the United States: how did electricity generation from coal change between 1990 and 2022 (in TWh), and how did the coal share in the electricity mix change?",
    #     "For Europe: calculate the ratio between natural gas consumption in Total Final Consumption and its share in thermal electricity generation (natural-gas-based) in 2022.",
    #     "What was the ratio between Primary Energy Production and Total Energy Supply in Saudi Arabia in 2022, and did the country exceed 100% self-sufficiency?",
    #     "Which energy source showed the largest increase in global Total Energy Supply between 1990 and 2022 (in EJ), and which source showed the largest decrease?",
    #     "Compare global coal and oil production trends from 1990 to 2022. In which year did coal first surpass oil?",
    #     "Using the 'electricity capacity by type 1990–2022' chart, how did the contribution of solar power to global installed capacity change (in GW and % of total capacity)?",
    #     "How did the share of renewable electricity in global power generation change between 2010 and 2022, and which renewable category contributed the most to this growth?",
    #     "Based on the refinery output chart (1990–2022), which refinery product (naphtha, kerosene, gasoline, fuel oil, other) increased the fastest between 2000 and 2022?",
    #     "Which region had the highest Total Final Consumption per capita in 2022, and which had the lowest? What is the difference between these values?",
    #     "Compare renewable electricity generation in China and Europe. For which renewable type is the gap the largest?",
    #     "Which region produced the most biofuels and waste in 2022, and what share of this production came from fuelwood?",
    #     "Which three countries had the highest renewable electricity capacity per capita in 2022, and how do they compare to the world average?",
    #     "Where does India rank in Asia (excluding China) in electricity generation from wind and solar sources?",
    #     "Compare the growth of solar electricity generation (1990–2022) with the growth of installed solar capacity. Which grew faster: generation or capacity?",
    #     "How did China’s energy intensity (GJ per thousand $) change relative to its TES per capita between 2000 and 2022, and what does this imply about economic efficiency?",
    #     "How are changes in global refinery output related to changes in transport sector TFC between 2000 and 2022? Is there an observable correlation?",
    #     "Compare the share of coal in China’s TES, in primary production, and in electricity generation. Why do these shares differ? Provide numeric values.",
    #     "Compare CO₂ emissions from fossil fuels across regions with their shares in Total Energy Supply. Does the emissions share match the energy share? Where is the discrepancy largest?"
    # ]

    mongo = MongoDBHandler(config)
    file_names = ["TestFiles/UNKyrgystan.PDF"]
    questions = mongo.getFileQuestions("UNKyrgystan.PDF")
    rag_client = RagPipline(PyMuPdf4LLM(), SymbolChunker, ChromaDB, Gemini(config["gemini_config"]), file_names, questions)
    answers = rag_client.process()
    print("\n\n".join(answers))


    # fm = FileManager()
    # fm.reinitFiles()
    # fm.updateFiles(mongo)
    # print()