import streamlit as st
import importlib

# 페이지 기본 설정
st.set_page_config(page_title="차량 정보", initial_sidebar_state="collapsed")

# 페이지 목록 정의
PAGES = {
    "홈": "my_pages.home",
    "전국차량등록현황": "my_pages.car_inquiry",
    "차량 FAQ": "my_pages.faq"
}

# 사이드바에서 페이지 선택
selection = st.sidebar.selectbox("메뉴", list(PAGES.keys()))

# 선택한 페이지 불러오기
module = importlib.import_module(PAGES[selection])
module.show()
