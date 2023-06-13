from selenium import webdriver
import warnings
import streamlit as st

warnings.filterwarnings('ignore')

# 제어창(chromedriver) 실행
driver = webdriver.Chrome('chromedriver.exe')
# 네이버 이동
driver.get('https://www.naver.com')
