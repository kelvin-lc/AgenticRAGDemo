import os
from pathlib import Path

from agno.knowledge.combined import CombinedKnowledgeBase
from agno.knowledge.csv import CSVKnowledgeBase
from agno.vectordb.pgvector import PgVector
from agno.vectordb.lancedb import LanceDb
import tempfile

# db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
from src.config import settings

# 获取当前文件所在目录的绝对路径
current_dir = Path(__file__).parent.absolute()

# 指定具体的CSV文件路径
csv_file_path = current_dir / "relationships_data.csv"

temp_dir = tempfile.mkdtemp()

# Create CSV knowledge base - 使用具体的CSV文件
csv_kb = CSVKnowledgeBase(
    path=csv_file_path,  # 使用具体的CSV文件路径
    vector_db=LanceDb(
        table_name="relationships_csv_knowledge",
        uri=temp_dir,
    ),
)

# Combine knowledge bases
relationships_knowledge_base = CombinedKnowledgeBase(
    sources=[
        csv_kb,
    ],
    vector_db=LanceDb(
        table_name="relationships_csv_knowledges",
        uri=temp_dir,
    ),
)

# 加载CSV文件到知识库
csv_kb.load(recreate=True)
relationships_knowledge_base.load(recreate=True)

# Initialize the Agent with the combined knowledge base
# agent = Agent(
#     knowledge=knowledge_base,
#     search_knowledge=True,
# )

# knowledge_base.load(recreate=False)

# # Use the agent
# agent.print_response("Ask me about something from the knowledge base", markdown=True)
