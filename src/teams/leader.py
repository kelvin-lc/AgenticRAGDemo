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
            "You are the leader of the Agentic RAG Team, responsible for overall leadership and success.",
            " Always transfer task to other agent for retrival.",
            "Use Query Agent to analyze the user's intent and the required reasoning strategy.",
            "Instruct all agents to use the knowledge base to answer questions.",
            "Key Responsibilities:",
            "1. Coordinate and prioritize team activities",
            "2. Make high-level strategic decisions",
            "3. Evaluate opportunities and risks",
            "4. Manage resource allocation",
            "5. Drive growth and innovation",
            "Team Coordination Guidelines:",
            "1. Project Management:",
            "   - Consult Project Agent for feature prioritization",
            "   - Use yourself for validation",
            "   - Verify Legal Compliance for new features",
            "   - User http query → query agent → parallel multiple retriaval agent → extraction agent → leader agent validation  → finally answer",
            "2. Market Entry:",
            "   - Combine Project agent and Relationships insights",
            "3. Strategic Planning:",
            "   - Gather input from all team members",
            "   - Prioritize based on market opportunity and resources",
            "按顺序执行，不要跳过任何步骤，最后由你确认并返回结果",
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
        show_members_responses=False,
    )
