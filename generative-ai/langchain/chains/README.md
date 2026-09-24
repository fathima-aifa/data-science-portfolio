# LangChain Projects

This folder contains practical projects and experiments built while learning and exploring LangChain.

## Projects

### Blog Post Generator

A simple Streamlit application that uses a sequential chain to generate a blog post outline and then create an engaging introduction based on the generated outline.

**Concepts:** PromptTemplate, LCEL, Sequential Chains, StrOutputParser

### Marketing Email Generator

A Streamlit application that uses sequential chains to generate a marketing email subject line and create a structured email based on the product, features, and target audience.

The final output is parsed into a JSON structure using `JsonOutputParser`.

**Concepts:** PromptTemplate, Sequential Chains, Lambda Functions, StrOutputParser, JsonOutputParser

### Data Science Assistant with Chat History

A Streamlit-based chatbot that answers Data Science questions using Mistral through Ollama. The application maintains conversation history, allowing the assistant to understand follow-up questions based on previous messages.

**Concepts:** ChatPromptTemplate, MessagesPlaceholder, InMemoryChatMessageHistory, RunnableWithMessageHistory, Streamlit Session State

## Technologies

* Python
* LangChain
* Ollama
* Mistral
* Streamlit



