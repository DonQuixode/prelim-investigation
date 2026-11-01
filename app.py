"""Small Streamlit UI: one set of points, two blog flows."""

import streamlit as st

from blog_chains import DEFAULT_EXAMPLES, DEFAULT_HUMANIZING_RULES, build_chains

st.set_page_config(page_title="Blog Lab", layout="wide")

st.title("Blog Lab")
st.caption("One set of points, two pipelines. Both write a 50 word blog.")


@st.cache_resource
def get_chains():
    return build_chains()


try:
    simple_blog_chain, styled_blog_chain = get_chains()
except KeyError as exc:
    st.error(f"Model setup failed: {exc}")
    st.stop()

POINTS_PLACEHOLDER = (
    "- BrewContent is a new product for the future of Content creation.\n"
    "- It has features for AI video, voice, image and text generation "
    "alongside automating the entire flow."
)

points = st.text_area(
    "Points (shared by both flows)",
    height=150,
    placeholder=POINTS_PLACEHOLDER,
)
st.caption("Both flows below use these points.")

left, right = st.columns(2, gap="large")

with left:
    st.subheader("Simple")
    st.caption("points → LLM")
    if st.button("Generate simple blog", type="primary", width="stretch",
                 disabled=not points.strip()):
        with st.spinner("Writing..."):
            try:
                st.session_state["simple_output"] = simple_blog_chain.invoke(
                    {"points": points}
                )
            except Exception as exc:
                st.session_state["simple_output"] = None
                st.error(f"Call failed: {exc}")

with right:
    st.subheader("Complex")
    st.caption("points + examples + rules → LLM")
    examples = st.text_area("Prose examples", value=DEFAULT_EXAMPLES,
                            height=220, key="examples")
    with st.expander("Humanizing rules"):
        rules = st.text_area("Rules", value=DEFAULT_HUMANIZING_RULES,
                             height=140, key="rules",
                             label_visibility="collapsed")
    if st.button("Generate styled blog", type="primary", width="stretch",
                 disabled=not (points.strip() and examples.strip())):
        with st.spinner("Writing..."):
            try:
                st.session_state["styled_output"] = styled_blog_chain.invoke({
                    "examples": examples,
                    "humanizing_rules": rules,
                    "points": points,
                })
            except Exception as exc:
                st.session_state["styled_output"] = None
                st.error(f"Call failed: {exc}")

st.divider()

out_left, out_right = st.columns(2, gap="large")

with out_left:
    st.caption("Simple output")
    with st.container(border=True, height=380):
        st.markdown(st.session_state.get("simple_output") or "_No output yet._")

with out_right:
    st.caption("Complex output")
    with st.container(border=True, height=380):
        st.markdown(st.session_state.get("styled_output") or "_No output yet._")
