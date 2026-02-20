from google.adk.agents import LlmAgent

root_agent = LlmAgent(
    name="final_review_agent",
    model="gemini-2.0-flash",
    description="학습 내용을 복습하고 다음 단계를 안내하는 에이전트",
    instruction="""
    당신은 강의 마무리 에이전트입니다.
    지금까지 학습한 내용을 5줄 이내로 정리하고, 다음 실습 과제를 3개 제안하세요.
    """
)
