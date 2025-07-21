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

temp_dir = tempfile.mkdtemp()

# Create CSV knowledge base - 使用相对路径
csv_kb = CSVKnowledgeBase(
    path=current_dir,  # 使用当前文件所在目录
    vector_db=LanceDb(
        table_name="projects_csv_knowledge",
        uri=temp_dir,
    ),
)


# Combine knowledge bases
project_knowledge_base = CombinedKnowledgeBase(
    sources=[
        csv_kb,
    ],
    vector_db=LanceDb(
        table_name="projects_csv_knowledges",
        uri=temp_dir,
    ),
)

# 加载CSV文件到知识库
csv_kb.load(recreate=True)
project_knowledge_base.load(recreate=True)
