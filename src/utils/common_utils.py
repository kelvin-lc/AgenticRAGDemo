import functools
import logging
import traceback
from typing import AsyncGenerator

from agno.agent import Agent

logger = logging.getLogger(__name__)


def catch_return_default(default=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                logger.warning(str(traceback.format_exc()))
                return default

        return wrapped_func

    return decorator


async def chat_response_streamer(agent: Agent, message: str) -> AsyncGenerator:
    """
    Stream agent responses chunk by chunk.

    Args:
        agent: The agent instance to interact with
        message: User message to process

    Yields:
        Text chunks from the agent response
    """
    run_response = await agent.arun(message, stream=True)
    async for chunk in run_response:
        yield chunk.to_json()
