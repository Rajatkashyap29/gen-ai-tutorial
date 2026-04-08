from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
loader = DirectoryLoader(
    path = 'files',
    glob= '*.pdf',
    loader_cls= PyPDFLoader
)

docs = loader.load()

print(docs)
print(docs[0].page_content)
print(docs[0].metadata)