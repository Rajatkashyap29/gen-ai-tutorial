from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('6-sem-cse.pdf')

docs = loader.load()
print(docs)
print(docs[0].page_content)
print(docs[0].metadata)
