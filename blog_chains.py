"""Model, prompts, and chains for the blog app.

The prompts match section 1 and section 2 of `rag_chains.ipynb`.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")


def _env(name, default=None):
    value = os.environ.get(name, default)
    if not value:
        raise KeyError(f"{name} is not set: add it to {ROOT / '.env'}")
    return value


def final_answer(text: str) -> str:
    """Keep the published text. Some providers put the model's reasoning in
    `content`, before a literal </think> marker; take only what follows it."""
    return text.rsplit("</think>", 1)[-1].strip()


SIMPLE_PROMPT = (
    "Write a 50 word blog for publishing with the following points: {points}"
)

STYLED_PROMPT = (
    "Write a 50 word blog for publishing. First, make rules based on how this "
    "example is written: {examples}, then, use those rules alongside these "
    "humanizing rules to avoid LLM smells: {humanizing_rules}, and then write on "
    "the topic(s) provided in these points. Do not add features which aren't "
    "present: {points}"
)

DEFAULT_HUMANIZING_RULES = """don't use the following: “it’s not X, it’s Y” framings, rule-of-three lists, em-dash overuse, “delve/tapestry/landscape,” tidy summary endings, throat-clearing openers"""

DEFAULT_EXAMPLES = """Two things get in the way of clear Founder identity and narrative:

1. The Fog of War: The first challenge is internal. Your story is still evolving, and you're too deep in the daily chaos to see its shape. You know something profound is happening in your company, but articulating it feels like trying to describe water while swimming. Besides, when the codebase has collapsed in a heap of on-call issues, identity and narrative are the last thing on your mind. You tell yourself you'll figure it out next week. Or the week after. You promise.

2. The Content-First Trap: The second challenge is external. Too many agencies and social media experts jump straight to content without getting context. They ask "What should we post?" before understanding why you're posting in the first place. They can tell you everything about your market position, but nothing about your authentic voice. You want to talk about your tech stack. They want you to pick a fight with Elon. End result? You sound like every other founder on LinkedIn."""


def build_chains(llm=None):
    """Build the two blog chains. Pass `llm` to use a test model."""
    if llm is None:
        llm = ChatOpenAI(model_name=_env("LLM_MODEL", "glm-5.3"),
                         base_url=_env("LLM_BASE_URL", "https://opencode.ai/zen/v1"),
                         api_key=_env("LLM_API_KEY"),
                         temperature=0.7,
                         use_responses_api=False)

    simple = (
        ChatPromptTemplate.from_messages([("system", SIMPLE_PROMPT)])
        | llm
        | StrOutputParser()
        | final_answer
    )
    styled = (
        ChatPromptTemplate.from_messages([("system", STYLED_PROMPT)])
        | llm
        | StrOutputParser()
        | final_answer
    )
    return simple, styled
