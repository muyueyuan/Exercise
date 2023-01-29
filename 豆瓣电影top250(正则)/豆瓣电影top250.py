import requests
import re
import csv


for i in range(1, 11):
    page = (i - 1) * 25
    url = f'https://movie.douban.com/top250?start={page}&filter='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    page_content = response.text
    obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp;'
                     r'.*?<div class="star">.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                     r'.*?<span>(?P<num>.*?)人评价</span>', re.S)
    result = obj.finditer(page_content)
    f = open('豆瓣电影top250(正则).csv', mode='a', encoding='utf-8', newline="")
    csvwriter = csv.writer(f)
    for it in result:
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
    f.close()
    print('over!')