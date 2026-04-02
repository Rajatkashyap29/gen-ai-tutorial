from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content='you are a helpful {domain} expert'),
    HumanMessage(content='explain in simple term, what is {topic}')
])

prompt = chat_template.invoke({
    'domain': 'cricket',
    'topic': 'dusra'
})

print(prompt)