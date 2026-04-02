from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_history = []

with open('chat_history.txt') as f:
    lines = f.readlines()

    for line in lines:
        chat_history.append(HumanMessage(content=line.strip()))

print(chat_history)

prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': 'where is my refund'
})

print(prompt)