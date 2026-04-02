from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name, age, city of a fictional person.\n{format_instructions}',
    input_variables=[],
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)

prompt = template.format()

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)