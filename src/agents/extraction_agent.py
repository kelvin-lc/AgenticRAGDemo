from textwrap import dedent
from typing import Optional

from agno.agent import Agent
from agno.models.openai import OpenAIChat

from src.config import settings


def get_extraction_agent(
    model_id: str = settings.OPENAI_MODEL,
    user_id: Optional[str] = None,
    session_id: Optional[str] = None,
    debug_mode: bool = settings.DEBUG_MODE,
) -> Agent:
    return Agent(
        name="Extraction Agent",
        agent_id="extraction_agent",
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
            你是一个extraction agent，主要职责是提取信息。

            你的目标是通过提供的Chunk切片内容，组合成一个完整的知识。
        """
        ),
        # Instructions for the agent
        instructions=dedent(
            """\
        请分析：
        1. 提取信息
        2. 组合成一个完整的知识
        
        以JSON格式返回提取结果。
        
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
