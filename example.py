import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriver 경로 설정
chrome_driver_path = ChromeDriverManager().install()

# ChromeDriver 서비스 생성
service = Service(chrome_driver_path)

# Chrome 옵션 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # 브라우저 창을 열지 않고 실행하기 위해 headless 모드 설정

# ChromeDriver 실행
with webdriver.Chrome(service=service, options=chrome_options) as driver:
    # 웹 자동화 코드 작성
    # ...
    pass  # 필요한 동작 수행

# ChromeDriver 종료
service.stop()
