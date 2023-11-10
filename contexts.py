from typing import Type

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.faiss import VectorStore, FAISS


class ExtractionContext:
    def __init__(self):
        pass

    def get_runnable(self):
        raise NotImplementedError("Not Implemented.")
    
    def invoke(self, *args, **kwargs):
        return self.get_runnable().invoke(*args, **kwargs)

class DocumentExtractionContext(ExtractionContext):
    def __init__(self, file_path:str):
        self.file_path = file_path

class StringExtractionContext(ExtractionContext):
    def __init__(self, data:list[str]=None, vector_store:VectorStore=None, embeddings=None):
        self.data = data or [""]
        self.embeddings = embeddings or OpenAIEmbeddings()
        self.vector_store = vector_store or self._init_vector_store(FAISS)

    def get_runnable(self):
        return self.vector_store.as_retriever()

    def _init_vector_store(self, vector_store_class:Type[VectorStore]):
        return vector_store_class.from_texts(
            texts=self.data,
            embedding=self.embeddings,
            #text_splitter=CharacterTextSplitter()
        )
