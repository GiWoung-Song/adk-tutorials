from google.adk.agents import LlmAgent

root_agent = LlmAgent(
    name="memory_agent",
    model="gemini-2.0-flash",
    description="대화 중 수집된 사용자 선호를 기억해 응답하는 에이전트",
    instruction="""
    당신은 메모리 에이전트입니다.
    사용자가 말한 선호(예: 좋아하는 언어, 학습 목표)를 기억하고 다음 답변에 반영하세요.
    """
)
