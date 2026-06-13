import streamlit as st

# CSS لإخفاء القائمة الجانبية كما اتفقنا
st.markdown("""<style>[data-testid="stSidebar"] {display: none;}</style>""", unsafe_allow_html=True)

# الحارس
if not st.session_state.get('authenticated', False):
    st.switch_page("app.py")

import streamlit as st

# CSS الاحترافي (نفس الثيم الداكن مع تحسين التباعد)
st.markdown("""
    <style>
        .stApp { background-color: #0A0F1E; color: white; }
        .rewards-card { background: linear-gradient(135deg, #00A3FF, #001F3F); padding: 20px; border-radius: 20px; text-align: center; color: white; margin-bottom: 25px; }
        .icon-box { display: flex; flex-direction: column; align-items: center; justify-content: center; color: #FFFFFF; font-size: 11px; margin-bottom: 20px; text-decoration: none; }
        .icon-box div { background: #151B2E; padding: 12px; border-radius: 12px; margin-bottom: 8px; border: 1px solid #2A3A5A; }
        .big-card { background: #151B2E; padding: 20px; border-radius: 20px; border: 1px solid #2A3A5A; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; }
        .btn-blue { background: #00A3FF; border: none; padding: 10px 20px; border-radius: 10px; color: white; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 1. قسم المكافآت
st.markdown("""<div class="rewards-card"><h3>Promotion Rewards</h3><p>Reach S2: 20 | S3: 60 | S4: 200 | S5: 600</p></div>""", unsafe_allow_html=True)

# 2. قسم الخدمات (8 أيقونات)
icons_data = [
    ("User Rules", "M14 2H6a2 2 0 0 0-2 2v16"), ("Mission", "M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"),
    ("Recharge", "M12 2v20M2 12h20"), ("Withdraw", "M12 2v20M2 12h20"),
    ("Contact", "M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"), ("Help", "M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"),
    ("Invite", "M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"), ("Benefits", "M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z")
]

# تقسيم الـ 8 أيقونات لصفين (4×2)
for i in range(0, 8, 4):
    row = st.columns(4)
    for j in range(4):
        name, path = icons_data[i+j]
        with row[j]:
            st.markdown(f'<a href="#" class="icon-box"><div><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="{path}"></path></svg></div>{name}</a>', unsafe_allow_html=True)

# 3. قسم أزرار العمليات الكبيرة
st.markdown("""
    <div class="big-card">
        <div><strong>Start Lending</strong><br><small style="color: #A0A0A0;">Earn Interest On Lending</small></div>
        <button class="btn-blue">Lend Immediately</button>
    </div>
    <div class="big-card">
        <div><strong>Credit Improvement</strong><br><small style="color: #A0A0A0;">Get More Benefits</small></div>
        <button class="btn-blue" style="background:#2A3A5A;">Promote</button>
    </div>
""", unsafe_allow_html=True)

# كود CSS للشريط السفلي الثابت
st.markdown("""
    <style>
        /* إجبار التطبيق على أخذ عرض الشاشة بالكامل */
        .stApp { background-color: #0A0F1E !important; }
        
        /* جعل الأعمدة متجاورة دائماً */
        [data-testid="column"] {
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
        }
        
        /* تنسيق الحاويات لتبدو ككروت */
        .big-card { 
            background: #151B2E; 
            padding: 15px; 
            border-radius: 15px; 
            border: 1px solid #2A3A5A; 
            margin-bottom: 10px; 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            width: 100%;
        }
        
        /* إصلاح أيقونات القائمة السفلية */
        .bottom-nav {
            display: flex !important;
            flex-direction: row !important;
            justify-content: space-around !important;
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# هيكل الأيقونات السفلية
nav_items = [
    ("Home", "M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"),
    ("Land", "M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"),
    ("Income", "M12 2v20M2 12h20"),
    ("Assets", "M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"),
    ("Me", "M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z")
]

# عرض الأيقونات
st.markdown('<div class="bottom-nav">', unsafe_allow_html=True)
for name, path in nav_items:
    st.markdown(f'''
        <div class="nav-item">
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="{path}"></path></svg>
            <br>{name}
        </div>
    ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
