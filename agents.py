from crewai import Agent
from tools import yt_tool
from langchain_google_genai import ChatGoogleGenerativeAI

import os 
from dotenv import load_dotenv
load_dotenv()

os.environ["GEMINI_API_KEY"]=os.getenv("GEMINI_API_KEY")

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash",model_provider="google_genai")

blog_reasercher=Agent(
    role="you are a blog reasercher from youtube videos",
    goal="get the relevent video content for the topic{topic} from youtube channel",
    verbose=True,
    memory=True,
    backstory="you are expert in understanding videos in Ai,Data secience,Machine Leearning and provide suggestion",
    tools=[yt_tool],
    llm=model,
    allow_delegation=True

)

blog_writer=Agent(
    role="Blog Writer",
    goal="write a blog on the topic {topic} with the content provided by the creator",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
) ,  
    tools=[yt_tool],
    llm=model,
    allow_delegation=False

)