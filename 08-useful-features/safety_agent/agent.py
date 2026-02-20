from google.adk.agents import LlmAgent

root_agent = LlmAgent(
    name="safety_agent",
    model="gemini-2.0-flash",
    description="민감하거나 위험한 요청을 안전하게 처리하는 에이전트",
    instruction="""
    당신은 안전 보조 에이전트입니다.
    위험하거나 불법적인 요청은 정중히 거절하고, 안전한 대안을 제시하세요.
    """
)
