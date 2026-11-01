# prelim-investigation

Preliminary investigation of LangChain chains and LLM setups.

## Setup

```sh
uv sync
cp .env.example .env    # add your API keys to .env
uv run jupyter lab
```

Open `rag_chains.ipynb`. Section 0 holds every model, key and URL. Section 1
holds the simple blog chain.

## Layout

| Path | Content |
|---|---|
| `rag_chains.ipynb` | The notebook. Section 0 is the LLM setup; section 1 is the simple blog chain. |
| `.env` | Your API keys. Not committed. |
| `pyproject.toml` | LangChain dependencies. |
