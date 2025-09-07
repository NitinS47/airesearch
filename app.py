import streamlit as st
from agent import run_research_agent
from fpdf import FPDF, XPos, YPos
import markdown

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🧠",
    layout="wide"
)

# --- PDF Generation Function (Corrected) ---
def create_pdf_report(markdown_text, query):
    """Generates a PDF report from markdown text with a header and footer."""
    class PDF(FPDF):
        def header(self):
            self.set_font('Helvetica', 'B', 16)
            self.cell(0, 10, 'AI Research Agent Report', border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

        def footer(self):
            self.set_y(-15)
            self.set_font('Helvetica', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', border=0, align='C')

    pdf = PDF()
    pdf.add_page()
    
    pdf.set_font('Helvetica', 'B', 12)
    pdf.multi_cell(0, 10, f"Research Query: {query}")
    pdf.ln(5)
    
    # Convert markdown to HTML to preserve formatting
    html_content = markdown.markdown(markdown_text)
    
    # Write the HTML content to the PDF
    pdf.set_font('Helvetica', '', 11)
    pdf.write_html(html_content)
    
    # Return PDF as a 'bytes' object for Streamlit
    return bytes(pdf.output())

# --- Main Content ---
st.title("AI Research Agent")
st.markdown("##### Your intelligent assistant for gathering, summarizing, and synthesizing information.")

# --- Input Controls ---
st.markdown("---")
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
            
            st.markdown("---")
            
            pdf_data = create_pdf_report(st.session_state.report, st.session_state.query)
            
            safe_filename = "".join(c for c in st.session_state.query if c.isalnum() or c in (' ', '_')).rstrip()
            
            st.download_button(
                label="📄 Download as PDF",
                data=pdf_data,
                file_name=f"AI_Report_{safe_filename[:30]}.pdf",
                mime="application/pdf"
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("Enter a topic above and click 'Start Research' to begin. For example, 'Impact of AI on the job market.'")
