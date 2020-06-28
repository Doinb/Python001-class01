# -*- coding: utf-8 -*-
"""
    maoyan_requests.py
    使用requests库+BeautifulSoup+pandas 对猫眼电影的页面进行爬虫+简单的持久化
"""
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
# cookie直接写入到代码中是否安全???
cookie = 'uuid_n_v=v1; uuid=B47805A0B92311EA8B56A5EC695B0A7341FCB9D60300464BA1B755F3068745D2; _csrf=3051fd220de186e942e0e7620677b48b3920c54bfeb1c1f619f41eba1d1c9cec; _lxsdk_cuid=172fa4eb461c8-08a9573861dda3-31607403-13c680-172fa4eb462c8; _lxsdk=B47805A0B92311EA8B56A5EC695B0A7341FCB9D60300464BA1B755F3068745D2; mojo-uuid=da38ab84b965b498654b4fa60065fde9; lt=btWugXOINhNbbHThsbtwWGgY9CoAAAAA5woAAG14-fSC_GmiXb7ZB3YNaLCWJJ78FrobVBcNwqKP9ubeQpNdQ8uBoj6-WGcPMfKmHw; lt.sig=_b1Z1Is0ec4S_WnZRBjueCCLH00; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593337361,1593337978; mojo-session-id={"id":"9f1182510ff1443f0e775184ab90c2e4","time":1593340547140}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593340547; __mta=175437085.1593337361589.1593338290687.1593340551388.12; _lxsdk_s=172fa7ea61c-b60-b93-427%7C200144354%7C5; mojo-trace-id=2'

url = 'https://maoyan.com/films?showType=3&sortId=3'

response = requests.get(url, headers={'User-Agent': user_agent, 'Cookie': cookie})

bs_info = bs(response.text, 'html.parser')

data = []
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}, limit=10):
    name = tags.find(class_='name').text
    info = tags.find_all(class_='movie-hover-title')
    # 过滤掉span标签
    tag = info[1].span.extract()
    tag_value = info[1].text.strip()
    release_time = info[3].span.extract()
    release_time_value = info[3].text.strip()
    data.append({"name": name, "tags": tag_value, "release_time": release_time_value})

    movies = pd.DataFrame(data=data)
    movies.to_csv('./maoyan_movies.csv', mode='a', encoding='utf8', index=False, header=True)
