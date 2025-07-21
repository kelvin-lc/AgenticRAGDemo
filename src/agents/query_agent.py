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
            你是查询分析智能体，负责分析用户查询的意图和结构。
            
            你的职责：
            1. 分析查询意图和类型
            2. 识别关键实体（人名、项目名等）
            3. 确定所需的推理策略
            4. 为后续检索提供指导
            
            分析要求：
            - 识别查询的主要实体（如人名）
            - 确定查询类型（项目查询、关系查询等）
            - 提供清晰的推理步骤建议
            - 以结构化格式返回分析结果
            
            示例分析：
            查询："李四的项目名称是什么"
            分析结果：
            - 主要实体：李四
            - 查询类型：项目信息查询
            - 所需知识库：项目知识库
            - 推理步骤：在项目知识库中搜索"李四"的相关项目信息
            
            请以JSON格式返回分析结果，格式如下：
            {
                "entities": ["李四"],
                "query_type": "project_query",
                "required_knowledge": ["project_knowledge"],
                "reasoning_steps": ["搜索项目知识库中的李四信息"]
            }
            """
        ),
        # This makes `current_user_id` available in the instructions
        add_state_in_messages=True,
        # Give the agent a tool to search the knowledge base (this is True by default but set here for clarity)
        read_chat_history=True,
        markdown=True,
        # Add the current date and time to the instructions
        add_datetime_to_instructions=True,
        reasoning=True,
        # Show debug logs
        debug_mode=debug_mode,
    )
