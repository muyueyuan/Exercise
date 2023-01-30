import requests
import re


domain = 'https://www.dytt89.com/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
                  '/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36'
}
resp = requests.get(url=domain, headers=headers)
resp.encoding = resp.apparent_encoding
# print(resp.text)
obj1 = re.compile(r'2023必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)
result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group('ul')
    # print(ul)
    result2 = obj2.finditer(ul)
    for itt in result2:
        child_href = domain + itt.group('href').strip("/")
        child_href_list.append(child_href)        #把子页面链接保存起来
for href in child_href_list:
    child_resp = requests.get(url=href, headers=headers)
    child_resp.encoding = child_resp.apparent_encoding
    # print(child_resp.text)
    result3 = obj3.search(child_resp.text)
    print(result3.group('movie'))
    print(result3.group('download'))
    # break
