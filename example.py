import re
import subprocess
import streamlit as st
# 레지스트리를 통해 크롬 설치 경로 확인
command = 'reg query "HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon" /v version'
try:
    output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True).decode()
    version = re.search(r"version\s*REG_SZ\s*(.*)", output).group(1)
    st.write(f"Chrome 버전: {version}")
except subprocess.CalledProcessError as e:
    st.write("Chrome 버전을 확인할 수 없습니다.")
