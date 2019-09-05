#包运行的一个注意事项
#小贴士
def rcscore():
 	a = 1
 	b = 2
 	c = 3
 	def inner():
 		score = a+b+c
 		print(score)
 	return inner
rcscore()()
#总共要运行两次不然结果为空

#-----------------------------------
#文件的复制思路
f1 = open('text.txt','r')
f2 = open('text2.txt','w')

content = f1.read()
# print(content)
f2.write(content)

f1.close
f2.close

#-----------------------------------
#对文件的一些操作

import os

os.remove('text2.txt')

os.mkdir('Python2')

os.rmdir('Python2')

os.removedirs('Python2/one')#两个文件夹同时删除

os.rmdir('Python2/one')#只删除最后一个文件
#获取当前目录
print(os.getcwd())

#设置默认目录
os.chdir('Python2')
print(os.getcwd())

#遍历当前目录列表(一个电视当前目录，两个点是上一级目录)
print(os.listdir('./'))

#-----------------------------------
爬虫正则学习(简化版)
import requests
import re
import json
# url = 'https://movie.douban.com/chart'
# def get_one_page(url):
# response = requests.get(url)
# print(response.text)
# html = response.text

html = '<html> \
 <body> \
 <h1 id="title">Hello World</h1> \
 <a href="#" class="link">This is link1</a> \
 <a href="# link2" class="link">This is link2</a> \
 <a target="_blank" class="linkto" href="http://new.qq.com/omn/\
 NEW2018042200486400">蓝图绘就梦想——《河北雄安新区规划纲要》发布</a>\
 </body> \
 </html>'


# pattern = re.compile('<div class="p12">.*?href="(.*?")".*?class>"(.*?)"</div>',re.S)
pattern = re.compile('<body>.*?title">(.*?)</h1>.*?#".*?>(.*?)</a>\
.*?link2".*?>(.*?)</a>.*?_blank.*?">(.*?)</a>.*?</body>')
items = re.findall(pattern,html)
infos = []
for item in items:
	# yield {
	# 	'link1': item[0],
	# 	'link2': item[1],
	# 	'title': item[2]
 # 	}
 	for ite in item:
 		infos.append(ite)
	
# print(infos)
dict = {}
dict['hello'] = infos[0]
dict['link1'] = infos[1]
dict['link2'] = infos[2]
dict['title'] = infos[3]
print(dict)

with open('result.txt','w',encoding = 'utf-8') as f:
	res = json.dumps(dict,ensure_ascii = False)
	f.write(res)
	
#-----------------------------------
import requests
import re
import json
from bs4 import BeautifulSoup
url = 'https://movie.douban.com/j/\
search_subjects?type=tv&tag=\
%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=40'
content = requests.get(url)
# print(content.text)
html = content.text
soup = BeautifulSoup(html,'html.parser')
# print(soup.text)
#json 类文件提取方法
js = json.loads(soup.text)
print(js['subjects'][0])

