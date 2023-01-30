import requests
from bs4 import BeautifulSoup
import time


url = 'https://www.umei.cc/bizhitupian/weimeibizhi/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
                  '/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36'
}
resp = requests.get(url=url, headers=headers)
resp.encoding = resp.apparent_encoding
# print(resp.text)
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find('div', class_="item_list infinite_scroll").find_all('a')
# print(alist)
for a in alist:
    href = 'https://www.umei.cc' + a.get('href')
    # print(href)
    child_page_resp = requests.get(url=href, headers=headers)
    child_page_resp.encoding = child_page_resp.apparent_encoding
    child_page_text = child_page_resp.text
    child_page = BeautifulSoup(child_page_text, "html.parser")
    img = child_page.find('div', class_="big-pic").find('img')
    src = img.get('src')
    img_resp = requests.get(url=src, headers=headers)
    img_resp.encoding = img_resp.apparent_encoding
    # img_resp.content
    img_name = src.split("/")[-1]
    with open("img/" + img_name, mode='wb') as f:
        f.write(img_resp.content)

    print('over', img_name)
    time.sleep(1)
print('all over!')
