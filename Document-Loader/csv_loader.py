from langchain_community.document_loaders import CSVLoader
loader = CSVLoader('social_network.csv')

docs = loader.load()
print(docs[0].page_content)