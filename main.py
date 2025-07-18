from Parsers.PdfPlumber import ParsByPdfPlumber
from Tools.Chunkers.SymbolChunker import SymbolChunker
from Tools.config import get_config
from Tools.LLMs.GoogleGemini import Gemini

if __name__ == "__main__":
    config = get_config()

    gemini = Gemini(config["gemini_config"])

    context = ["im 21", "im student", "my name is Qwerz"]
    questions = ["how old im", "how old is student", "describe me", "do a brief story about me"]

    print(gemini.get_query_embeddings_for_list_of_chunks(questions))

    # # Load configuration
    # config = get_config()
    # GEMINI_API_KEY = config.get("gemini_api", {}).get("key")
    #
    # print("GEMINI API KEY: {}".format(GEMINI_API_KEY))

    # with SymbolChunker(ParsByPdfPlumber, "TestFiles/OverlapTest.pdf", 400, 70) as chunker:
    #     for block in chunker:
    #         print(block)
    #         print("--------")

    # chunker = SymbolChunker(ParsByPdfPlumber, "TestFiles/OverlapTest.pdf", 400, 70)
    # chunker.open()

    # with SymbolChunker(ParsByPdfPlumber, "TestFiles/OverlapTest.pdf", 400, 70) as chunker:
    #     for chunk in chunker:
    #         print(chunk)

    # #WORKS
    # parser = ParsByPdfPlumber()
    # parser.open("TestFiles/ParserTestingPDF.pdf")
    #
    # print(next(iter(parser)))

    # #WORKS _2_

    # with ParsByPdfPlumber("TestFiles/ParserTestingPDF.pdf") as parser:
    #     for chunk in parser:
    #         print(chunk)
