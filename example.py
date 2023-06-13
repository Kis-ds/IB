import re
import subprocess
import streamlit as st

# 실행 가능한 명령어를 통해 크롬 버전 정보 얻기
command = ['google-chrome', '--version']  # 또는 'chrome', 'chromium-browser' 등
try:
    output = subprocess.check_output(command, stderr=subprocess.STDOUT).decode()
    version = output.split(' ')[2].strip()
    print(f"Chrome 버전: {version}")
except subprocess.CalledProcessError as e:
    print("Chrome 버전을 확인할 수 없습니다.")
