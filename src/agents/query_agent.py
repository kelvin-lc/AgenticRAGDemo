from textwrap import dedent
from typing import Optional

from agno.agent import Agent
from agno.models.openai import OpenAIChat

from src.config import settings


def get_query_agent(
    model_id: str = settings.OPENAI_MODEL,
    user_id: Optional[str] = None,
    session_id: Optional[str] = None,
    debug_mode: bool = settings.DEBUG_MODE,
) -> Agent:
    return Agent(
        name="Query Agent",
        agent_id="query_agent",
        user_id=user_id,
        session_id=session_id,
        model=OpenAIChat(
            id=model_id,
            base_url=settings.OPENAI_BASE_URL,
            api_key=settings.OPENAI_API_KEY,
        ),
        # Description of the agent
        description=dedent(
            """\
            你是一个query agent，主要职责是查询意图和所需的推理策略。

            你的目标是通过提供清晰的解释、功能代码示例和最佳实践指导，帮助开发人员理解并使用知识库。
        """
        ),
        # Instructions for the agent
        instructions=dedent(
            """\
        请分析：
        1. 查询意图
        2. 涉及的实体
        3. 是否需要多跳推理
        4. 推理步骤
        
        以JSON格式返回分析结果。
        """
        ),
        # This makes `current_user_id` available in the instructions
        add_state_in_messages=True,
        # Give the agent a tool to search the knowledge base (this is True by default but set here for clarity)
        read_chat_history=True,
        markdown=True,
        # Add the current date and time to the instructions
        add_datetime_to_instructions=True,
        # Show debug logs
        debug_mode=debug_mode,
    )
