import streamlit as st
from agent import run_research_agent # Import our main function

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🧠",
    layout="wide"
)

# --- Custom CSS for Professional Purple/White Theme ---
st.markdown("""
<style>
/* Base Theme: Light background with purple text */
html, body, [class*="st-"], [class*="css-"] {
    background-color: #F8F7FF; /* Very light lavender-white */
    color: #3D2C56; /* Dark purple for main text */
    font-family: 'Segoe UI', 'Roboto', sans-serif;
}

/* Button Styling */
.stButton>button {
    background-color: #6a05ad; /* Strong purple */
    color: #ffffff;
    border-radius: 10px;
    border: none;
    padding: 12px 20px;
    font-size: 1.05em;
    font-weight: 500;
    transition: all 0.3s ease;
    box-shadow: 0 4px 14px 0 rgba(106, 5, 173, 0.25); /* Subtle purple shadow */
    width: 100%;
    cursor: pointer;
}
.stButton>button:hover {
    background-color: #8a2be2; /* Brighter purple on hover */
    box-shadow: 0 6px 20px 0 rgba(106, 5, 173, 0.3);
    transform: translateY(-2px);
}
.stButton>button:active {
    background-color: #5d00a0; /* Darker on click */
    transform: translateY(0);
}

/* Title and Headers */
h1 {
    color: #4B0082; /* Indigo for main title */
    font-weight: 700;
    padding-bottom: 10px;
}
h2, h3, h4, h5, h6 {
    color: #5D3FD3; /* Medium purple for sub-headers */
    font-weight: 600;
}
p {
    line-height: 1.6;
}

/* Input Box */
[data-testid="stTextInput"] > div > div > input {
    background-color: #FFFFFF;
    border-radius: 10px;
    border: 1px solid #D6BCF5; /* Light purple border */
    color: #3D2C56;
    padding: 10px 15px;
    box-shadow: inset 0 1px 2px rgba(0,0,0,0.05);
}
[data-testid="stTextInput"] > div > div > input:focus {
    border-color: #8a2be2;
    box-shadow: 0 0 0 0.2rem rgba(138, 43, 226, 0.2);
    outline: none;
}

/* Align button vertically with the text input */
[data-testid="stVerticalBlock"] {
    align-items: end;
}

/* Alert Boxes (Info, Warning, Error) */
[data-testid="stAlert"] {
    background-color: #E6E0FF; /* Very light purple background */
    border-radius: 10px;
    border-left: 5px solid;
    color: #3D2C56;
}
[data-testid="stAlert"][data-testid="stAlert-info"] { border-left-color: #6a05ad; }
[data-testid="stAlert"][data-testid="stAlert-warning"] { border-left-color: #DDA0DD; } /* Orchid for warning */
[data-testid="stAlert"][data-testid="stAlert-error"] { border-left-color: #C71585; } /* Medium Violet Red for error */

/* Links */
a:link, a:visited {
  color: #6a05ad;
  font-weight: 500;
}
a:hover {
  color: #8a2be2;
}

/* Spinner */
.stSpinner > div > div {
    border-top-color: #6a05ad;
}

/* Markdown Report Container */
.stMarkdown {
    background-color: #FFFFFF;
    padding: 25px 35px;
    border-radius: 15px;
    border: 1px solid #EAE6FF; /* Subtle lavender border */
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05);
    margin-top: 30px;
}

/* Horizontal Rule */
hr {
    border-top: 1px solid #D6BCF5;
    margin-top: 25px;
    margin-bottom: 25px;
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
st.markdown("<br>", unsafe_allow_html=True) # Add some space
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


# Display report if it has been generated
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
