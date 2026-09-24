import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


# Connect to the Mistral model running through Ollama
llm = ChatOllama(model="mistral")


# Create the chatbot prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful Data Science Assistant.
Explain Data Science concepts in simple and clear language.
Use examples when helpful."""
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])


# Connect the prompt to the LLM
chain = prompt | llm


# Store conversation histories
if "store" not in st.session_state:
    st.session_state.store = {}


def get_session_history(session_id):
    if session_id not in st.session_state.store:
        st.session_state.store[session_id] = InMemoryChatMessageHistory()
    return st.session_state.store[session_id]


# Add chat history to the chain
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)


# Streamlit application
st.title("Data Science Assistant")

if st.button("Clear Chat"):
    st.session_state.store.pop("user1", None)
    st.rerun()

history = get_session_history("user1")

for message in history.messages:
    if message.type == "human":
        with st.chat_message("user"):
            st.write(message.content)
    elif message.type == "ai":
        with st.chat_message("assistant"):
            st.write(message.content)

user_input = st.chat_input("Ask a Data Science question:")

if user_input:
    response = chain_with_history.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": "user1"}}
    )

    st.rerun()