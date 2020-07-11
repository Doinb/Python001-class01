# -*- coding: utf-8 -*-
"""
    requests_shimo.py
    使用requests去模拟登录石墨文档
"""
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False, use_cache_server=False)

headers = {
    'User-Agent': ua.random,
    'Referer': 'https://shimo.im/login?from=home',
    'origin': 'https://shimo.im',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'x-requested-with': 'XmlHttpRequest',
    'x-source': 'lizard-desktop',
}

s = requests.Session()

login_url = 'https://shimo.im/lizard-api/auth/password/login'

form_data = {
    # 脱敏
    'email': 'xxx',
    'mobile': '+86undefined',
    'password': 'xxx'
}

pre_login = 'https://shimo.im/login?from=home'
pre_resp = s.get(pre_login, headers=headers)

print(pre_resp)

response = s.post(login_url, data=form_data, headers=headers, cookies=s.cookies)

print(s.cookies)
