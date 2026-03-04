import re
from pathlib import Path

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.config import GROQ_API_KEY

_PROMPT_PATH = Path(__file__).parent.parent / "prompts" / "sql_prompt.txt"
_PROMPT_TEMPLATE = _PROMPT_PATH.read_text(encoding="utf-8")

_prompt = PromptTemplate(input_variables=["question"], template=_PROMPT_TEMPLATE)

_llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=GROQ_API_KEY
)

_chain = _prompt | _llm | StrOutputParser()


def _clean_sql(raw: str) -> str:
    raw = re.sub(r"```(?:sql)?", "", raw, flags=re.IGNORECASE)
    raw = raw.replace("```", "")
    return raw.strip().rstrip(";") + ";"


def natural_language_to_sql(question: str) -> str:
    """Convert a natural-language question to a SQL SELECT statement."""
    return _clean_sql(_chain.invoke({"question": question}))