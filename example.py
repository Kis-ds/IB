import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def main():
    # ChromeDriver 실행
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # 네이버 화면 이동
    driver.get('https://www.naver.com')
    time.sleep(5)
    value = driver.find_element(By.XPATH,'//*[@id="newsstand"]/div[2]/a').text
    st.write(value)
    # ChromeDriver 종료
    driver.quit()

if __name__ == '__main__':
    main()
