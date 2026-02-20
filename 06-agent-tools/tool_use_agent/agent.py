from google.adk.agents import LlmAgent
from .tools import now_utc

root_agent = LlmAgent(
    name="tool_use_agent",
    model="gemini-2.0-flash",
    description="필요 시 도구를 호출해 답변 정확도를 높이는 에이전트",
    instruction="""
    당신은 도구 사용 에이전트입니다.
    사용자가 현재 시각을 물으면 반드시 `now_utc` 도구를 호출한 뒤 결과를 설명하세요.
    """,
    tools=[now_utc]
)
