import getpass
import os
from langchain.chat_models import init_chat_model  
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate


try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

os.environ["LANGSMITH_TRACING"]="true"
if "LANGSMITH_API_KEY" not in os.environ:
    os.environ["LANGSMITH_API_KEY"]=getpass.getpass(
        prompt="Enter your LANGSMITH_API_KEY (optional):"
    )
if "LANGSMITH_PROJECT" not in os.environ:
    os.environ["LANGSMITH_PROJECT"] = getpass.getpass(
        prompt='Enter your LangSmith Project Name (default = "default"): '
    )
    if not os.environ.get("LANGSMITH_PROJECT"):
        os.environ["LANGSMITH_PROJECT"]="default";

if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")



model = init_chat_model("llama-3.1-8b-instant", model_provider="groq")


#Translator

system_template = "Translate the following from English into {language}"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

text_to_translate = input("Enter the text you want to translate:")
translate_language = input("Enter the language in which you want the text to be translated to: ")

chain = prompt_template | model
result = chain.invoke({
    "language": translate_language,
    "text": text_to_translate
})
print("Result:", result.content)

#Summarizer 

# system_template= "Summarise the following text in English using only 50 words."



# prompt_template = ChatPromptTemplate.from_messages([
#     ("system", system_template),
#     ("user", "{text}")
# ])

# text_to_summarise = input("Enter the text you want to summarise:").strip()

# if not text_to_summarise:
#     print("No text entered. Please provide text to summarise.")
#     exit()
# chain= prompt_template|model
# result = chain.invoke({
#     "text":text_to_summarise
# })
# print("Result: ", result.content)

