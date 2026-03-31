from google.adk.agents import Agent
from google.adk.tools import google_search

news_agent = Agent(
    name="news_agent",
    model="gemini-2.5-flash",
    instruction="기업 뉴스 요약 및 전망 분석",
    tools=[google_search],
    output_key='news_info'
)
