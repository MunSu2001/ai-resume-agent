from google.adk.agents import ParallelAgent, SequentialAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

from agents.company_agent import company_agent
from agents.news_agent import news_agent
from agents.resume_agent import resume_agent
from agents.final_agent import summarizer

parallel_fet = ParallelAgent(
    name="multi_info_fetcher",
    sub_agents=[company_agent, news_agent, resume_agent],
)

root_agent = SequentialAgent(
    name="ai_resume_system",
    sub_agents=[parallel_fet, summarizer],
)

session_service = InMemorySessionService()

runner = Runner(
    agent=root_agent,
    app_name="resume_app",
    session_service=session_service
)
