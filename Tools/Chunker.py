from ClassInterfaces import IChunker, IParser

class Chunker:
    input_text_buffer = ''

    prev_chunk_overlap = ""
    new_chunk = ""

    def __init__(self, parser: IParser, chunk_size:int, overlap_size:int) -> None:
        self.parser = parser
        self.chunk_size = chunk_size
        self.overlap_size = overlap_size

    def open(self, file_name:str) -> None:
        self.parser.open(file_name)

    def close(self) -> None:
        self.parser.close()


    def expand_input_text_buffer(self):
        next_text = self.parser.get_next_text_block()

        if next_text is None:
            raise Exception("Chunker says: No text left in file")

        self.input_text_buffer += next_text

    def expand_chunk_buffer(self):
        if len(self.input_text_buffer) < self.chunk_size:
            self.expand_input_text_buffer()

        #TODO HERE PLACE TO ADD PARAGRAPHS INTO NEW CHUNK


# TODO: figure out a way to normally refill input text buffer. Than normally add new paragraphs into new_chunk.
#  Probably rethink way to work with files.
#  something like file=parser.open("FILEPATH"). So o logically work with file, not parser. Or maby this is stupid -_-


    def get_next_chunk(self) -> str or None:
        self.new_chunk = self.prev_chunk_overlap

        while len(self.new_chunk) < self.chunk_size:
            self.expand_chunk_buffer()
            if self.new_chunk == '':
                break


        self.prev_chunk_overlap = self.new_chunk[:self.overlap_size]
        return self.new_chunk



