from google.adk.agents import LlmAgent, SequentialAgent

planner_agent = LlmAgent(
    name="planner_agent",
    model="gemini-2.0-flash",
    description="요청을 작업 단계로 나누는 플래너",
    instruction="""
    당신은 플래너입니다.
    사용자의 요청을 3단계 실행 계획으로 정리하세요.
    """,
    output_key="plan"
)

executor_agent = LlmAgent(
    name="executor_agent",
    model="gemini-2.0-flash",
    description="플랜을 바탕으로 초안을 작성하는 실행자",
    instruction="""
    당신은 실행자입니다.
    세션 상태의 `plan`을 참고해 사용자 요청에 대한 실행 결과 초안을 작성하세요.
    """
)

root_agent = SequentialAgent(
    name="team_coordinator_agent",
    description="플래너와 실행자가 협업하는 멀티 에이전트",
    sub_agents=[planner_agent, executor_agent]
)
