import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Cipher Edge", layout="centered")

# 2. التنسيق العام (CSS للنظام الجديد)
st.markdown("""
    <style>
        /* خلفية بيضاء/رمادي فاتح */
        .stApp { background-color: #f8f9fa !important; }
        
        /* النصوص والأرقام باللون الأسود */
        h1, h2, h3, p, div { color: #000000 !important; }
        
        /* الرصيد الإجمالي باللون الأصفر */
        .balance-box { 
            background-color: #FFD700; 
            padding: 20px; 
            border-radius: 15px; 
            text-align: center; 
            font-weight: bold; 
            color: #000; 
        }
        
        /* الأيقونات السفلية الزجاجية */
        .nav-icon {
            background: rgba(173, 216, 230, 0.3);
            border: 1px solid #00f2ff;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            cursor: pointer;
        }
        .nav-icon:active { background: #00008b !important; }
    </style>
""", unsafe_allow_html=True)

# 3. عرض الرصيد (مثال)
st.markdown('<div class="balance-box">Total Net Worth: 5,250.00 USDT</div>', unsafe_allow_html=True)

# 4. التنقل السفلي (أيقونات)
col1, col2, col3, col4 = st.columns(4)
with col1: st.markdown('<div class="nav-icon">🏠</div>', unsafe_allow_html=True)
with col2: st.markdown('<div class="nav-icon">📊</div>', unsafe_allow_html=True)
with col3: st.markdown('<div class="nav-icon">💰</div>', unsafe_allow_html=True)
with col4: st.markdown('<div class="nav-icon">⚙️</div>', unsafe_allow_html=True)

# --- هنا ستبدأ بإضافة محتوى الصفحات الخاص بك تدريجياً ---
