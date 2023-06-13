import streamlit as st
from selenium import webdriver

# Streamlit 앱 시작
st.title("Streamlit with Selenium")

# ChromeDriver 실행
driver = webdriver.Chrome()
driver.get("https://www.example.com")

# 웹 페이지 제목 추출
title = driver.title

# 추출한 제목 출력
st.write("Web Page Title:", title)

# 드라이버 종료
driver.quit()
