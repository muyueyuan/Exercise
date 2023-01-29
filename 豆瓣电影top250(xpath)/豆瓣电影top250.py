import requests
import parsel
import csv


for i in range(1, 11):
    page = (i - 1) * 25
    url = 'https://movie.douban.com/top250?start={}&filter='.format(str(page))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    resp = response.text    #str 字符串 可用正则提取,若要用xpath，需要转换类型
    # print(resp)
    selector = parsel.Selector(resp)     #转换类型
    # print(selector)
    lis = selector.xpath('//ol[@class="grid_view"]/li')
    for li in lis:
        title = li.xpath('.//div[@class="hd"]/a/span[1]/text()').get()
        actor = li.xpath('.//div[@class="bd"]/p[1]/text()').get().strip()
        score = li.xpath('.//div[@class="star"]/span[2]/text()').get()
        num = li.xpath('.//div[@class="star"]/span[4]/text()').get()
        info = li.xpath('.//div[@class="bd"]/p[2]/span/text()').get()
        print(title, actor, score, num, info)
        with open('豆瓣.csv', mode='a', encoding='utf-8', newline="") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([title, actor, score, num, info])



