import streamlit as st
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriver Manager를 사용하여 ChromeDriver 설치 및 경로 가져오기
chrome_driver_path = ChromeDriverManager().install()

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저 창을 띄우지 않고 실행할 경우

# ChromeDriver 실행
try:
    with webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options) as driver:
        # Streamlit 앱 구성
        st.title("Streamlit with Selenium")

        # 크롤링 작업 등 수행
        driver.get("https://www.example.com")
        st.write(driver.title)
except Exception as e:
    st.error(f"Failed to start ChromeDriver: {e}")
    sys.exit(1)
