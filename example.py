import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# ChromeDriverManager로 특정 버전의 ChromeDriver 설치
driver = webdriver.Chrome(ChromeDriverManager(version="114.0.5735.110").install())
#driver = webdriver.Chrome(ChromeDriverManager().install())

# 네이버 화면 이동
driver.get('https://www.naver.com')
time.sleep(5)
value = driver.find_element(By.XPATH,'//*[@id="newsstand"]/div[2]/a').text
st.write(value)
# ChromeDriver 종료
driver.quit()
