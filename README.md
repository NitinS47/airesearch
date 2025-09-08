# AI Research Agent 🧠

The AI Research Agent is a powerful tool designed to automate the process of online research. It takes a user's query, scours the web for relevant articles, scrapes the essential content, and uses the Google Gemini API to generate a concise, structured summary with citations. The final report can also be downloaded as a PDF.

![AI Research Agent Demo](path/to/your/screenshot.png)
*Replace `path/to/your/screenshot.png` with a screenshot of your running application.*

---
## ✨ Features

* **🤖 Automated Research:** Enter any topic and let the agent find the most relevant articles from the web.
* **📄 AI-Powered Summaries:** Utilizes Google's Gemini API to generate high-quality, structured summaries from multiple sources.
* **🔗 Source Citation:** Automatically includes links to the original articles to ensure credibility and allow for deeper reading.
* **📥 PDF Export:** Download the complete, formatted research report as a PDF with a single click.
* **🌐 Simple Web Interface:** A clean and intuitive UI built with Streamlit, making it easy for anyone to use.

---
## 🛠️ Tech Stack

* **Backend:** Python
* **Frontend:** Streamlit
* **AI Model:** Google Gemini API
* **Web Search:** `ddgs` (DuckDuckGo Search)
* **Web Scraping:** `newspaper3k`
* **PDF Generation:** `fpdf2` & `markdown`
* **Dependencies:** `python-dotenv`, `lxml`, `beautifulsoup4`, `cssselect`

---
## 🚀 Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

* Python 3.9 or higher
* A Google Gemini API Key. You can get one from [Google AI Studio](https://aistudio.google.com/).

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/ai-research-agent.git](https://github.com/your-username/ai-research-agent.git)
    cd ai-research-agent
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a file named `.env` in the root of your project folder and add your Google Gemini API key to it:
    ```
    GOOGLE_API_KEY="your_google_api_key_here"
    ```

---
## 🖥️ Usage

To run the application, execute the following command in your terminal from the project's root directory:

```sh
streamlit run app.py
```
Your web browser will open with the application running.

---
## 📁 Folder Structure

Here is the folder structure of the project:

```
ai-research-agent/
├── venv/
├── .env
├── .gitignore
├── agent.py
├── app.py
└── requirements.txt
```