#-----------------------------------
#requests正则表达式模板
import requests
from requests.exceptions import RequestException
import re
import json
def get_one_page(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def parser_one_page(html):
	pattern = re.compile('')
	items = re.findall(pattern,html)
	for item in items:
		yield {
			'index': item[0],
			'image': item[1],
			'title': item[2],
			'actor': item[3].strip()[3:],
			'time': item[4].strip()[5:],
			'score': item[5] + item[6]
		}

def write_to_file(content):
	with open('result','a',encoding = 'utf-8') as f:
		f.write(json.dumps(content,ensure_acsii = False) + '\n')
		f.close()

def main(offset):
	url = '.*?offset=' + str(offset)
	html = get_one_page(url)
	for item in parser_one_page(html):
		print(item)
		write_to_file(item)


if __name__ == '__main__':
	for i in range(10):
		main(i*10)

#-----------------------------------

import requests
import re
import json
from bs4 import BeautifulSoup
url = 'https://movie.douban.com/chart'
content = requests.get(url)
html = content.text
# print(content.text)

# pattern = re.compile('<div.*?p12">.*?pl">"(.*?)"</p>.*?</div>',re.S)
# result = re.findall(pattern,html)
# print(result)
soup = BeautifulSoup(html,'html.parser')
title = soup.select('.p12')
print(title)
#-----------------------------------
#beautiful soup 运用案例，成功爬取豆瓣最新电影
import requests
import re
import json
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
def get_one_page(url):
	try:
		content = requests.get(url)
		if content.status_code == 200:
			return content.text
		return None
	except RequestException:
		return None
	

def parser_one_movie(html,num):
	soup = BeautifulSoup(html,'html.parser')
	result = soup.select(".item")[num]
	#提取电影名
	title = result.select('.nbg')[0]
	# print(title['title'])
	#提取演员
	actor = result.select('.pl')[0].get_text()
	# print('演员：' + actor)
	#根据span标签提出span相关的内容
	comment = result.select('span')[3].get_text()
	# print("评价人数：" + comment)
	rating_nums = result.select('.rating_nums')[0].get_text()
	# print('豆瓣评分：' + rating_nums)
	# print(result)
	return {
		'电影': title['title'],
		'演员': actor,
		'评论人数': comment,
		'豆瓣评分': rating_nums
	}


def write_to_file(res):
	with open("New_movies.txt",'a',encoding = 'utf-8') as f:
		f.write(json.dumps(res,ensure_ascii = False) + '\n')
		f.close

def main():
	url = 'https://movie.douban.com/chart'
	html = get_one_page(url)
	for i in range(10):
		res = parser_one_movie(html,i)
		print(res)
		write_to_file(res)


if __name__ == '__main__':
	main()

#-----------------------------------
scrapy使用小攻略：
#浏览网页时要使用的代理
'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
#创建一个爬虫文件scrapy genspider myspeider douban.com
#在scrapy中想要将匹配对象转换为unicode使用extract()
#运行爬虫使用scrapy crawl + name
#运行爬虫存入一个文档格式可以使用scrapy crawl + name + -o + forkname.json

# 进行首个scrapy框架实验
https://www.douban.com/  
# define the fields for your item here like:
    # name = scrapy.Field()
    name = 'dbSpeider'
    allowd_domains = ['https://www.douban.com/']
    start_urls = ['https://movie.douban.com/tv/#']
    # pass
    #运行爬虫使用scrapy crawl + name
	def parse(self,reponse):
		with open('douban.html','wb') as f:
			f.write(reponse.body)


#-----------------------------------

#第一多个scrapy项目总结（关于搜狗小说）
1.首先创建scrapy项目使用，scrapy startproject + 项目名
（不是URL，是URL的话做callback的时候不能跳转下一页）
2.配置item文件，写入你需要爬取的字段
3.配置设置，可以先提前打开pipeline（后面要用到）
然后就是使用代理：
'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
不然不能进入网站，会被屏蔽
百度代理：'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.10 Safari/537.36'
4.就可以cd到spiders文件夹下，使用scrapy genspider myspeider douban.com
（这里的douban.com不是URL，是URL的话做callback的时候不能采集下一页）
创建一个新的爬虫（算是核心）负责请求URL，处理想要提取的东西
5.循环后要调用爬虫项目中的item文件，但是有时候不能直接导入模块，这时
我们可以导入一个sys模块进行处理：
import sys
sys.path.append(r'C:\Users\lg\Desktop\Python\dbSpider')
这里使用yield弄成一个生成器一个一个返回：
yield item
6.如果有多个URL需要请求的话，可以在start_url[],里面直接添加，但是那样子太
孬了，要提取大量数据的话要写很多，很难看，也那难写；所以在这里我们可以使
用一个递归函数：
yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
（关灯了，今天就写到此处）

#-----------------------------------

xpath使用小贴士!!!
from lxml import etree
import requests
response = requests.get(url)
html = response.text
content = etree.HTML(html)
links = content.xpath('//*[@class="book-img-text"]//li')
#此处用了@href获取的是标签内的属性，如不在标签内则在后面加入/text()
for link in links:
    href = link.xpath('./div[2]/h4/a/@href')[0]
    print(href)
novel_name = content.xpath('/html/body/div[2]/div[6]/div[1]//h1/em/text()')[0]

#-----------------------------------

关于以下解决编译字符串问题解决方案：
# 'gbk' codec can't decode byte 0x80 in position 40: illegal multibyte sequence
import codecs
with open('test.json','r',encoding='utf-8') as f:

#-----------------------------------
pygal作条形图
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#简单型
mystyle = LS('#333366',base_style = LCS)
chart = pygal.Bar(style = mystyle,x_label_rotation = 45,show_legend = False)
chart.title = 'QiDian Novel Rank Top 50'
chart.x_labels = names
chart.add('',yuepiao)
chart.render_to_file('NovelTop50.svg')
#复杂型
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.title_font_size = 24
my_config.lable_font_size = 20
my_config.show_legend= False
my_config.major_label_font_size = 18
my_config.tuncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(my_config,style=my_style)
chart.title = "QiDian Novel Rank Top 50" 
chart.x_labels = names
chart.add('',yuepiao)
chart.render_to_file('NovelTop50.svg')


# 该方式注意使用 int() 将数据变量变成整数不然会报错

#-----------------------------------
#导入json文件作图时，注意事项
import json
import codecs
with open('test.json',encoding='utf-8') as f:
	novel_list = []
	for line in f.readlines():
		# print(line.strip())
		novel_dict = json.loads(line.strip())
		novel_list.append(novel_dict)
print(novel_list[:2])
for data in novel_list[:2]:
	novel_name = data['monthCount']
	# print(novel_name)
#要首先存入一个列表才能遍历出来

#-----------------------------------
处理：UnicodeEncodeError: 'gbk' codec can't encode character '\
xd6' in position 102: illegal multibyte sequence'错误
import requests
import codecs
url = 'http://www.youth.cn/'
response = requests.get(url)
response.encoding = 'gbk'
print(response.text)

#-----------------------------------
#MongoDB使用方法1：
MONGO_URL = 'localhost'
MONGO_DB = 'qidian'
MONGO_TABLE = 'novelRank'

import pymongo
from config import *
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def save_to_mongo(result):
	try:
		if db[MONGO_TABLE].insert(result):
			print('存储到MongoDB成功..',result)
	except Exception:
		print('存储到MongoDB成功..',result)

#调用函数
save_to_mongo(result)
#MongoDB使用方法2：（scrapy中的使用方法）
MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DBNAME = "Qidian"
MONGODB_SHEETNAME = "QidianNovel"

import pymongo
from scrapy.conf import settings

class QidianPipeline(object):
	def __init__(self):
		host = settings['MONGODB_HOST']
		port = settings['MONGODB_PORT']
		dbname = settings['MONGODB_DBNAME']
		sheetname = settings['MONGODB_SHEETNAME']
		# 创建数据库连接
		client = pymongo.MongoClient(host = host,port = port)
		# 指定数据库
		mydb = client[dbname]
		# 存放数据的数据库表明
		self.sheet = mydb['sheetname']

	def process_item(self, item, spider):
		result = dict(item)
		self.sheet.insert(result)
		return item

#-----------------------------------
MongoDB命令：
>D:/MongoDB/bin/mongo.exe
# 查看当前数据库
>db
# 查看所有数据库
>show dbs
# 连接到dbname数据库
>use dbname
# 查看当前数据库下的所有表
>show collections
# 查看表中的所有数据
>db.tablename.find()
# 删除当前所在数据库
>db.dropDatabase()
#导出数据库文件
# >D:\MongoDB\bin
# mongoexport -d 数据库名 -c 表名 -o  C:\Users/
# \lg\Desktop\ python\输出文件名  --type json/csv -f field （CSV文件特别声明）
（不是在mongo.exe下运行）（特别注意：大小写问题）
#-----------------------------------
import json
import codecs
import re
with open('dylive.json',encoding = 'utf-8') as f:
	dylive_list = []
	for line in f.readlines():
		live_dict = json.loads(line.strip())
		dylive_list.append(live_dict)
# title = content['title']
# enrages = content['enrages'].replace('万','0000')
# print(enrages)
		# print(live_dict['enrages'])

lives = '20万'
pattern = re.compile(r'\D')
item = re.findall(pattern,lives)
x = lives.replace('万','0000')
print(x)

#-----------------------------------
# 当抓取的网页文件类型是json时，解析方式：
import json
import requests
response = requests.get(url)
html = response.content.decode()
content = json.loads(html)
infos = content['data']['rl']

#-----------------------------------

with open('novel_rank.json',encoding='utf-8') as f:
	novel_list = []
	for line in f.readlines():
		# print(line.strip())
		novel_dict = json.loads(line.strip())
		novel_list.append(novel_dict)
#-----------------------------------
#将json文件读取出来
import json
# filenames = ['wyjj.json','djry.json','syxx.json','yltd.json','kjjy.json','yyzb.json']
# for filename in filenames:
filename = 'znl.json'
with open(filename,encoding = 'utf-8') as f:
	anchor_list = []
	for line in f.readlines():
		anchor_dict = json.loads(line.strip())
		anchor_list.append(anchor_dict)

# print(anchor_list)

enrages = []
for list in anchor_list:
	enrages.append(list['人气'])

	# print(list)
enrages[0] = '21000'
# print(enrages)
number = 0
enrag = 0
for enrage in enrages:
	enrag += int(enrage)
	number += 1

print('{} {}'.format(str(enrag),str(number))) 

#-----------------------------------
#模拟输入框
from selenium.webdriver.common.keys import Keys
input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
input.send_keys('')
input.send_keys(Keys.RETURN)
#选取可点击的点
submit = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
submit.click()
#-----------------------------------
from pyquery import PyQuery as pq
html = brower.page_source
doc = pq(html)
items = doc('#mainsrp-itemlist .items .item').items()
count = 0
for item in items.items():
	product = {
		# 'image':item.find('.pic .img').attr('stc'),
		# 'price':item.find('.price').text(),
		# 'deal':item.find('.deal-cnt').text()[0:-3],
		# 'title':item.find('.title').text(),
		'shop':item.find('.shopname').text(),
		'location':item.find('.location').text()
	}
	count +=1
	print(product)
#-----------------------------------
import requests
from pyquery import PyQuery as pq
url = 'http://lol.qq.com/webplat/info/news_version3/152/4579/m5583/list_1.shtml'
response = requests.get(url)
response.encoding = 'gbk'
html = response.text
# print(html)
doc = pq(html)
items = doc('.layout .newslistbox .news-lst').items()
for item in items.items():#记住这里是。items()
#     tag = item.find('.lnk-type').text()
    title = item.find('a').text()
    time = item.find('.date').text()
    print(title,time)
    
#-----------------------------------

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
brower = webdriver.Chrome()
wait = WebDriverWait(brower, 10)
def skim():
	try:
		brower.get('https://www.douyu.com/directory/all')
		page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#J-pager > a:nth-child(11)")))
		return page.text
	except TimeoutException:
		skim()
def brower_next(page):
	try:
		cautious = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#J-pager > input")))
		submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J-pager > a.shark-pager-submit')))
		cautious.send_keys(page)
		submit.click()
		wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#J-pager > a.shark-pager-item.current"),str(page)))
		parse_one_page()
	except TimeoutException:
		brower_next()
def parse_one_page():
	wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#live-list-content #live-list-contentbox li")))
	html = brower.page_source
	doc = pq(html)
	items = doc('#live-list-content #live-list-contentbox li').items()
	count = 0
	for item in items:
	    anchor = {
	        'title':item.find('.play-list-link').attr('title'),
	        'name': item.find('.dy-name').text(),
	        'num':item.find('.dy-num').text()
	        }
	    print(anchor)
	    count += 1
	print(count)

def main():
	try:
		page = skim()
		for i in range(1,5):
			time.sleep(1)
			brower_next(i)
		# time.sleep(5)
	finally:
		brower.quit()

if __name__ == '__main__':
	main()

#-----------------------------------
#Numpy使用小贴士
# import sys
# from datetime import datetime
import numpy as np

def numpysum(n):
	a = np.arange(n) ** 2
	b = np.arange(n) ** 3
	c = a + b
	return c

# def pythonsum(n):
# 	a = range(n)
# 	b = range(n)
# 	c = []
# 	for i in range(len(a)):
# 		a[i] = i ** 2
# 		b[i] = i ** 3
# 		c.append(a[i] + b[i])
# 	return c

n = 1000
# start = datetime.now()
c = numpysum(n)
# s = datetime.now() - start
# print(c[-2:])
# print(s.microseconds)

# c = pythonsum(n)
# s = datetime.now() - start
# print(c[-2:])
# print(s.microseconds)





# a = np.arange(5)
# print(a)


#-----------------------------------
#计算运行的速度
# import sys
# from datetime import datetime

# start = datetime.now()
# date = datetime.now() - start
# print(date)
# a = range(5)
# print(len(a))
a = []
a[1] = 1
print(a)

#-----------------------------------
#pymysql使用小贴士！！！
import pymysql

#打开数据库连接
db = pymysql.connect('localhost','root','lg083533','student')
#创建游标对象
cursor = db.cursor()

#查询数据库中的数据
# sql = 'select * from stu'
# try:
# 	cursor.execute(sql)
# 	#提取第一行
# 	# student = cursor.fetchone()
# 	#提取所有行
# 	students = cursor.fetchall()
# 	for student in students:
# 		# print(type(student))
# 		print(student)
# except Exception as ex:
# 	print(ex)

#插入一条记录
# sql = 'insert into stu values (%s,%s,%s,%s)'
# try:
# 	cursor.execute(sql,('陈德凤','20150108020129','15285381046','贵州'))
# 	db.commit()

# except Exception as ex:
# 	db.rollback()
# 	print(ex)

# 条件查询
sql = 'select * from stu where 年龄 >= %s'
try:
	cursor.execute(sql,(20))
	students = cursor.fetchall()
	for student in students:
		stu_num = {
			'name':student[0],
			'sc_num':student[1],
			'age':student[2],
			'tel':student[3],
			'address':student[4]}
		print(stu_num)
except Exception as ex:
	print(ex)



cursor.close
db.close

#-----------------------------------
#将爬虫数据写入csv
import requests
import re
import json
import csv
import codecs
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
def get_one_page(url):
	try:
		content = requests.get(url)
		if content.status_code == 200:
			return content.text
		return None
	except RequestException:
		return None
	

def parser_one_movie(html):
	soup = BeautifulSoup(html,'html.parser')
	results = soup.select(".item")
	itemlist = []
	for result in results:
		title = result.select('.nbg')[0]
		actor = result.select('.pl')[0].get_text()
		comment = result.select('.pl')[1].get_text()
		comment = int(re.compile('(\d+)').search(comment).group(1))
		rating_nums = result.select('.rating_nums')[0].get_text()
		rating_nums = float(rating_nums)
		# movies = {
		# 	'电影': title['title'],
		# 	# '演员': actor,
		# 	'评论人数': comment,
		# 	'豆瓣评分': float(rating_nums)
		# }

		list = [title['title'],comment,rating_nums]
		itemlist.append(list)
	#会返回一个提取完整的列表
	return itemlist


def write_to_csv(itemlist):
	#不加newline会多出一个空行，不能用encoding，不然会导致乱码
	with open('set1.csv','w+',newline = '') as f:
		writer = csv.writer(f)
		writer.writerow(['电影','评论人数','豆瓣评分'])
		for item in itemlist:
			# print(item)
			writer.writerow(item)

def main():
	url = 'https://movie.douban.com/chart'
	html = get_one_page(url)
	list = parser_one_movie(html)
	write_to_csv(list)

if __name__ == '__main__':
	main()
#-----------------------------------
#使用python配置Chrome文件
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=C:/Users/lg/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('www.baidu.com')
#-----------------------------------
#切换窗口
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
import time
brower = webdriver.Chrome()
brower.maximize_window()
brower.get('http://news.baidu.com/')
wait = WebDriverWait(brower, 10)
submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#pane-news > div > ul > li.hdline0 > strong > a')))
submit.click()
print('当前窗口句柄：',brower.current_window_handle)
handles = brower.window_handles
print('所有句柄：',handles)
for handle in handles:
	if handle != brower.current_window_handle:
		print('switch to second window:',handle)
		brower.close()
		brower.switch_to.window(handle)


#-----------------------------------
# python正则表达式匹配小数
re.compile('(\d+\.\d)').search(hot).group(1)

#-----------------------------------
#微信小东西（不完全版）
import os
import itchat
# def outer():
#     global filename
#     filename = 'ligamng'
#     # def inner():
#     #     name = filename + 'zuishuai!'
#     #     print(name)
#     # return inner

# def hanhsu():
#     print(filename)

# def main():
#     # c = outer()
#     # c()
#     outer()
#     hanhsu()

# if __name__ == '__main__':
#     main()

# msg = '2'
# list = ['1','2']
# if msg in list:
#     print(msg)
# else:
#     print('0')

# def send_files():
# global CurDirs
# message = '测试.txt'
# dir = r'C:\Users\lg\desktop'
# os.chdir(dir)
# CurDirs = os.listdir('./')
# for curdir in CurDirs:
#     # itchat.send(curdir,'filehelper')
#     print(curdir)
# if message in CurDirs:
#     # print('接收：',message)
#     print(str(dir) + '\ ' + message)
# #     # itchat.send_file(str(dir) + str(message),'filehelper')

# # send_files()

# from os import path

# d = path.dirname(__file__)
# print(d)

# text_path = 'txt/lz.txt' #设置要分析的文本路径
# x = path.join(dir, text_path)
# print(x)

import itchat

sendMsg = u"{消息助手}：暂时无法回复"
usageMsg = u"使用方法：\n1.运行CMD命令：cmd\n" \
           u"关机命令:cmd shutdown -s -t 0 \n" \
           u"重启命令:cmd shutdown -r -t 0 \n" \
           u"2.获取当前电脑用户：cap\n"\
           u"3.截取当前屏幕：shot\n"

@itchat.msg_register('Text')      
def main(msg):
    global message
    global fromName
    global toName
    message = msg['Text']
    fromName = msg['FromUserName']
    toName = msg['ToUserName']
    if toName == "filehelper":
        print('消息内容：',message)
        if message == '1':
            print('正在发送文件...')
            itchat.send('妈的怎么发送不了文件','filehelper')
            itchat.send_file('set2.py','filehelper')
            print('发送超时！')
        else:
            print('文件发送失败！')
        if message == '2':
            sendToOther()

def sendToOther():
    user_info = itchat.search_friends(name='老七也气鼓鼓')
    if len(user_info) > 0:
        # 拿到用户名
        user_name = user_info[0]['UserName']
        print(user_name)
        # 发送文字信息
        itchat.send_msg('宝宝你好啊！(通过程序给你发送了一条消息)', user_name)
        # itchat.send_image('cat.jpg', user_name)
        # itchat.send_file('19_2.py', user_name)
        # itchat.send_video('sport.mp4', user_name)


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.send(usageMsg, "filehelper")
    itchat.run()



















