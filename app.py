import streamlit as st
import feedparser

st.set_page_config(
    page_title="My News" ,
    page_icon="🎃",
    layout="wide"
)
st.write("最新バージョン確認")

st.markdown("""
<style>

.stApp {
    background: red !important;
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
        <a href="{article.link}" target="_blank" class="news-button">
        記事を見る →
        </a>

        </div>

        """, unsafe_allow_html=True)

