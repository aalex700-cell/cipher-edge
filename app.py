import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Cipher Edge", layout="wide")

# 2. نظام حفظ الحالة (اللون والأقسام)
if 'theme' not in st.session_state:
    st.session_state.theme = 'Dark'

def toggle_theme():
    st.session_state.theme = 'Light' if st.session_state.theme == 'Dark' else 'Dark'

# تحديد الألوان
bg_color = "#ffffff" if st.session_state.theme == 'Light' else "#0e1117"
text_color = "#000000" if st.session_state.theme == 'Light' else "#ffffff"

# تطبيق الألوان (CSS)
st.markdown(f"""
    <style>
        .stApp {{ background-color: {bg_color}; color: {text_color}; }}
        h1, h2, h3, p, div {{ color: {text_color} !important; }}
    </style>
""", unsafe_allow_html=True)

# 3. القائمة الجانبية (نظام التنقل)
st.sidebar.title("💠 Cipher Edge")

# زر تبديل الإضاءة في القائمة الجانبية
if st.sidebar.button("☀️ / 🌙 تبديل النمط"):
    toggle_theme()
    st.rerun()

menu = st.sidebar.radio("Navigation", ["Dashboard", "Wallet", "Transactions", "Settings"])

# 4. محتوى الصفحات
if menu == "Dashboard":
    st.title("📊 Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Balance", "$45,230.50", "+3.2%")
    col2.metric("Encryption Strength", "99.9%", "Stable")
    col3.metric("Active Nodes", "12", "0")

elif menu == "Wallet":
    st.title("💰 Your Assets")
    st.info("Secure Wallet Address: 0x7a...f4")
    if st.button("Connect Ledger"):
        st.success("Wallet connected successfully!")

elif menu == "Transactions":
    st.title("🔄 Transaction History")
    st.table({"Date": ["2026-06-07", "2026-06-06"], "Type": ["Deposit", "Withdraw"], "Amount": ["$500", "$200"]})

elif menu == "Settings":
    st.title("⚙️ Security Settings")
    st.checkbox("Enable Two-Factor Authentication (2FA)")
    st.button("Save Changes")
