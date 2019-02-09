
import requests as rq
from bs4 import BeautifulSoup

#制定超連結字串
url='https://www.ptt.cc/bbs/Python/index.html'

ptt=rq.get(url)

#檢查狀態,如有響應,使用BeautifulSoup解析
if ptt.status_code==rq.codes.ok:
	soup=BeautifulSoup(ptt.text,'html.parser')
else:
	pass

#找尋標題
title=soup.find_all('div',class_='title')


for i in title:
	print('---------------------------------')
	print('標題:',i.text)
	try:
		print('網址:',i.find('a',href=True)['href'])
	except TypeError:
		pass
	print('---------------------------------')

