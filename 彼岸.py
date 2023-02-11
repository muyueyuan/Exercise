import os
import time
import requests
import concurrent.futures as cf
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


# 目标网站
site = 'http://pic.netbian.com'
# 请求头部
headers = {
    'referer': site,
    'user-agent': UserAgent().random
}
# 图片分类
tags = [
    ['4K风景', '4kfengjing'],
    ['4K美女', '4kmeinv'],
    ['4K游戏', '4kyouxi'],
    ['4K动漫', '4kdongman'],
    ['4K影视', '4kyingshi'],
    ['4K明星', '4kmingxing'],
    ['4K汽车', '4kqiche'],
    ['4K动物', '4kdongwu'],
    ['4K人物', '4krenwu'],
    ['4K美食', '4kmeishi'],
    ['4K宗教', '4kzongjiao'],
    ['4K背景', '4kbeijing']
]


# 保存图片到本地
def save(img_url, img_path):
    resp = requests.get(img_url, headers=headers)
    with open(img_path, 'wb') as f:
        f.write(resp.content)


# 进度条打印
def show(page_num, count, length, runTime):
    fin_per = count/length
    bar_len = 50
    num_fin = round(fin_per*bar_len)
    str_fin = num_fin*'>'
    num_non = bar_len-num_fin
    str_non = num_non*'-'
    process = f'{count:0>{len(str(length))}}/{length}[{str_fin}{str_non}]{fin_per*100:.2f}%|{runTime:.2f}S'
    print(process, end='\r')
    if fin_per == 1.0:
        print()


# 下载一页中的所有图片
def down_page(tag_dir, tag_url, page_num):
    page_dir = os.path.join(tag_dir, str(page_num).zfill(3))
    if not os.path.exists(page_dir):
        os.mkdir(page_dir)
    else:
        pass
    if page_num == 1:
        page_url = tag_url+'/index.html'
    else:
        page_url = tag_url+f'/index_{page_num}.html'
    resp = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(resp.content, 'lxml')
    link_list = soup.select('ul.clearfix>li>a')
    imgs_list = [site+link['href'] for link in link_list]
    for ind, img_link in enumerate(imgs_list):
        resp = requests.get(img_link, headers=headers)
        soup = BeautifulSoup(resp.content, 'lxml')
        img_title = soup.select_one('div.photo-hd>h1').string
        img_path = f'{page_dir}\\{ind+1:0>2} {img_title}.jpg'
        img_url = site+soup.select_one('a#img>img')['src']
        save(img_url, img_path)


# 爬取图片直链并下载
def down(tag_dir, tag_url, page_start, page_end):
    startTime = time.time()
    tp = cf.ProcessPoolExecutor()
    futures = []
    count = 0
    length = page_end-page_start+1
    for page_num in range(page_start, page_end+1):
        future = tp.submit(down_page, tag_dir, tag_url, page_num)
        futures.append(future)
    for future in cf.as_completed(futures):
        count += 1
        endTime = time.time()
        runTime = endTime-startTime
        show(page_num, count, length, runTime)
    tp.shutdown(wait=True)


# 主函数
def main():
    print('彼岸图网4K图片分类为:')
    for ind, key in enumerate(tags):
        print(str(ind).zfill(2), key[0])
    tag_ind = int(input('请选择图片分类的编号: '))
    tag_dir = tags[tag_ind][0]
    if not os.path.exists(tag_dir):
        os.mkdir(tag_dir)
    else:
        pass
    tag_url = site+'/'+tags[tag_ind][1]
    resp = requests.get(tag_url, headers=headers)
    soup = BeautifulSoup(resp.content, 'lxml')
    page_sum = int(soup.select('div.page>a')[-2].string)
    page_start = 1
    page_end = page_sum
    print(f'请图片分类共有页数为: {page_sum}')
    page_start = int(input('请选择下载的起始页数: '))
    page_end = int(input('请选择下载的结束页数: '))
    down(tag_dir, tag_url, page_start, page_end)


if __name__ == "__main__":
    main()
