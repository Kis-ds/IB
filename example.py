from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
import streamlit as st
import time
warnings.filterwarnings('ignore')

# 제어창(chromedriver) 실행
driver = webdriver.Chrome('chromedriver.exe')
# 네이버 화면 이동
driver.get('https://www.naver.com')
time.sleep(5)
