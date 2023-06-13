import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Chrome 드라이버 설치
chrome_driver_path = ChromeDriverManager().install()

# Chrome 브라우저 버전 가져오기
options = Options()
options.add_argument("--headless")  # 브라우저 창을 열지 않고 실행하려면 추가
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Chrome 버전 가져오기
chrome_version = driver.capabilities["browserVersion"]
st.write("Chrome 버전:", chrome_version)

# 드라이버 종료
driver.quit()
