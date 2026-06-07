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

# استبدل كود المترجم السابق بهذا الكود فقط
with col2:
    st.markdown("""
        <div id="google_translate_element"></div>
        <script>
            function googleTranslateElementInit() {
                new google.translate.TranslateElement({
                    pageLanguage: 'en',
                    layout: google.translate.TranslateElement.InlineLayout.VERTICAL
                }, 'google_translate_element');
            }
        </script>
        <script src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
        <style>
            #google_translate_element { position: absolute; right: 10px; top: 10px; }
            .goog-te-gadget-simple { background-color: transparent !important; border: none !important; }
            .goog-te-gadget-simple span { color: #00f2ff !important; }
        </style>
    """, unsafe_allow_html=True)
