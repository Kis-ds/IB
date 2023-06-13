import streamlit as st
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless") # 브라우저 창을 띄우지 않고 실행할 경우

try:
    # ChromeDriver 설치 경로 확인
    chrome_driver_path = ChromeDriverManager().install()

    # ChromeDriver 실행 권한 부여
    os.chmod(chrome_driver_path, 0o755)

    # ChromeDriver 옵션 및 서비스 설정
    driver_service = Service(chrome_driver_path)
    driver_service.start()

    with webdriver.Chrome(service=driver_service, options=chrome_options) as driver:
        # Streamlit 앱 구성
        st.title("Streamlit with Selenium")

        # 크롤링 작업 등 수행
        driver.get("https://www.example.com")
        st.write(driver.title)

    # ChromeDriver 서비스 종료
    driver_service.stop()

except Exception as e:
    st.error(f"Failed to start ChromeDriver: {e}")
