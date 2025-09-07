import streamlit as st
from agent import run_research_agent  # Import our main function

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🧠",
    layout="wide"
)

# --- Main Content ---
st.title("AI Research Agent")
st.markdown("##### Your intelligent assistant for gathering, summarizing, and synthesizing information.")

# --- Input Controls ---
st.markdown("<br>", unsafe_allow_html=True)  # Small spacing
col1, col2 = st.columns([4, 1])

with col1:
    query = st.text_input(
        "Enter your research topic:",
        placeholder="e.g., The future of AI ethics",
        label_visibility="collapsed"
    )

with col2:
    if st.button("Start Research", key="start_research_button"):
        if not query:
            st.warning("Please enter a topic to research.")
        else:
            st.session_state.query = query
            st.session_state.report = None
            st.session_state.submitted = True

st.markdown("---")

# --- Display report if generated ---
if 'submitted' in st.session_state and st.session_state.submitted:
    with st.spinner("The agent is at work... Searching, scraping, and summarizing..."):
        try:
            if st.session_state.report is None:
                st.session_state.report = run_research_agent(st.session_state.query)

            st.markdown(st.session_state.report)

        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("Enter a topic above and click 'Start Research' to begin. For example, 'Impact of AI on the job market.'")
