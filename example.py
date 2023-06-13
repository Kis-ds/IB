import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Streamlit 앱 설정
st.set_page_config(page_title="Selenium with Streamlit")

# Chrome 드라이버 설치
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # 브라우저 창을 열지 않고 실행하려면 추가할 수 있습니다.
chrome_driver = ChromeDriverManager().install()

# Streamlit 앱 내에서 Selenium 사용
st.title("Selenium with Streamlit")

# 검색어 입력
search_query = st.text_input("Enter a search query")

# 검색 버튼 클릭 시
if st.button("Search"):
    # Selenium으로 검색 결과 가져오기
    with webdriver.Chrome(chrome_driver, options=chrome_options) as driver:
        driver.get("https://www.google.com/search?q=" + search_query)
        title = driver.title

    # 검색 결과 타이틀 출력
    st.write("Search Result Title:", title)
