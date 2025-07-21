from typing import Any

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from src.api.errors import InternalError
from src.schemas.agent import AgentRequest
from src.teams.leader import get_agentic_rag_team
from src.utils.common_utils import chat_response_streamer

router = APIRouter()


@router.post(
    "/completions",
)
async def run_agent(
    request: AgentRequest,
) -> Any:
    """
    Run an agent
    """
    try:
        agentic_rag_team = get_agentic_rag_team(
            user_id=request.user_id,
            session_id=request.session_id,
        )
    except Exception as e:
        raise InternalError(detail=str(e))

    if request.stream:
        return StreamingResponse(
            chat_response_streamer(agentic_rag_team, request.message),
            media_type="text/event-stream",
        )
    else:
        response = await agentic_rag_team.arun(request.message, stream=False)
        return response.content
