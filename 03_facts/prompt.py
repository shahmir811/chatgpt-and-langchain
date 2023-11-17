from dotenv import load_dotenv
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from redundant_filter_retriever import RedundantFilterRetriever
import langchain

langchain.debug = True

load_dotenv()
chat = ChatOpenAI()
embeddings = OpenAIEmbeddings()

# Below we are creating an instance of Chroma directly (not from Chroma.from_document),
# so we use embedding_function keyword instead of embedding
db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)

retriever = db.as_retriever()
# retriever = RedundantFilterRetriever(embeddings=embeddings, chroma=db)


chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff"
)

query = "What is an interesting fact about the English Language?"
result = chain.run(query)

print(result)
