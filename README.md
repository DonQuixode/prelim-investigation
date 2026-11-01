# prelim-investigation

Preliminary investigation of LangChain chains and LLM setups.

## Setup

```sh
uv sync
cp .env.example .env    # add your API keys to .env
uv run jupyter lab
```

Open `rag_chains.ipynb`. Section 0 holds every model, key and URL. Section 1
holds the simple blog chain and section 2 the styled chain.

## App

```sh
uv run streamlit run app.py
```

The app has one shared Points box and two flows: Simple (points only) and
Complex (points + prose examples + humanizing rules). Each flow writes to a
bounded output box.

## Layout

| Path | Content |
|---|---|
| `app.py` | Streamlit UI. One Points box, two flows, two output boxes. |
| `blog_chains.py` | Model, prompts, and chains used by the app. |
| `rag_chains.ipynb` | The notebook. Section 0 is the LLM setup; sections 1 and 2 are the chains. |
| `.env` | Your API keys. Not committed. |
| `pyproject.toml` | LangChain and Streamlit dependencies. |
