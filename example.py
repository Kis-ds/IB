import streamlit as st
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저 창을 열지 않고 실행하기 위해 headless 모드 설정

# ChromeDriver 실행 명령
command = "chromedriver"

# ChromeDriver 실행
process = subprocess.Popen(command, stdout=subprocess.PIPE)

# ChromeDriver가 실행될 때까지 잠시 대기
process.stdout.readline()

# ChromeDriver와 연결
driver = webdriver.Chrome(options=chrome_options)

# 웹 자동화 코드 작성
# ...

# ChromeDriver 종료
driver.quit()
process.terminate()
