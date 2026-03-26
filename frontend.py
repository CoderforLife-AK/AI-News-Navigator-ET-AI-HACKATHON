import streamlit as st
import requests
from streamlit_option_menu import option_menu

API_URL = "http://127.0.0.1:8000"

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI News Navigator",
    page_icon="🧠",
    layout="wide"
)

# ---------- CUSTOM CSS (PREMIUM LOOK) ----------
st.markdown("""
<style>

body {
    background-color: #0e1117;
}

.main {
    background-color: #0e1117;
}

h1, h2, h3 {
    color: white;
}

.news-card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
}

.ai-box {
    background: linear-gradient(135deg,#1f2937,#111827);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:

    st.title("🧠 AI News")

    selected = option_menu(
        "Navigation",
        ["News Feed", "AI Assistant"],
        icons=["newspaper", "robot"],
        default_index=0,
    )

    topic = st.selectbox(
        "Choose Interest",
        ["technology", "startup", "stocks", "economy"]
    )

# ---------- HEADER ----------
st.title("🧠 AI News Navigator")
st.caption("Your Personalized AI Intelligence Briefing")

# ==================================================
# NEWS FEED PAGE
# ==================================================

if selected == "News Feed":

    st.header("📰 Personalized News")

    if st.button("✨ Generate My News Briefing"):

        response = requests.get(f"{API_URL}/news/{topic}")
        data = response.json()

        for article in data["personalized_news"]:

            st.markdown(f"""
            <div class="news-card">
                <h3>{article['title']}</h3>
                <p>{article['summary']}</p>
                <a href="{article['url']}" target="_blank">
                    Read Full Article →
                </a>
            </div>
            """, unsafe_allow_html=True)

# ==================================================
# AI ASSISTANT PAGE
# ==================================================

if selected == "AI Assistant":

    st.header("🤖 Ask AI About Today's News")

    question = st.text_input(
        "Ask anything about current news"
    )

    if st.button("Ask AI") and question:

        params = {
            "question": question,
            "topic": topic
        }

        response = requests.get(f"{API_URL}/ask", params=params)
        answer = response.json()

        st.markdown(f"""
        <div class="ai-box">
            <h4>AI Insight</h4>
            <p>{answer['answer']}</p>
        </div>
        """, unsafe_allow_html=True)