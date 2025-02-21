import streamlit as st
import random

# 初始化 session_state
if "page" not in st.session_state:
    st.session_state.page = "main"

# 畫面切換邏輯
if st.session_state.page == "main":
    st.title("🍽️ 你今天想選擇什麼？")
    
    # 三個按鈕選擇不同類別
    if st.button("🥤 飲料選擇"):
        st.session_state.page = "drink"
    if st.button("🍱 午餐選擇"):
        st.session_state.page = "lunch"
    if st.button("🍛 晚餐選擇"):
        st.session_state.page = "dinner"

elif st.session_state.page == "drink":
    st.title("🥤 來點飲料吧！")
    # 這裡放飲料選擇邏輯
    if st.button("返回主畫面"):
        st.session_state.page = "main"

elif st.session_state.page == "lunch":
    st.title("🍱 午餐來點什麼呢？")
    # 這裡放午餐選擇邏輯
    if st.button("返回主畫面"):
        st.session_state.page = "main"

elif st.session_state.page == "dinner":
    st.title("🍛 晚餐吃什麼好呢？")
    # 這裡放晚餐選擇邏輯（可以用你現在寫好的程式）
    # 晚餐選項
dinner_options = [
    "好食居", "彈牙麵", "長生鹽人", "存嘉", "超厚切豬排", "泰國小館", "實至名歸",
    "樂三宰相", "薯樂堡", "孫東寶", "仙客來", "明德小炒", "魯三塊", "越南小吃",
    "石二鍋", "泰圓", "SUBBER", "江家牛肉麵永和豆漿", "劉媽媽抄手大滷麵",
    "Hale", "奎人豬排", "Runnyegg Burger", "築間"
]

# 設定 CSS 樣式
st.markdown(
    """
    <style>
        /* 讓標題置中 */
        .title {
            text-align: center;
            font-size: 40px !important;
            font-weight: bold;
        }
        
        /* 讓副標題置中並調整大小 */
        .subtitle {
            text-align: center;
            font-size: 20px !important;
            color: gray;
        }
        
        /* 設定按鈕的樣式 */
        div.stButton > button {
            font-size: 25px !important;
            padding: 15px 30px;
            background-color: #ffcc00;
            color: black;
            border-radius: 10px;
            border: none;
            display: block;
            margin: 0 auto; /* 讓按鈕置中 */
        }
        
        /* 結果顯示的樣式 */
        .result-box {
            text-align: center;
            font-size: 25px !important;
            font-weight: bold;
            color: #ff6600;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# **標題與副標題**
st.markdown("<p class='title'>🤍 今天吃什麼 🤍</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>點擊按鈕決定今天的晚餐！</p>", unsafe_allow_html=True)

# **按鈕置中**
col1, col2, col3 = st.columns([1, 2, 1])  # col2 設大一點，讓按鈕更居中
with col2:
    if st.button("🍴我要甲奔🥤"):
        choice = random.choice(dinner_options)
        st.markdown(f"<p class='result-box'>🍴今天吃：{choice}🍺</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;font-size: 20px; font-weight: bold; color: #888888;'>今天辛苦了 快去吃飯吧(๑•̀ㅂ•́)و✧</p>", unsafe_allow_html=True)

    if st.button("返回主畫面"):
        st.session_state.page = "main"

