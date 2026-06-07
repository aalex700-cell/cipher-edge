import streamlit as st

# إعداد الصفحة لتكون واسعة واحترافية
st.set_page_config(page_title="Cipher Edge Portal", layout="wide")

# تخصيص الألوان والستايل
st.markdown("""
    <style>
        .main { background-color: #0e1117; color: white; }
        .stSidebar { background-color: #161b22; }
    </style>
""", unsafe_allow_html=True)

# القائمة الجانبية (نظام التنقل)
st.sidebar.title("💠 Cipher Edge")
menu = st.sidebar.radio("Navigation", ["Dashboard", "Wallet", "Transactions", "Settings"])

# محتوى الصفحات
if menu == "Dashboard":
    st.title("📊 Overview")
    st.write("Welcome back to your secure node.")
    # إضافة أعمدة لعرض البيانات
    col1, col2, col3 = st.columns(3)
    col1.metric("Balance", "$45,230.50", "+3.2%")
    col2.metric("Encryption Strength", "99.9%", "Stable")
    col3.metric("Active Nodes", "12", "0")

elif menu == "Wallet":
    st.title("💰 Your Assets")
    st.info("Secure Wallet Address: 0x7a...f4")
    # مكان لإضافة زر إيداع أو سحب
    if st.button("Connect Ledger"):
        st.success("Wallet connected successfully!")

elif menu == "Transactions":
    st.title("🔄 Transaction History")
    st.table({"Date": ["2026-06-07", "2026-06-06"], "Type": ["Deposit", "Withdraw"], "Amount": ["$500", "$200"]})

elif menu == "Settings":
    st.title("⚙️ Security Settings")
    st.checkbox("Enable Two-Factor Authentication (2FA)")
    st.button("Save Changes")
