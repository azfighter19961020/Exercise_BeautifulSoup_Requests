import requests as rq
from bs4 import BeautifulSoup as bs
import sys
import pandas as pd
import re

pd.set_option('max_columns',None)

#制定超連結字串
url='https://www.pilio.idv.tw/ltohk/ServerW/list.asp'
lottory=rq.get(url)
lottory.encoding='BIG-5'

if lottory.status_code==rq.codes.ok:
	soup=bs(lottory.text,'html.parser')
else:
	print('website no response')
	sys.exit()

total=soup.find_all('td',style='font-size: 48px; font-weight: bold; color: #000000;border-bottom-style: dotted;\
 border-bottom-color: #CCCCCC; word-break: break-all')

date=soup.find_all('td',style='font-size: 28px; font-weight: bold; color: #000000;border-bottom-style: dotted; border-bottom-color: #CCCCCC')

#存取樂透號碼
x=[]
for i in total:
	x.append(str(i.string))
else:
	number=pd.DataFrame(x)
	number.columns=['樂透號碼']
	for i in range(number.shape[0]):
		number.iloc[i,0]=re.findall('\d+',number.iloc[i,0])
	else:
		pass

#存取日期
y=[]
for i in date:
	y.append(str(i.text))
else:
	date=pd.DataFrame(y)
	date.columns=['日期']

#合併
result=pd.concat([date,number],axis=1)
print(result)

input()