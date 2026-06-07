import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cipher Edge Network", page_icon="💎", layout="centered")

if 'theme' not in st.session_state:
    st.session_state.theme = 'Dark'

bg = "#ffffff" if st.session_state.theme == 'Light' else "#0b0f17"
txt = "#000000" if st.session_state.theme == 'Light' else "#ffffff"

col1, col2 = st.columns([1, 4])

with col1:
    if st.button("☀️/🌙", key="theme_toggle"):
        st.session_state.theme = 'Light' if st.session_state.theme == 'Dark' else 'Dark'
        st.rerun()

with col2:
    st.markdown('<div id="google_translate_element"></div><script type="text/javascript">function googleTranslateElementInit(){new google.translate.TranslateElement({pageLanguage: "en", layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, "google_translate_element");}</script><script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>', unsafe_allow_html=True)

st.markdown(f"""
<style>
.stApp {{ background-color: {bg} !important; }}
h1, h2, h3, h4, h5, h6, p, label, span, small, .stMarkdown p {{ color: {txt} !important; }}
</style>
""", unsafe_allow_html=True)
