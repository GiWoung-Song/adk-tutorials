from google.adk.agents import LlmAgent

root_agent = LlmAgent(
    name="deploy_ready_agent",
    model="gemini-2.0-flash",
    description="배포 준비 상태를 점검하는 에이전트",
    instruction="""
    당신은 배포 점검 에이전트입니다.
    요청을 받으면 관측성, 장애 대응, 비용, 보안 관점 체크리스트를 제시하세요.
    """
)
