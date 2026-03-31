from google.adk.agents import Agent
from tools.company_tool import get_code, get_company_info

company_agent = Agent(
    name='company_agent',
    model="gemini-2.5-flash",
    description='기업 정보 제공',
    instruction='기업 정보를 출력',
    output_key='company_info',
    tools=[get_code, get_company_info]
)
