import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# ChromeDriverManager로 특정 버전의 ChromeDriver 설치
#driver = webdriver.Chrome(ChromeDriverManager().install())

# 네이버 화면 이동
#driver.get('https://www.naver.com')
#time.sleep(5)
#value = driver.find_element(By.XPATH,'//*[@id="newsstand"]/div[2]/a').text
#st.write(value)
# ChromeDriver 종료
#driver.quit()

# Chrome 드라이버 설치
chrome_driver_path = ChromeDriverManager().install()

# Chrome 브라우저 버전 가져오기
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창을 열지 않고 실행하려면 추가
driver = webdriver.Chrome(chrome_driver_path, options=options)

# Chrome 버전 가져오기
chrome_version = driver.capabilities["browserVersion"]
st.write("Chrome 버전:", chrome_version)

# 드라이버 종료
driver.quit()
