from pathlib import Path

from agno.knowledge.combined import CombinedKnowledgeBase
from agno.knowledge.csv import CSVKnowledgeBase
from agno.vectordb.pgvector import PgVector

# db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
from src.config import settings

# Create CSV knowledge base
csv_kb = CSVKnowledgeBase(
    path=Path("data/csvs"),
    # vector_db=PgVector(
    #     table_name="csv_documents",
    #     db_url=settings.DATABASE_URI,
    # ),
)


# Combine knowledge bases
project_knowledge_base = CombinedKnowledgeBase(
    sources=[
        csv_kb,
    ],
    # vector_db=PgVector(
    #     table_name="combined_documents",
    #     db_url=settings.DATABASE_URI,
    # ),
)
