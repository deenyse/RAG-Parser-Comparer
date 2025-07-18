from Parsers.PdfPlumber import ParsByPdfPlumber
from Tools.SymbolChunker import SymbolChunker

import yaml


if __name__ == "__main__":


    def load_config(file_path="config.yaml"):
        try:
            with open(file_path, "r") as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file {file_path} was not found.")
        except yaml.YAMLError as e:
            raise ValueError(f"YAML parsing issue: {str(e)}")


    # Загружаем конфигурацию
    config = load_config()
    GEMINI_API_KEY = config.get("gemini_api", {}).get("key")

    print("GEMINI API KEY: {}".format(GEMINI_API_KEY))

    # with SymbolChunker(ParsByPdfPlumber, "TestFiles/OverlapTest.pdf", 400, 70) as chunker:
    #     for block in chunker:
    #         print(block)
    #         print("--------")

    chunker = SymbolChunker(ParsByPdfPlumber, "TestFiles/OverlapTest.pdf", 400, 70)
    chunker.open()

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
