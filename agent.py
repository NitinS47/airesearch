import os
from dotenv import load_dotenv
from ddgs import DDGS  # <-- CORRECTED IMPORT
from newspaper import Article, Config
import google.generativeai as genai

# Load environment variables
load_dotenv()

def search_web(query: str, num_results: int = 5) -> list[dict]:
    """Performs a web search using DuckDuckGo and returns results."""
    print(f"-> Searching the web for: '{query}'...")
    with DDGS() as ddgs:
        # The generator ddgs.text() returns dictionaries
        results = [r for r in ddgs.text(query, max_results=num_results)]
    # We only need the title and href (URL)
    return [{"title": r['title'], "url": r['href']} for r in results]

def extract_content(url: str) -> dict | None:
    """Extracts the title and text content from a given URL."""
    try:
        print(f"-> Scraping content from: {url}")
        
        # Create a configuration object and disable SSL verification
        config = Config()
        config.verify_ssl = False
        
        # Pass the config to the Article
        article = Article(url, config=config)
        
        article.download()
        article.parse()
        return {
            "url": url,
            "text": article.text,
        }
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Configure the Gemini API
genai.configure(api_key=os.getenv("AIzaSyAbJBSlHpQKKDp8O-riDZ4p46FRGZ20C5w"))

def summarize_and_analyze(query: str, content_list: list[dict]) -> str:
    """Summarizes and analyzes the collected content using the Gemini API."""
    print("-> Summarizing and analyzing content with Gemini...")
    
    # Combine all the text into one large string
    full_text = ""
    for content in content_list:
        full_text += f"Source URL: {content['url']}\n"
        full_text += f"Content:\n{content['text']}\n\n---\n\n"

    # Set up the model
    generation_config = {
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    model = genai.GenerativeModel(model_name="gemini-2.0-flash", generation_config=generation_config)

    prompt = f"""
    You are an expert AI research assistant. Your task is to synthesize information from the provided web content to answer the user's query.
    
    User Query: "{query}"

    Provided Content:
    {full_text}

    Instructions:
    1. Generate a comprehensive summary that directly answers the user's query. Give the summary in with gaps identified in the research. debates, and consensus if applicable.
    2. Organize the summary into clear, easy-to-read sections or bullet points in Markdown format.
    3. For each key point, you MUST cite the source URL it came from. E.g., (Source: https://example.com).
    4. Do not include information that is not present in the provided content.
    5. Conclude with a "Sources" section listing all URLs used.
    """
    
    response = model.generate_content(prompt)
    return response.text

def run_research_agent(query: str):
    """The main function to orchestrate the research agent."""
    search_results = search_web(query)
    if not search_results:
        return "Could not find any relevant URLs. Please try a different query."

    all_content = []
    for result in search_results:
        content = extract_content(result['url'])
        if content and content['text']:
            all_content.append(content)
            
    if not all_content:
        return "Could not extract content from the found URLs."

    final_report = summarize_and_analyze(query, all_content)
    return final_report

# To test the backend directly from the command line
if __name__ == '__main__':
    user_query = "What are the latest breakthroughs in Alzheimer's research (2024–2025)?"
    report = run_research_agent(user_query)
    print("\n--- FINAL REPORT ---")

    print(report)
