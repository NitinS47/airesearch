import streamlit as st
from agent import run_research_agent # Import our main function

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🧠",
    layout="wide"
)

# --- Custom CSS for Lavender/Purple Theme ---
st.markdown("""
<style>
/* Base Theme: Dark Purple/Lavender background, with white/light text */
html, body, [class*="st-"], [class*="css-"] {
    background-color: #1a0226; /* Deep dark purple */
    color: #e0e0f0; /* Soft white/lavender for main text */
    font-family: 'Segoe UI', 'Roboto', sans-serif; /* Professional font */
}

/* Button Styling */
.stButton>button {
    background-color: #6a05ad; /* Medium purple */
    color: #ffffff;
    border-radius: 12px; /* Slightly more rounded */
    border: none;
    padding: 12px 20px;
    font-size: 1.1em;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3); /* Softer, larger shadow */
    width: 100%; /* Make button fill its column */
    cursor: pointer;
}
.stButton>button:hover {
    background-color: #8a2be2; /* Brighter lavender on hover */
    box-shadow: 0 6px 15px rgba(0,0,0,0.4);
    transform: translateY(-2px); /* Slight lift effect */
}
.stButton>button:active {
    background-color: #5d00a0; /* Darker purple on click */
    transform: translateY(0);
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

/* Title and Headers */
h1 {
    color: #e0e0f0; /* Soft white for main titles */
    font-weight: 700;
    font-size: 2.8em;
    padding-bottom: 10px;
    border-bottom: 3px solid #6a05ad; /* Purple underline */
    margin-bottom: 25px;
}
h2, h3, h4, h5, h6 {
    color: #c9a0dc; /* Lighter lavender for sub-headers */
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 10px;
}
p {
    line-height: 1.7; /* Improve readability */
}

/* Input Box */
[data-testid="stTextInput"] label {
    color: #c9a0dc; /* Lavender for input labels */
    font-size: 1.1em;
    font-weight: 500;
}
[data-testid="stTextInput"] > div > div > input {
    background-color: #2a033d; /* Slightly lighter dark purple */
    border-radius: 12px;
    border: 1px solid #4a046f; /* Medium purple border */
    color: #e0e0f0;
    padding: 10px 15px;
    font-size: 1.05em;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
}
[data-testid="stTextInput"] > div > div > input:focus {
    border-color: #8a2be2; /* Brighter lavender on focus */
    box-shadow: 0 0 0 0.2rem rgba(138, 43, 226, 0.25);
    outline: none;
}


/* Align button vertically with the text input */
[data-testid="stVerticalBlock"] {
    align-items: end;
}

/* Alert Boxes (Info, Warning, Error) */
[data-testid="stAlert"] {
    background-color: #2a033d; /* Dark purple background for alerts */
    border-radius: 10px;
    padding: 15px 20px;
    border-left: 5px solid;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    margin-bottom: 15px;
}
[data-testid="stAlert"][data-testid="stAlert-info"] {
    border-left-color: #6a05ad; /* Medium purple for info */
    color: #e0e0f0;
}
[data-testid="stAlert"][data-testid="stAlert-warning"] {
    border-left-color: #e0b0ff; /* Light lavender for warning */
    color: #ffffff;
}
[data-testid="stAlert"][data-testid="stAlert-error"] {
    border-left-color: #d896ff; /* Slightly brighter purple for error */
    color: #ffffff;
}

/* Links */
a:link, a:visited {
  color: #b091e0; /* Muted lavender for links */
  text-decoration: none;
  font-weight: 500;
}
a:hover {
  text-decoration: underline;
  color: #e0b0ff; /* Lighter lavender on hover */
}

/* Spinner */
.stSpinner > div > div {
    border-top-color: #6a05ad; /* Purple spinner */
    border-bottom-color: transparent;
}

/* Markdown elements (for the report) */
.stMarkdown {
    background-color: #2a033d; /* Slightly lighter dark purple for report background */
    padding: 25px 35px;
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.4);
    margin-top: 30px;
}
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
    color: #e0b0ff; /* Lighter purple for report headings */
    border-bottom-color: #4a046f; /* Matching border for headings */
}
.stMarkdown strong {
    color: #e0b0ff; /* Emphasize bold text with lavender */
}

/* Horizontal Rule */
hr {
    border-top: 2px solid #4a046f;
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
col1, col2 = st.columns([4, 1]) # Create two columns for input and button

with col1:
    query = st.text_input(
        "Enter your research topic:", 
        placeholder="e.g., The future of AI ethics",
        label_visibility="collapsed" # Hides the label as it's redundant
    )

with col2:
    # Use a unique key for the button to prevent potential issues when re-running
    if st.button("Start Research", key="start_research_button"):
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
    st.info("Enter a topic above and click 'Start Research' to begin. For example, 'Impact of AI on the job market.'")
