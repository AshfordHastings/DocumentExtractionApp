from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS

class ExtractionContext:
    def __init__(self):
        pass

    def get_runnable(self):
        raise NotImplementedError("Not Implemented.")
    
class VectorStore:
    def __init__(self):
        pass

    def get_retriever(self):
        pass
    
class FAISSVectorStore:
    def __init__(self):
        pass

    def _generate_embeddings(self):
        return OpenAIEmbeddings()
    
    def generate_vector_store(self, data):
        return FAISS.from_texts(
            [data],
            embedding=self._generate_embeddings(),
            #text_splitter=CharacterTextSplitter()
        )
    
class ChromaVectorStore:
    def __init__(self):
        pass

class DocumentExtractionContext(ExtractionContext, FAISSVectorStore):
    def __init__(self, file_path:str):
        self.file_path = file_path

class StringExtractionContext(ExtractionContext, FAISSVectorStore):
    def __init__(self, data:str):
        self.data = data

    def get_runnable(self):
        return self.generate_vector_store(self.data).as_retriever()