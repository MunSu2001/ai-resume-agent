from google.adk.agents import Agent

summarizer = Agent(
    name='final_agent',
    model="gemini-2.5-flash",
    instruction="""
    기업 정보 : {company_info}
    뉴스 : {news_info}
    자기소개서 : {resume_info}

    최종 자기소개서 생성
    """
)
