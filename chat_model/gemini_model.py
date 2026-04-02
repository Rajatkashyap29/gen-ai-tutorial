# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# model  = ChatGoogleGenerativeAI(model= 'gemini-2.5-flash')

# result = model.invoke("What is the capital of India")

# print(result.content)


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.2)

ip = input("Enter your qus")

qus_prompt = "You are a good teacher, You are expert in everythoing. Give output in only 30 words. "

qus = qus_prompt+ ip
result = model.invoke(qus)
print (result.content)