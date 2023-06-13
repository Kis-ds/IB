import re
import subprocess
import streamlit as st
import winreg

def get_chrome_version():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon")
        value, _ = winreg.QueryValueEx(key, "version")
        return value
    except FileNotFoundError:
        return None

chrome_version = get_chrome_version()
if chrome_version:
    st.write(f"Chrome 버전: {chrome_version}")
else:
    st.write("Chrome 버전을 확인할 수 없습니다.")
