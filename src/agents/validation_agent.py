from textwrap import dedent
from typing import Optional

from agno.agent import Agent
from agno.models.openai import OpenAIChat

from src.config import settings


def get_validation_agent(
    model_id: str = settings.OPENAI_MODEL,
    user_id: Optional[str] = None,
    session_id: Optional[str] = None,
    debug_mode: bool = settings.DEBUG_MODE,
) -> Agent:
    return Agent(
        name="Validation Agent",
        agent_id="validation_agent",
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
            你是一个validation agent，主要职责是验证最终答案是否正确,提供置信度。
        """
        ),
        # Instructions for the agent
        instructions=dedent(
            """\
        请分析：
        1. 验证最终答案
        
        以置信度返回验证结果。
        
        示例：
        
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
