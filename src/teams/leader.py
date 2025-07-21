"""团队协调器 - 基于Agno框架的Coordinate模式团队。

该模块实现了一个包含项目智能体和关系智能体的协调团队，
采用Agno框架的Coordinate模式进行智能体协作。
"""

from typing import Optional

from agno.models.openai import OpenAIChat
from agno.team.team import Team

from src.agents.project_retrival_agent import get_project_agent
from src.agents.relationships_retrival_agent import get_relationships_agent
from src.agents.query_agent import get_query_agent
from src.agents.extraction_agent import get_extraction_agent
from src.agents.validation_agent import get_validation_agent
from src.config import settings


def get_agentic_rag_team(
    user_id: Optional[str] = None,
    session_id: Optional[str] = None,
) -> Team:
    return Team(
        name="Agentic RAG Team",
        mode="coordinate",
        user_id=user_id,
        session_id=session_id,
        model=OpenAIChat(
            id=settings.OPENAI_MODEL,
            base_url=settings.OPENAI_BASE_URL,
            api_key=settings.OPENAI_API_KEY,
        ),
        instructions=[
            "你是Agentic RAG团队的领导者，负责协调团队成员完成用户查询。",
            "",
            "工作流程：",
            "1. 首先使用Query Agent分析用户查询意图",
            "2. 然后使用Project Agent检索项目相关信息",
            "3. 使用Relationships Agent检索关系信息（如果需要）",
            "4. 使用Extraction Agent整合和提取关键信息",
            "5. 使用Validation Agent验证答案的准确性",
            "6. 最后你综合所有信息，直接回答用户的问题",
            "",
            "重要规则：",
            "- 你必须按照上述流程逐步执行，不能跳过任何步骤",
            "- 每个步骤都要等待Agent完成后再进行下一步",
            "- 最终答案必须由你直接提供，不要只是转交任务",
            "- 如果查询关于某人参与的项目，必须使用Project Agent检索并回答",
            "- 回答要简洁明了，直接给出用户想要的信息",
            "- 确保Project Agent能够访问到项目知识库中的数据",
            "- 如果Project Agent没有找到信息，检查知识库是否正确加载",
            "",
            "执行要求：",
            "- 当Query Agent完成分析后，你必须立即调用Project Agent",
            "- 不要只停留在Query Agent的分析结果上",
            "- 必须完成整个检索和回答流程",
            "- 最终要给出具体的答案，而不是过程描述",
            "",
            "示例：",
            "用户问：'李四在哪里项目'",
            "你应该：",
            "1. 让Query Agent分析查询意图",
            "2. 让Project Agent检索李四的项目信息",
            "3. 直接回答：'李四参与了以下项目：[具体项目列表]'",
            "",
            "注意：不要只执行Query Agent就结束，必须继续执行后续步骤！",
        ],
        members=[
            get_query_agent(),
            get_project_agent(),
            get_relationships_agent(),
            get_extraction_agent(),
            get_validation_agent(),
        ],
        add_datetime_to_instructions=True,
        markdown=True,
        debug_mode=settings.DEBUG_MODE,
        show_members_responses=True,  # 改为True以便调试
    )
