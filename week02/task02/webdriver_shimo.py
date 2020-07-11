# -*- coding: utf-8 -*-
"""
    webdriver_shimo.py
"""
from selenium import webdriver
import  time

try:
    brower = webdriver.Chrome()
    # 打开石墨
    brower.get("https://shimo.im/login?from=home")
    time.sleep(1)

    brower.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input')\
        .send_keys('xxx')
    brower.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input')\
        .send_keys('xxx')

    btn_login = brower.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')

    btn_login.click()

    time.sleep(1)

    cookies = brower.get_cookies()
    print(cookies)
    time.sleep(2)

except Exception as e:
    print(e)
finally:
    brower.close()