import streamlit as st
import feedparser

st.set_page_config(
    page_title="My News" ,
    page_icon="🎃",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg, ##E6C1CE,#CEE6C1);
}

/* ガラス風カード */
.news-card{
    background: rgba(255,255,255,0.35);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
        
    border-radius:20px;
    padding:20px;
    margin-bottom:20px;
    border:1px solid rgba(255,255,255,0.4);
    box-shadow:0 8px 20px rgba(0,0,0,0.08);
}         

.news-button{
    display:inline-black;
    margin-top:15px;
    padding:10px 16px;
    background:#8CBF7F;
    corlor:white !important;
    text-decoration:none;
    border-radius:10px
    font-weight:bold;
}                                              

.news-button:hover{
    background:#6EA866;
}

</style>
""", unsafe_allow_html=True)

st.title("Today's AI News")
st.write("最新のAIニュースを自動取得しています")
url = "https://news.google.com/rss/search?q=AI&hl=ja&gl=JP&ceid=JP:ja"
feed = feedparser.parse(url)

col1, col2 = st.columns(2)

for i, article in enumerate(feed.entries[:10]):
    target = col1 if i % 2 == 0 else col2
    with target:
        st.markdown(f"""
        <div class="news-card">
        <h3>🤍 {article.title}</h3>
        <p>📅 {article.published}</p>
        <p>Google News</p>
        <a href="{article}" target="_blank" class="news-button">
        記事を見る →
        </a>

        </div>

        """, unsafe_allow_html=True)

