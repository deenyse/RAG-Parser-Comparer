from Parsers.PdfPlumber import ParsByPdfPlumber
from Tools.Chunkers.SymbolChunker import SymbolChunker
from Tools.config import get_config


if __name__ == "__main__":
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

    with SymbolChunker(ParsByPdfPlumber, "TestFiles/OverlapTest.pdf", 400, 70) as chunker:
        for chunk in chunker:
            print(chunk)

    # #WORKS
    # parser = ParsByPdfPlumber()
    # parser.open("TestFiles/ParserTestingPDF.pdf")
    #
    # print(next(iter(parser)))

    # #WORKS _2_

    # with ParsByPdfPlumber("TestFiles/ParserTestingPDF.pdf") as parser:
    #     for chunk in parser:
    #         print(chunk)
