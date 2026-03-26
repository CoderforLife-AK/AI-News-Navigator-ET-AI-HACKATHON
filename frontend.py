import streamlit as st
import requests
from streamlit_option_menu import option_menu

API_URL = "https://ai-news-navigator-et-ai-hackathon.onrender.com"

# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="AI News Navigator",
    page_icon="🧠",
    layout="wide"
)


# ==============================
# PREMIUM CSS
# ==============================

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

/* Title Gradient */
.big-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    background: linear-gradient(90deg,#38bdf8,#a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Glass Card */
.glass {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(12px);
    margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* Buttons */
.stButton>button {
    border-radius: 10px;
    background: linear-gradient(90deg,#6366f1,#8b5cf6);
    color: white;
    border: none;
    padding: 10px 18px;
}

</style>
""", unsafe_allow_html=True)


# ==============================
# HEADER
# ==============================

st.markdown('<p class="big-title">🧠 AI News Navigator</p>', unsafe_allow_html=True)
st.caption("🚀 AI-Powered Personalized News Experience")


# ==============================
# SIDEBAR MENU
# ==============================

with st.sidebar:
    selected = option_menu(
        "Navigation",
        ["Personalized News", "Ask AI"],
        icons=["newspaper", "chat-dots"],
        default_index=0,
    )


# ==============================
# NEWS SECTION
# ==============================

if selected == "Personalized News":

    st.header("📰 Personalized News")

    interest = st.text_input("Enter your interest", "technology")

    if st.button("Get News"):

        with st.spinner("🧠 AI is analyzing news..."):

            try:
                response = response = requests.get(
                    f"{API_URL}/news/{interest}",
                    timeout=60
                )
                data = response.json()

                for article in data["results"]:
                    st.markdown(f"""
                    <div class="glass">
                        <h4>{article["title"]}</h4>
                        <p>{article["summary"]}</p>
                    </div>
                    """, unsafe_allow_html=True)

            except:
                st.error("⚠️ Backend not reachable. Check API URL.")


# ==============================
# AI CHAT SECTION
# ==============================

if selected == "Ask AI":

    st.header("💬 Ask AI About News")

    query = st.text_input("Ask anything about news")

    if st.button("Ask AI"):

        with st.spinner("🤖 Thinking..."):

            try:
                response = response = requests.get(
                    f"{API_URL}/news/{interest}",
                    timeout=60
                )
                answer = response.json()["response"]

                st.markdown(f"""
                <div class="glass">
                    🤖 {answer}
                </div>
                """, unsafe_allow_html=True)

            except:
                st.error("⚠️ Could not connect to AI service.")
