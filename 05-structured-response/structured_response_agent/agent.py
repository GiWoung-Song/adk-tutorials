from google.adk.agents import LlmAgent

root_agent = LlmAgent(
    name="structured_response_agent",
    model="gemini-2.0-flash",
    description="항상 JSON 형태로 답변하는 에이전트",
    instruction="""
    당신은 구조화된 응답 에이전트입니다.
    어떤 질문이 들어오든 반드시 아래 JSON 형식으로만 답변하세요.

    {
      "summary": "핵심 요약",
      "action_items": ["실행 항목1", "실행 항목2"],
      "risk_level": "low|medium|high"
    }
    """
)
