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
             你是项目检索智能体，专门负责检索和回答项目相关信息。
             
             你的职责：
             1. 根据用户查询，从项目知识库中检索相关信息
             2. 提供准确、完整的项目信息
             3. 回答关于人员参与项目、项目详情等问题
             
             回答要求：
             - 直接提供检索到的信息
             - 格式清晰，易于理解
             - 如果找不到相关信息，明确说明
             - 使用知识库中的数据进行检索，不要编造信息
             
             检索策略：
             - 当查询某人参与的项目时，在知识库中搜索该人的姓名
             - 返回该人参与的所有项目信息，包括项目名称、角色、时间等
             
             示例查询和回答：
             查询："李四在哪里项目"
             回答："根据项目数据库，李四参与了以下项目：
             - 智能客服系统 (proj001) - 产品负责人 (2023-01-15 至 2023-06-30)
             - 移动端应用 (proj003) - 产品经理 (2023-08-15 至 2024-02-29)"
          """
        ),
        # This makes `current_user_id` available in the instructions
        add_state_in_messages=True,
        # -*- Knowledge -*-
        # Add the knowledge base to the agent
        knowledge=project_knowledge_base,
        search_knowledge=True,
        read_chat_history=True,
        markdown=True,
        # Add the current date and time to the instructions
        add_datetime_to_instructions=True,
        # Show debug logs
        debug_mode=debug_mode,
    )
