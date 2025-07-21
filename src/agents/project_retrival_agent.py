from textwrap import dedent
from typing import Optional

from agno.agent import Agent
from agno.models.openai import OpenAIChat

from src.config import settings
from src.knowledges.projects_csv_knowledge import project_knowledge_base


def get_project_agent(
    model_id: str = settings.OPENAI_MODEL,
    user_id: Optional[str] = None,
    session_id: Optional[str] = None,
    debug_mode: bool = settings.DEBUG_MODE,
) -> Agent:
    return Agent(
        name="Project Agent",
        agent_id="project_agent",
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
            You are Project Agent, an advanced AI Agent specializing in Project Management.

            Your goal is to help developers understand and use Project Management by providing clear explanations, functional code examples, and best-practice guidance for using Project Management.
        """
        ),
        # Instructions for the agent
        instructions=dedent(
            """\
           你是一个retrieval agent，主要职责是检索项目信息。

           你的目标是通过提供的查询意图，检索项目信息。
        """
        ),
        # This makes `current_user_id` available in the instructions
        add_state_in_messages=True,
        # -*- Knowledge -*-
        # Add the knowledge base to the agent
        knowledge=project_knowledge_base,
        # Give the agent a tool to search the knowledge base (this is True by default but set here for clarity)
        search_knowledge=True,
        read_chat_history=True,
        markdown=True,
        # Add the current date and time to the instructions
        add_datetime_to_instructions=True,
        # Show debug logs
        debug_mode=debug_mode,
    )
