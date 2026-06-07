import streamlit as st
import pandas as pd
# --- إضافة الزر والمترجم في قمة الصفحة ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div id="google_translate_element"></div>
    </div>
    <script type="text/javascript">
        function googleTranslateElementInit() {
            new google.translate.TranslateElement({pageLanguage: 'en', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
        }
    </script>
    <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
""", unsafe_allow_html=True)

if st.button("☀️ / 🌙 تبديل النمط"):
    st.session_state.theme = 'Light' if st.session_state.get('theme', 'Dark') == 'Dark' else 'Dark'
    st.rerun()

# --- بقية كودك القديم يبدأ من هنا ---
# 1. إعدادات الصفحة
st.set_page_config(page_title="Cipher Edge Network", page_icon="💎", layout="centered", initial_sidebar_state="expanded")

# 2. نظام الإضاءة (تأكد أن هذا الكود في الأعلى)
if 'theme' not in st.session_state: st.session_state.theme = 'Dark'
def toggle_theme(): st.session_state.theme = 'Light' if st.session_state.theme == 'Dark' else 'Dark'
bg_color = "#ffffff" if st.session_state.theme == 'Light' else "#0b0f17"
text_color = "#000000" if st.session_state.theme == 'Light' else "#ffffff"

st.markdown(f"""
    <style>
        .stApp, [data-testid="stSidebar"], .stSidebar {{ background-color: {bg_color} !important; }}
        h1, h2, h3, h4, h5, h6, p, label, span, small, .stMarkdown p {{ color: {text_color} !important; }}
        .stButton > button {{ background-color: #00f2ff !important; color: #000000 !important; font-weight: bold !important; border: 1px solid #00f2ff !important; }}
    </style>
""", unsafe_allow_html=True)

# 3. زر الإضاءة والمترجم (المدمج في الأعلى)
col_ui, col_tr = st.columns([1, 4])
with col_ui:
    if st.button("☀️/🌙", key="btn_theme"): toggle_theme(); st.rerun()
with col_tr:
    st.markdown('<div id="google_translate_element"></div><script type="text/javascript">function googleTranslateElementInit(){new google.translate.TranslateElement({pageLanguage: "en", layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, "google_translate_element");}</script><script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>', unsafe_allow_html=True)

import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة والترجمة الذكية
st.set_page_config(
    page_title="Cipher Edge Network",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="expanded"
)

# إضافة أداة ترجمة جوجل الرسمية في أعلى التطبيق
st.markdown("""
    <div id="google_translate_element" style="text-align:right; padding:5px;"></div>
    <script type="text/javascript">
        function googleTranslateElementInit() {
            new google.translate.TranslateElement({
                pageLanguage: 'en',
                layout: google.translate.TranslateElement.InlineLayout.SIMPLE
            }, 'google_translate_element');
        }
    </script>
    <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
""", unsafe_allow_html=True)

# 2. تهيئة قواعد البيانات المؤقتة (Session State)
if "logged_in" not in st.session_state: st.session_state["logged_in"] = False
if "username" not in st.session_state: st.session_state["username"] = ""
if "role" not in st.session_state: st.session_state["role"] = "user"
if "current_view" not in st.session_state: st.session_state["current_view"] = "Dashboard"

# ذاكرة المشرفين
if "supervisors" not in st.session_state:
    st.session_state["supervisors"] = {"sub_admin1": "Super2026"}

# قاعدة بيانات الأعضاء الشاملة
if "users_db" not in st.session_state:
    st.session_state["users_db"] = {
        "AhmedAli100601": {
            "name": "Ahmed Ali",
            "email": "ahmed@cipher.io",
            "phone": "+201000000000",
            "status": "active",
            "kyc_front": None, "kyc_back": None, "kyc_selfie": None,
            "kyc_verified": False,
            "wallet_name": "Binance",
            "wallet_address": "TY7xxxxxxxxx...xxxx", # محفظة السحب الخاصة بالعضو
            "fixed_deposit_wallet": "TRX_PERMANENT_DEPOSIT_ADDRESS_001", # محفظة الإيداع المحددة من الأدمن
            "total_deposit": 5000.0,
            "total_withdraw": 0.0,
            "total_rewards": 250.0,
            "withdraw_status": "None",
            "p_image": None
        }
    }

# ذاكرة الإشعارات والدعم
if "global_notices" not in st.session_state: st.session_state["global_notices"] = ["🚀 Welcome to Cipher Edge VIP Network Node."]
if "private_notices" not in st.session_state: st.session_state["private_notices"] = {"AhmedAli100601": []}
if "support_tickets" not in st.session_state: st.session_state["support_tickets"] = {"AhmedAli100601": []}

# 🎨 الحقن البصري وتفعيل وميض الأزرار عند اللمس (Hover Effects)
st.markdown("""
    <style>
    .stApp, [data-testid="stSidebar"], .stSidebar { background-color: #0b0f17 !important; }
    .block-container { max-width: 480px !important; padding-top: 1rem !important; }
    h1, h2, h3, h4, h5, h6, p, label, span, small, .stMarkdown p { color: #ffffff !important; }
    
    .stButton > button {
        background-color: #00f2ff !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: 1px solid #00f2ff !important;
        opacity: 1 !important;
        transition: all 0.3s ease-in-out !important;
    }
    .stButton > button p { color: #000000 !important; font-weight: bold !important; }
    
    .stButton > button:hover {
        background-color: #00ff88 !important;
        border-color: #00ff88 !important;
        box-shadow: 0 0 20px rgba(0, 255, 136, 0.8) !important;
        transform: scale(1.02);
    }
    
    div[data-testid="stFormSubmitButton"] button, .secondary-btn button {
        background-color: #161b22 !important; color: #ffffff !important; border: 1px solid #30363d !important;
    }
    
    .status-active { background-color: #00ff88; color: #000; padding: 4px 10px; border-radius: 20px; font-weight: bold; font-size: 12px; }
    .status-suspended { background-color: #ff7b72; color: #fff; padding: 4px 10px; border-radius: 20px; font-weight: bold; font-size: 12px; }
    
    .premium-card { background: #121824 !important; border: 2px solid #00f2ff !important; border-radius: 16px !important; padding: 20px !important; margin-bottom: 20px !important; }
    .brand-title { background: linear-gradient(to right, #00ff88, #00f2ff) !important; -webkit-background-clip: text !important; -webkit-text-fill-color: transparent !important; font-size: 36px !important; font-weight: 900 !important; text-align: center !important; }
    .notice-box-global { background-color: rgba(122, 34, 255, 0.2) !important; border-left: 6px solid #7a22ff !important; padding: 10px; border-radius: 8px; margin-bottom: 10px; }
    .notice-box-private { background-color: rgba(0, 255, 136, 0.2) !important; border-left: 6px solid #00ff88 !important; padding: 10px; border-radius: 8px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 🛑 بوابة تسجيل الدخول وإنشاء الحساب
# ==========================================
if not st.session_state["logged_in"]:
    st.markdown('<div class="brand-title">CIPHER EDGE</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#8b949e;'>GLOBAL ENCRYPTION NODE</p>", unsafe_allow_html=True)
    
    tab_login, tab_signup = st.tabs(["🔒 Log in", "📝 Registration"])
    
    with tab_login:
        in_user = st.text_input("Username *")
        in_pass = st.text_input("Password *", type="password")
        
        if st.button("Log in ⚡", use_container_width=True):
            u_clean = in_user.strip()
            if u_clean == "Admin_Cipher" and in_pass == "Cipher2026":
                st.session_state["logged_in"] = True
                st.session_state["username"] = "Super Admin"
                st.session_state["role"] = "admin"
                st.session_state["current_view"] = "AdminDashboard"
                st.rerun()
            elif u_clean in st.session_state["supervisors"] and st.session_state["supervisors"][u_clean] == in_pass:
                st.session_state["logged_in"] = True
                st.session_state["username"] = u_clean
                st.session_state["role"] = "supervisor"
                st.session_state["current_view"] = "SupervisorDashboard"
                st.rerun()
            elif u_clean in st.session_state["users_db"]:
                st.session_state["logged_in"] = True
                st.session_state["username"] = u_clean
                st.session_state["role"] = "user"
                st.session_state["current_view"] = "Dashboard"
                st.rerun()
            else:
                st.error("Invalid credentials signature.")
                
    with tab_signup:
        with st.form("signup_node"):
            new_u = st.text_input("Desired Username *")
            new_n = st.text_input("Full Name *")
            new_e = st.text_input("Email Address *")
            new_p = st.text_input("Password *", type="password")
            btn_sign = st.form_submit_button("Register 🚀", use_container_width=True)
            if btn_sign and new_u and new_n:
                st.session_state["users_db"][new_u.strip()] = {
                    "name": new_n, "email": new_e, "phone": "", "status": "active",
                    "kyc_front": None, "kyc_back": None, "kyc_selfie": None, "kyc_verified": False,
                    "wallet_name": "Binance", "wallet_address": "",
                    "fixed_deposit_wallet": "PENDING_ADMIN_ASSIGNMENT", # يتم تعيينها لاحقاً من الأدمن
                    "total_deposit": 0.0, "total_withdraw": 0.0, "total_rewards": 0.0,
                    "withdraw_status": "None", "p_image": None
                }
                st.success("Registration success! Please switch to Log in tab.")

# ==========================================
# 👑 لوحة تحكم الأدمن + المشرف (الرتب العليا)
# ==========================================
elif st.session_state["role"] in ["admin", "supervisor"]:
    role_title = "👑 Super Admin" if st.session_state["role"] == "admin" else "🛠️ System Supervisor"
    
    with st.sidebar:
        st.markdown(f"<div style='text-align:center;'><h3>{role_title}</h3></div>", unsafe_allow_html=True)
        if st.button("📊 Global Core Monitor", use_container_width=True): st.session_state["current_view"] = "AdminDashboard"; st.rerun()
        if st.button("📢 Broadcast Alerts Terminal", use_container_width=True): st.session_state["current_view"] = "AdminAnnounce"; st.rerun()
        if st.button("🛠️ Support Desk Hub", use_container_width=True): st.session_state["current_view"] = "AdminSupport"; st.rerun()
        if st.button("👥 Directory & KYC Verification", use_container_width=True): st.session_state["current_view"] = "AdminUsers"; st.rerun()
        
        if st.session_state["role"] == "admin":
            st.write("---")
            if st.button("➕ Deploy Supervisor Node", use_container_width=True): st.session_state["current_view"] = "AddSupervisor"; st.rerun()
            
        st.write("---")
        if st.button("Sign out 🚪", use_container_width=True):
            st.session_state["logged_in"] = False
            st.session_state["current_view"] = "Login"
            st.rerun()

    if st.session_state["current_view"] == "AddSupervisor" and st.session_state["role"] == "admin":
        st.title("➕ Deploy Supervisor Node")
        sup_u = st.text_input("Supervisor Username:")
        sup_p = st.text_input("Supervisor Password:", type="password")
        if st.button("Grant Restricted Access Signature ⚡"):
            if sup_u and sup_p:
                st.session_state["supervisors"][sup_u.strip()] = sup_p
                st.success("Supervisor initialized successfully.")

    elif st.session_state["current_view"] == "AdminDashboard":
        st.title("📊 Global Core Monitor")
        st.write("---")
        st.metric(label="Total Tracked Nodes", value=f"{len(st.session_state['users_db'])} Users")

    elif st.session_state["current_view"] == "AdminAnnounce":
        st.title("📢 Broadcast Alerts Terminal")
        st.write("---")
        st.subheader("Public Broadcast Signal")
        msg_g = st.text_input("Alert message text:")
        confirm_g = st.checkbox("Confirm public broadcast deployment")
        if st.button("Fire Signal to All Active Nodes 🚀") and confirm_g:
            if msg_g:
                st.session_state["global_notices"].append(msg_g)
                st.success("Public signal deployed.")

    elif st.session_state["current_view"] == "AdminSupport":
        st.title("🛠️ Support Desk Hub")
        st.write("---")
        active_tickets = list(st.session_state["support_tickets"].keys())
        if active_tickets:
            sel_u = st.selectbox("Select Support Session Log:", active_tickets)
            for m in st.session_state["support_tickets"][sel_u]:
                st.write(f"**{m['sender'].upper()}:** {m['message']}")
            rep = st.text_input("Compose terminal response:")
            if st.button("Transmit Response ⚡"):
                if rep:
                    st.session_state["support_tickets"][sel_u].append({"sender": "admin", "message": rep})
                    st.success("Transmitted.")
                    st.rerun()
        else:
            st.info("No active support tickets.")

    # 📌 تعديل لوحة التحكم الخاصة بالأدمن لإضافة حقل ملء محفظة إيداع العميل
    elif st.session_state["current_view"] == "AdminUsers":
        st.title("👥 Directory & KYC Verification")
        st.write("---")
        
        for u_id, u_data in st.session_state["users_db"].items():
            st.markdown(f"### Node: `{u_id}`")
            st.write(f"**Name:** {u_data['name']} | **Email:** {u_data['email']}")
            st.write(f"**Saved Withdrawal Wallet:** `{u_data['wallet_address']}` ({u_data['wallet_name']})")
            
            st.write("---")
            # 🔥 خامساً (1): حقل ملء وتعديل عنوان محفظة الإيداع الخاص بالعضو من قبل الأدمن
            st.subheader("📥 Assign Deposit Wallet Address")
            admin_assigned_wallet = st.text_input(f"Set Permanent Deposit Wallet for {u_id}:", value=u_data["fixed_deposit_wallet"], key=f"fixed_{u_id}")
            if st.button(f"Save Deposit Address for {u_id}", key=f"btn_fixed_{u_id}"):
                u_data["fixed_deposit_wallet"] = admin_assigned_wallet.strip()
                st.success(f"Successfully set deposit wallet for {u_id}!")
                st.rerun()
            st.write("---")

            st.write("Status Controls:")
            col_act, col_susp = st.columns(2)
            with col_act:
                if st.button(f"Activate {u_id}", key=f"act_{u_id}"): 
                    u_data["status"] = "active"; st.rerun()
            with col_susp:
                if st.button(f"Suspend {u_id}", key=f"susp_{u_id}"): 
                    u_data["status"] = "suspended"; st.rerun()
                    
            st.write("**KYC Documents:**")
            if u_data["kyc_front"]: st.image(u_data["kyc_front"], caption="Front", width=150)
            if u_data["kyc_back"]: st.image(u_data["kyc_back"], caption="Back", width=150)
            if u_data["kyc_selfie"]: st.image(u_data["kyc_selfie"], caption="Selfie", width=150)
            
            st.write(f"Current KYC Status: **{u_data['kyc_verified']}**")
            if not u_data["kyc_verified"]:
                if st.button(f"Verify and Clear KYC for {u_id}", key=f"v_kyc_{u_id}"):
                    u_data["kyc_verified"] = True; st.success("Cleared."); st.rerun()
            else:
                if st.button(f"Revoke KYC for {u_id}", key=f"r_kyc_{u_id}"):
                    u_data["kyc_verified"] = False; st.rerun()
                    
            if u_data["withdraw_status"] == "pending":
                st.warning("⚠️ Pending Withdrawal Request Found!")
                if st.button(f"Approve Payout for {u_id}", key=f"payout_{u_id}"):
                    u_data["withdraw_status"] = "completed"
                    u_data["total_withdraw"] += 10.0
                    st.success("Paid."); st.rerun()
            st.write("---")

# ==========================================
# 👤 الشق الثالث: لوحة تحكم حساب العميل الشاملة
# ==========================================
elif st.session_state["role"] == "user":
    c_user = st.session_state["username"]
    ud = st.session_state["users_db"][c_user]
    
    d_val = float(ud["total_deposit"])
    r_val = float(ud["total_rewards"])
    w_val = float(ud["total_withdraw"])
    total_net_worth = d_val + r_val - w_val
    
    with st.sidebar:
        if ud["status"] == "active":
            st.markdown("<span class='status-active'>🟢 ACTIVE NODE</span>", unsafe_allow_html=True)
        else:
            st.markdown("<span class='status-suspended'>🔴 SUSPENDED NODE</span>", unsafe_allow_html=True)
            
        if ud["p_image"] is not None:
            st.image(ud["p_image"], width=100)
            
        st.markdown(f"<h4>👤 Welcome, {c_user}</h4>", unsafe_allow_html=True)
        
        # الأزرار تفاعلية بالكامل وتنقلك فورا لصفحتها مع تأثير الوميض
        if st.button("📊 Dashboard / لوحة التحكم", use_container_width=True): st.session_state["current_view"] = "Dashboard"; st.rerun()
        if st.button("📥 Deposit / الايداع", use_container_width=True): st.session_state["current_view"] = "Deposit"; st.rerun()
        if st.button("📤 Withdraw / السحب", use_container_width=True): st.session_state["current_view"] = "Withdraw"; st.rerun()
        if st.button("📈 Yield Levels Plans", use_container_width=True): st.session_state["current_view"] = "Plans"; st.rerun()
        if st.button("🔗 Referral Matrix Hub", use_container_width=True): st.session_state["current_view"] = "Referral"; st.rerun()
        if st.button("🛠️ Customer Service Desk", use_container_width=True): st.session_state["current_view"] = "Support"; st.rerun()
        if st.button("⚙️ Profile & KYC Lock", use_container_width=True): st.session_state["current_view"] = "Profile"; st.rerun()
        
        st.write("---")
        if st.button("Sign out 🚪", use_container_width=True):
            st.session_state["logged_in"] = False
            st.session_state["current_view"] = "Login"
            st.rerun()

    if st.session_state["current_view"] == "Dashboard":
        col_t, col_b = st.columns([5,1])
        with col_t: st.title("📊 Dashboard")
        with col_b:
            p_cnt = len(st.session_state["private_notices"].get(c_user, []))
            t_not = len(st.session_state["global_notices"]) + p_cnt
            if st.button(f"🔔({t_not})"): st.session_state["current_view"] = "Notifications"; st.rerun()
            
        st.markdown(f'''
            <div class="premium-card">
                <span style="font-size:12px;color:#8b949e;">TOTAL NET WORTH BALANCE</span>
                <h1 style="color:#00f2ff;margin:5px 0;">${total_net_worth:,.2f} USDT</h1>
            </div>
        ''', unsafe_allow_html=True)
        
        met1, met2, met3 = st.columns(3)
        with met1: st.metric("Total Deposit", f"${d_val:,.2f}")
        with met2: st.metric("Total Withdraw", f"${w_val:,.2f}")
        with met3: st.metric("Total Rewards", f"${r_val:,.2f}")
        
        st.write("---")
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("📥 Go to Deposit / الايداع", use_container_width=True):
                st.session_state["current_view"] = "Deposit"; st.rerun()
        with col_btn2:
            if st.button("📤 Go to Withdraw / السحب", use_container_width=True):
                st.session_state["current_view"] = "Withdraw"; st.rerun()
        
        if ud["withdraw_status"] == "pending":
            st.warning("⏱️ Current Extraction Protocol Status: PENDING CONTROL CLEARANCE")

    elif st.session_state["current_view"] == "Notifications":
        st.title("🔔 Feed Terminal")
        for notice in st.session_state["global_notices"]:
            st.markdown(f'<div class="notice-box-global">📢 {notice}</div>', unsafe_allow_html=True)
        if st.button("Back"): st.session_state["current_view"] = "Dashboard"; st.rerun()

    # شاشة الملف الشخصي - تفعيل رفع وثائق التوثيق ورفع الصورة وربط محفظة السحب
    elif st.session_state["current_view"] == "Profile":
        st.title("⚙️ Profile & KYC Core")
        st.write("---")
        
        st.subheader("👤 User Avatar / الصورة الشخصية")
        img_p = st.file_uploader("Upload Profile Image Avatar", type=["jpg", "png"])
        if img_p and st.button("Save Avatar / حفظ الصورة الشخصية"):
            ud["p_image"] = img_p; st.success("Avatar linked successfully."); st.rerun()
            
        st.write("---")
        # 🔥 خامساً (2): خانة تسجيل وربط عنوان محفظة السحب للعميل لحمايته وقفلها
        st.subheader("🔒 Payout Address Vault / محفظة السحب للعميل")
        if ud["wallet_address"] == "":
            st.info("Please set your permanent payout withdrawal address. Once saved, it cannot be altered manually.")
            plat_val = st.selectbox("Exchange/Wallet Platform", options=["Binance", "OKX", "Bybit"])
            addr_val = st.text_input("Your Withdrawal Wallet Address (USDT TRC20) *")
            if st.button("Permanently Store Wallet Destination"):
                if addr_val.strip() != "":
                    ud["wallet_name"] = plat_val
                    ud["wallet_address"] = addr_val.strip()
                    st.success("Withdrawal address secured and locked successfully.")
                    st.rerun()
                else:
                    st.error("Address field cannot be blank.")
        else:
            st.success(f"🔒 Locked Payout Destination: {ud['wallet_name']} - `{ud['wallet_address']}`")

        st.write("---")
        st.subheader("📑 Identity Verification (KYC)")
        if not ud["kyc_verified"]:
            f_img = st.file_uploader("1. Document Front Face View", type=["jpg", "png"])
            b_img = st.file_uploader("2. Document Rear Back View", type=["jpg", "png"])
            s_img = st.file_uploader("3. Facial Verification Live Selfie", type=["jpg", "png"])
            if st.button("Upload KYC Stack / رفع وثائق التوثيق"):
                if f_img and b_img and s_img:
                    ud["kyc_front"] = f_img
                    ud["kyc_back"] = b_img
                    ud["kyc_selfie"] = s_img
                    st.success("Documents uploaded! Pending Admin review.")
        else:
            st.success("💎 KYC Identity Verification Cleared and Approved.")

    # شاشة الإيداع - يرى العضو العنوان الذي حدده الأدمن له بدقة
    elif st.session_state["current_view"] == "Deposit":
        st.title("📥 Deposit Protocol")
        st.write("---")
        st.subheader("Your Assigned Permanent Deposit Network Address:")
        
        # يظهر هنا العنوان الثابت الذي يضعه الأدمن من لوحته
        st.code(ud["fixed_deposit_wallet"], language="text")
        
        st.write("⚠️ **Security Alert Trigger Control:**")
        st.caption("Deposits arriving from coordinates other than your locked address will halt.")
        
        amt_d = st.number_input("Amount to inject ($)", min_value=10.0)
        from_addr = st.text_input("Originating Transmitting Address Hash:")
        
        if st.button("Confirm Ingestion Transfer ⚡"):
            ud["total_deposit"] += amt_d
            st.success("Transfer initialized and cleared successfully.")

    elif st.session_state["current_view"] == "Withdraw":
        st.title("📤 Withdraw Protocol")
        st.write("---")
        if not ud["kyc_verified"]:
            st.error("🛑 Extraction Blocked: Complete KYC identity stack audit first in Profile page.")
        elif ud["wallet_address"] == "":
            st.error("🛑 Extraction Blocked: Please save your Withdrawal Wallet Address in Profile page first.")
        else:
            st.success("🔓 Liquidity Extraction Enabled.")
            st.write(f"Destination Platform: **{ud['wallet_name']}** | Address: `{ud['wallet_address']}`")
            amt_w = st.number_input("Extraction Amount ($)", min_value=10.0, max_value=total_net_worth)
            if st.button("Authorize Extraction Protocol", type="primary"):
                ud["withdraw_status"] = "pending"
                st.info("⚡ Extraction status changed to: PENDING.")

    elif st.session_state["current_view"] == "Plans":
        st.title("📈 Yield Accumulation Level Arrays")
        st.write("---")
        for i in range(1, 6):
            st.markdown(f'''
                <div class="premium-card">
                    <h3 style="color:#00f2ff;margin:0;">Level {i} Investment Plan Node</h3>
                    <p style="font-size:12px;color:#00ff88;margin:5px 0;">Status: Ready for Activation</p>
                </div>
            ''', unsafe_allow_html=True)

    elif st.session_state["current_view"] == "Referral":
        st.title("🔗 Referral Matrix Hub")
        st.write("---")
        ref_list = [f"https://cipher-edge.io/join?ref={c_user}-{i:03d}" for i in range(1, 11)]
        st.dataframe(ref_list, column_config={"value": "Access Signature Link Route"})

    elif st.session_state["current_view"] == "Support":
        st.title("🛠️ Customer Service Desk Feed")
        st.write("---")
        if c_user not in st.session_state["support_tickets"]: st.session_state["support_tickets"][c_user] = []
        for m in st.session_state["support_tickets"][c_user]:
            st.write(f"**{m['sender'].upper()}:** {m['message']}")
        msg_s = st.text_input("Type support terminal payload string:")
        if st.button("Transmit Payload to Support Node ⚡"):
            if msg_s:
                st.session_state["support_tickets"][c_user].append({"sender": "user", "message": msg_s})
                st.toast("✅ Support packet transmitted!", icon="🚀")
                st.rerun()
