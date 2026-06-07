import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="Cipher Edge Network", page_icon="💎", layout="centered")

# نظام حفظ حالة الإضاءة
if 'theme' not in st.session_state: st.session_state.theme = 'Dark'
def toggle_theme(): st.session_state.theme = 'Light' if st.session_state.theme == 'Dark' else 'Dark'

bg_color = "#ffffff" if st.session_state.theme == 'Light' else "#0b0f17"
text_color = "#000000" if st.session_state.theme == 'Light' else "#ffffff"

st.markdown(f"""
    <style>
        .stApp, [data-testid="stSidebar"] {{ background-color: {bg_color} !important; }}
        h1, h2, h3, p, label {{ color: {text_color} !important; }}
        .stButton > button {{ background-color: #00f2ff !important; color: #000000 !important; font-weight: bold !important; }}
    </style>
""", unsafe_allow_html=True)

# المترجم + زر الإضاءة في أعلى الصفحة
col_top1, col_top2 = st.columns([1, 3])
with col_top1:
    if st.button("☀️/🌙" if st.session_state.theme == 'Dark' else "🌙/☀️"):
        toggle_theme()
        st.rerun()
with col_top2:
    st.markdown('<div id="google_translate_element"></div>', unsafe_allow_html=True)
    st.markdown('<script src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>', unsafe_allow_html=True)

# --- بقية الكود الخاص بك (نظام الدخول والأقسام) ---
if "logged_in" not in st.session_state: st.session_state["logged_in"] = False
if "users_db" not in st.session_state: st.session_state["users_db"] = {"AhmedAli100601": {"name": "Ahmed Ali", "email": "ahmed@cipher.io", "wallet_address": "TY7xxxx...", "fixed_deposit_wallet": "TRX_ADDRESS_001", "total_deposit": 5000.0, "total_rewards": 250.0, "total_withdraw": 0.0, "status": "active", "kyc_verified": False, "withdraw_status": "None", "p_image": None}}

# [هنا تضع باقي منطق الكود الخاص بك الذي أرسلته لي سابقاً بالكامل...]
# (لقد اختصرت المساحة هنا، لكن الكود الذي أرسلته أنت في الأعلى ضعه هنا بعد سطر 39 مباشرة)
