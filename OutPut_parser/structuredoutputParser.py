from dotenv import load_dotenv
from pydantic import BaseModel

from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()


# Define schema using Pydantic
class Facts(BaseModel):
    fact_1: str
    fact_2: str
    fact_3: str


# Initialize model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Attach structured output
structured_model = model.with_structured_output(Facts)

# Invoke
result = structured_model.invoke("Give three facts about black holes")

print(result)