from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma

load_dotenv()

embeddings = OpenAIEmbeddings()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)

loader = TextLoader("facts.txt")
docs = loader.load_and_split(
    text_splitter=text_splitter
)

db = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="emb"
)

query = "What is an interesting fact about the English Language?"
# results = db.similarity_search(query)  # Retrieves data without score
# results = db.similarity_search_with_score(query, k=2)  # k=2 means only get top 02 most relevant records
results = db.similarity_search_with_score(query)  # k=2 means only get top 02 most relevant records


for result in results:
    print('\n')
    print(result[1])
    print(result[0].page_content)



