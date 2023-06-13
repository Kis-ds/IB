import streamlit as st
import subprocess
from bs4 import BeautifulSoup
import requests

# ChromeDriver 실행 파일 경로
chromedriver_path = "/home/appuser/.wdm/drivers/chromedriver/linux64/114.0.5735.90/chromedriver"

# 실행 권한 추가
subprocess.run(["chmod", "+x", chromedriver_path], check=True)

# Streamlit 앱 시작
st.title("Streamlit with Selenium")

# 웹 크롤링 작업
url = "https://www.example.com"  # 크롤링할 웹 페이지의 URL
command = [chromedriver_path]
process = subprocess.Popen(command, stdout=subprocess.PIPE)
output = process.communicate()[0]

# 웹 페이지 파싱
soup = BeautifulSoup(output, "html.parser")
title = soup.title.string

# 추출한 제목 출력
st.write("Web Page Title:", title)
