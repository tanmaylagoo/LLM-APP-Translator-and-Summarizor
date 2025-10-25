# LangChain Translator & Summarizer

A simple yet powerful command-line tool built with [LangChain](https://www.langchain.com/) and Groq's LLaMA 3.1 model. Translate English text into any language and a second separate program to summarise long passages made using similar concepts as the language translator.

---

## Features

- **Translator**: Convert English text into any target language using dynamic prompt chaining.
- **Summarizer** *(optional)*: Generate concise 50-word summaries of English text.
- **Secure API Handling**: Uses `getpass` to safely input LangSmith and Groq API keys.
- **Environment Support**: Loads `.env` variables automatically with `python-dotenv`.
- **LangSmith Tracing**: Enables tracing for debugging and performance insights.

---

## Requirements

- Python 3.8+
- Install dependencies:

```bash
pip install langchain langchain-core groq python-dotenv
