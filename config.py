import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool
# Load environment variables
load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the LLM
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model='gpt-4o-mini')

# Initialize the search tool
search_tool =   SerperDevTool()
