import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Kleos — Hiring a contractor in Belarus",
    page_icon="🇧🇾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide default Streamlit chrome so the page renders full-bleed
st.markdown("""
<style>
  #MainMenu, header, footer {visibility: hidden;}
  .block-container {padding: 0 !important; max-width: 100% !important;}
  [data-testid="stAppViewContainer"] > .main {padding: 0 !important;}
  [data-testid="stHeader"] {display: none;}
</style>
""", unsafe_allow_html=True)

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")

# Height must comfortably exceed the tallest rendered state (all sections
# expanded). The page is English-only and the sanctions block is a compact note,
# so it's a touch shorter than the checklist-based pages in the series.
components.html(html, height=6200, scrolling=True)
