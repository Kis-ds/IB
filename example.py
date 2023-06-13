from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')

# 제어창(chromedriver) 실행
driver = webdriver.Chrome('chromedriver.exe')
# 네이버 화면 이동
driver.get('https://www.naver.com')
value = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/ul/li[1]/span/a[1]').text
st.write(value)