import streamlit as st
from agent import run_research_agent # Import our main function

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🧠",
    layout="wide"
)

# --- Fully Themed Custom CSS (Sidebar styles removed) ---
st.markdown("""
<style>
/* Base Theme */
html, body, [class*="st-"], [class*="css-"] {
    background-color: #260000; /* Dark maroon for the entire page */
    color: #fafafa;
    font-family: 'sans serif';
}

/* Button Styling */
.stButton>button {
    background-color: #8B0000;
    color: #ffffff;
    border-radius: 8px;
    border: 1px solid #a52a2a;
    padding: 10px 16px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,0.2);
    width: 100%; /* Make button fill its column */
}
.stButton>button:hover {
    background-color: #a52a2a;
    border-color: #c04040;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.3);
}
.stButton>button:active {
    background-color: #6e0000;
}

/* Title and Headers */
h1, h2 {
    color: #ffcccc; /* Light red for main titles */
    border-bottom: 2px solid #4d0000;
    padding-bottom: 5px;
}
h3, h4, h5, h6 {
    color: #e0e0e0;
}

/* Input Box */
[data-testid="stTextInput"] label {
    color: #ffcccc;
}
[data-testid="stTextInput"] > div > div > input {
    background-color: #330000;
    border-radius: 8px;
    border: 1px solid #4d0000;
    color: #fafafa;
}

/* Align button vertically with the text input */
[data-testid="stVerticalBlock"] {
    align-items: end;
}

/* Alert Boxes */
[data-testid="stAlert"] {
    background-color: #330000;
    border-radius: 8px;
    border-left: 5px solid;
}
[data-testid="stAlert"][data-testid="stAlert-info"] { border-left-color: #a52a2a; }
[data-testid="stAlert"][data-testid="stAlert-warning"] { border-left-color: #ff7f7f; }
[data-testid="stAlert"][data-testid="stAlert-error"] { border-left-color: #ff4d4d; }

/* Links */
a:link, a:visited {
  color: #ff9999; /* Light red for links */
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
  color: #ffcccc;
}

/* Spinner */
.stSpinner > div > div {
    border-top-color: #8B0000;
}

/* Hide Streamlit Header/Footer */
header {visibility: hidden;}
footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)


# --- Main Content ---
st.title("AI Research Agent")
st.markdown("##### Your intelligent assistant for gathering, summarizing, and synthesizing information.")

# --- Input Controls ---
col1, col2 = st.columns([4, 1]) # Create two columns for input and button

with col1:
    query = st.text_input(
        "Enter your research topic:", 
        placeholder="e.g., The future of renewable energy",
        label_visibility="collapsed" # Hides the label as it's redundant
    )

with col2:
    if st.button("Start Research"):
        if not query:
            st.warning("Please enter a topic to research.")
        else:
            # Store the query in session state to be used by the main panel
            st.session_state.query = query
            st.session_state.report = None # Clear previous report
            st.session_state.submitted = True

st.markdown("---")


# Display report if it has been generated
if 'submitted' in st.session_state and st.session_state.submitted:
    with st.spinner("The agent is at work... Searching, scraping, and summarizing..."):
        try:
            # Run the agent only once and store the report in session state
            if st.session_state.report is None:
                st.session_state.report = run_research_agent(st.session_state.query)
            
            # Display the report from session state
            st.markdown(st.session_state.report)

        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("Enter a topic above and click 'Start Research' to begin.")