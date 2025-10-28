import streamlit as st
from datetime import datetime

# =========================
# DESIGN SYSTEM
# =========================
st.set_page_config(page_title="Articla — Share Ideas", layout="wide")

# Color Palette
PRIMARY = "#4F46E5"   # Indigo
SECONDARY = "#06B6D4" # Cyan
SUCCESS = "#16A34A"   # Green
ERROR = "#DC2626"     # Red
NEUTRAL_BG = "#F9FAFB" # Light gray
TEXT_COLOR = "#111827"

# Typography
st.markdown("""
    <style>
    body {
        background-color: %s;
        color: %s;
        font-family: 'Inter', sans-serif;
    }
    h1, h2, h3, h4 {
        font-weight: 700;
        color: %s;
    }
    p, li, label {
        font-size: 16px;
        color: %s;
    }
    .article-card {
        background-color: white;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 16px;
    }
    .stButton>button {
        background-color: %s;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: 600;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background-color: %s;
        color: white;
        transform: scale(1.02);
    }
    </style>
""" % (NEUTRAL_BG, TEXT_COLOR, TEXT_COLOR, TEXT_COLOR, PRIMARY, SECONDARY),
unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.title("📝 Articla — Share and Explore Ideas")

st.markdown("Welcome to **Articla**, a minimal article-sharing platform built with Streamlit.")

# =========================
# ARTICLE SUBMISSION FORM
# =========================
st.subheader("✍️ Share a New Article")
with st.form("article_form", clear_on_submit=True):
    title = st.text_input("Article Title", placeholder="Enter a catchy title...")
    author = st.text_input("Your Name", placeholder="John Doe")
    content = st.text_area("Content", placeholder="Write your article here...", height=200)
    submitted = st.form_submit_button("Publish Article")

    if submitted:
        if title and author and content:
            if "articles" not in st.session_state:
                st.session_state.articles = []
            st.session_state.articles.append({
                "title": title,
                "author": author,
                "content": content,
                "date": datetime.now().strftime("%b %d, %Y")
            })
            st.success("✅ Article published successfully!")
        else:
            st.error("⚠️ Please fill all fields before publishing.")

# =========================
# DISPLAY ARTICLES
# =========================
st.subheader("📚 Recent Articles")

if "articles" in st.session_state and len(st.session_state.articles) > 0:
    for article in reversed(st.session_state.articles):
        with st.container():
            st.markdown(f"""
                <div class="article-card">
                    <h3>{article['title']}</h3>
                    <p><em>By {article['author']} — {article['date']}</em></p>
                    <p>{article['content']}</p>
                </div>
            """, unsafe_allow_html=True)
else:
    st.info("No articles yet. Be the first to share something!")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("© 2025 Articla | Built with ❤️ using Streamlit")
