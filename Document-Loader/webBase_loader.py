import os
from dotenv import load_dotenv

os.environ["USER_AGENT"] = "Mozilla/5.0"

from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt = PromptTemplate(
    template='Answer the following question:\n{question}\nfrom the following text:\n{text}',
    input_variables=['question', 'text']
)

parser = StrOutputParser()

url = 'https://en.wikipedia.org/wiki/MacBook_Air'

loader = WebBaseLoader(url)
docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({
    'question': 'What product are we talking about?',
    'text': docs[0].page_content
})

print(result)