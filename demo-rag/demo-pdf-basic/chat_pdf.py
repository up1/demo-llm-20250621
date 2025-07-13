from agno.agent import Agent
from agno.document.chunking.agentic import AgenticChunking
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.chroma import ChromaDb

knowledge_base = PDFKnowledgeBase(
    path="./data/microsoft_annual_report_2022.pdf",
    vector_db=ChromaDb(collection="reports", persistent_client=True),
    chunking_strategy=AgenticChunking(),
)
# knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)

agent.print_response("What was the total revenue of 2022, 2021 and 2020?", markdown=True)