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
    st.components.v1.html("""
        <div id="google_translate_element"></div>
        <script type="text/javascript">
            function googleTranslateElementInit() {
                new google.translate.TranslateElement({
                    pageLanguage: 'en',
                    includedLanguages: 'ar,en,fr,es',
                    layout: google.translate.TranslateElement.InlineLayout.SIMPLE
                }, 'google_translate_element');
            }
        </script>
        <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
    """, height=50)
