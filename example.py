import streamlit as st
import subprocess
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriver 경로 확인
command = "which chromedriver"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, _ = process.communicate()
chromedriver_path = output.decode().strip()

# Chrome 옵션 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # 브라우저 창을 띄우지 않고 실행할 경우

# ChromeDriver 실행
try:
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
except Exception as e:
    st.error(f"Failed to start ChromeDriver: {e}")
    sys.exit(1)

# Streamlit 앱 구성
st.title("Streamlit with Selenium")

# 크롤링 작업 등 수행
driver.get("https://www.example.com")
st.write(driver.title)

# ChromeDriver 종료
driver.quit()
