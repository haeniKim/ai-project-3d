from flask import Flask, Blueprint, request, jsonify
import os
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain

# bp = Blueprint('chat', __name__, url_prefix= '/chat')

# # API_KEY
# os.environ["OPENAI_API_KEY"] = "KEY"

# # PDF Loading
# loader = PyPDFLoader("static/pdf/china_studybook.pdf")
# documents = loader.load()

# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# texts = text_splitter.split_documents(documents)

# # Embedding
# embeddings = OpenAIEmbeddings()
# vector_store = Chroma.from_documents(texts, embeddings)
# retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# # Prompt
# prompt_template="""
# You are a Korean tutor and need to kindly teach a multicultural elementary school student
# how Korean culture compares to the culture of the china. 
# {summaries}
# Please give your answer in Korean in 200 characters or less.
# """
# # system_template="""Use the following pieces of context to answer the users question shortly.
# # Given the following summaries of a long document and a question, create a final answer with references ("SOURCES"), use "SOURCES" in capital letters regardless of the number of sources.
# # If you don't know the answer, just say that "I don't know", don't try to make up an answer.
# # ----------------
# # {summaries}

# # You MUST answer in Korean and in Markdown format:"""

# messages = [
#     SystemMessagePromptTemplate.from_template(prompt_template),
#     HumanMessagePromptTemplate.from_template("{question}")
# ]

# prompt = ChatPromptTemplate.from_messages(messages)

# chain_type_kwargs = {"prompt": prompt}

# llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)  # Modify model_name if you have access to GPT-4

# chain = RetrievalQAWithSourcesChain.from_chain_type(
#     llm=llm,
#     chain_type="stuff",
#     retriever = retriever,
#     return_source_documents=True,
#     chain_type_kwargs=chain_type_kwargs
# )


# @bp.route('/', methods = ['POST', 'GET'])
# def chat_query():
#     if request.method == 'POST':
#         data = request.get_json()
#         query = data.get('query')
#         result = chain(query)

#         answer = result['answer']

#         result = {'answer': answer}
#         return jsonify(result)
    
