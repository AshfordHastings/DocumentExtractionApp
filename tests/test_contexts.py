import os
import pytest

from dataclasses import dataclass
from langchain.text_splitter import CharacterTextSplitter

from langchain_app.contexts import (
    StringExtractionContext
)

TEST_DOC_PATH = os.path.join(os.getenv("BASE_PATH"), "tests/data/state_of_the_union.txt")

@dataclass
class TestDocument:
    split_text:list[str]
    test_query:str

@pytest.fixture()
def test_document_state_of_union():
    full_text = open(TEST_DOC_PATH, "r").read()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_text = text_splitter.split_text(full_text)
    test_query = "What did the president say about technology?"

    yield TestDocument(split_text, test_query)
    

def test_extraction_context_from_text():
    context = StringExtractionContext("Hello world")
    assert context.data == "Hello world"
    assert context.vector_store is not None
    assert context.embeddings is not None
    assert context.vector_store.as_retriever() is not None

def test_extraction_context_from_document(test_document_state_of_union:TestDocument):
    context = StringExtractionContext(data=test_document_state_of_union.split_text)
    retrieved_docs = context.invoke(test_document_state_of_union.test_query)

    print(retrieved_docs[0].page_content)

