import streamlit as st
from datetime import datetime

# =========================
# SITE CONFIG
# =========================
st.set_page_config(page_title="Articla — IGN-Inspired Blog", layout="wide")

# =========================
# DESIGN SYSTEM
# =========================
PRIMARY = "#EF4444"      # Red (IGN-inspired)
SECONDARY = "#F59E0B"    # Amber accent
SUCCESS = "#10B981"      # Emerald
ERROR = "#DC2626"        # Red
NEUTRAL_BG = "#F9FAFB"   # Light gray background
TEXT_COLOR = "#111827"   # Near-black
CAPTION_COLOR = "#6B7280" # Gray text

# =========================
# GLOBAL STYLE (CSS)
# =========================
st.markdown(f"""
    <style>
    body {{
        background-color: {NEUTRAL_BG};
        color: {TEXT_COLOR};
        font-family: 'Inter', sans-serif;
    }}
    h1, h2, h3 {{
        font-weight: 700;
        color: {TEXT_COLOR};
    }}
    h1 {{ font-size: 36px; }}
    h2 {{ font-size: 24px; margin-top: 32px; }}
    h3 {{ font-size: 20px; margin-bottom: 8px; }}
    p, li, label {{
        font-size: 16px;
        line-height: 1.6;
    }}
    .featured {{
        background-color: white;
        border-radius: 24px;
        padding: 32px;
        margin-bottom: 32px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }}
    .article-card {{
        background-color: white;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        transition: 0.2s;
    }}
    .article-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }}
    .stButton>button {{
        background-color: {PRIMARY};
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 18px;
        font-weight: 600;
        transition: 0.2s;
    }}
    .stButton>button:hover {{
        background-color: {SECONDARY};
        transform: scale(1.02);
    }}
    .meta {{
        font-size: 14px;
        color: {CAPTION_COLOR};
        margin-bottom: 12px;
    }}
    .thumbnail {{
        border-radius: 12px;
        width: 100%;
        height: 180px;
        object-fit: cover;
        margin-bottom: 12px;
    }}
    </style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.title("🎮 Articla — IGN-Inspired Blog")
st.caption("Share your latest thoughts, stories, and reviews.")

# =========================
# ARTICLE FORM
# =========================
st.subheader("📝 Share a New Article")
with st.form("article_form", clear_on_submit=True):
    title = st.text_input("Title", placeholder="Enter an engaging title...")
    author = st.text_input("Author", placeholder="Your name")
    image_url = st.text_input("Thumbnail Image URL (optional)", placeholder="Paste image URL...")
    content = st.text_area("Article Content", placeholder="Write your story...", height=200)
    submitted = st.form_submit_button("Publish Article")

    if submitted:
        if title and author and content:
            if "articles" not in st.session_state:
                st.session_state.articles = []
            st.session_state.articles.append({
                "title": title,
                "author": author,
                "content": content,
                "image": image_url,
                "date": datetime.now().strftime("%b %d, %Y")
            })
            st.success("✅ Article published!")
        else:
            st.error("⚠️ Please fill in all required fields.")

# =========================
# DISPLAY ARTICLES
# =========================
if "articles" not in st.session_state or len(st.session_state.articles) == 0:
    st.info("No articles yet. Be the first to publish!")
else:
    articles = st.session_state.articles
    featured = articles[-1]

    # Featured Article
    st.markdown("<h2>🌟 Featured Article</h2>", unsafe_allow_html=True)
    with st.container():
        st.markdown(f"""
            <div class="featured">
                {'<img src="' + featured['image'] + '" class="thumbnail">' if featured['image'] else ''}
                <h2>{featured['title']}</h2>
                <div class="meta">By {featured['author']} — {featured['date']}</div>
                <p>{featured['content']}</p>
            </div>
        """, unsafe_allow_html=True)

    # Other Articles (Grid Layout)
    st.markdown("<h2>📰 More Articles</h2>", unsafe_allow_html=True)
    cols = st.columns(2)
    for i, article in enumerate(reversed(articles[:-1])):
        col = cols[i % 2]
        with col:
            st.markdown(f"""
                <div class="article-card">
                    {'<img src="' + article['image'] + '" class="thumbnail">' if article['image'] else ''}
                    <h3>{article['title']}</h3>
                    <div class="meta">By {article['author']} — {article['date']}</div>
                    <p>{article['content'][:200]}...</p>
                </div>
            """, unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("© 2025 Articla | Inspired by IGN | Built with ❤️ using Streamlit")
