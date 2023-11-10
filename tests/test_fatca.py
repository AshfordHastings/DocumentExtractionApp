import os
import pytest

from dataclasses import dataclass
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.llms.openai import OpenAI
from langchain.schema.output_parser import StrOutputParser

from langchain_app.contexts import (
    DocumentExtractionContext
)

TEST_DOC_PATH = os.path.join(os.getenv("BASE_PATH"), "tests/data/example_fatca.pdf")

TEST_FORMAT_INSTRUCTIONS = """
Answser the following query according the context given below. 
"""

TEST_TEMPLATE = """
{format_instructions}
{query}
Context:
{context}
"""



@dataclass
class TestDocument:
    test_data:any
    test_query:str

@pytest.fixture()
def test_document_fatca():
    loader = PyPDFLoader(TEST_DOC_PATH)
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    #text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    pages = loader.load_and_split(text_splitter)
    yield TestDocument(pages, "What is the Financial Institution’s country/jurisdiction of residence for tax purposes?")
    

@pytest.mark.skip('Completed')
def test_extraction_context_from_document(test_document_fatca:TestDocument):
    context = DocumentExtractionContext(data=test_document_fatca.test_data)
    #retrieved_docs = context.invoke(test_document_fatca.test_query)
    #retrieved_docs = context.vector_store.similarity_search(test_document_fatca.test_query)
    retrieved_docs = context.vector_store.similarity_search_with_score(test_document_fatca.test_query)
    for doc in retrieved_docs:
        print(f"Score:\n{doc[1]}r\n\nChunk:\n{doc[0].page_content}")
    #print(f"Score:\n{retrieved_docs[0][1]}r\n\nChunk:\n{retrieved_docs[0][0].page_content}")

def test_extraction_from_document(test_document_fatca:TestDocument):
    context = DocumentExtractionContext(data=test_document_fatca.test_data)
    prompt_template = PromptTemplate(
        template=TEST_TEMPLATE,
        input_variables=["context", "query"],
        partial_variables={"format_instructions": TEST_FORMAT_INSTRUCTIONS}
    )
    chain = (
        {"context": context.get_runnable(), "query": RunnablePassthrough()}
        | prompt_template
        | OpenAI()
        | StrOutputParser()
    )
    chain_result = chain.invoke(test_document_fatca.test_query)
    print(chain_result)
