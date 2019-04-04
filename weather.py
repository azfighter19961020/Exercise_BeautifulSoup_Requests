import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

s1=[]
s2=[]
s3=[]
z1=[]
z2=[]
z3=[]
url='https://www.cwb.gov.tw/V7/forecast/taiwan/Taipei_City.htm'

weather=rq.get(url)
weather.encoding='BIG-5'

if weather.status_code==rq.codes.ok:
	soup=BeautifulSoup(weather.text,'html.parser')
else:
	pass

x1=soup.find_all('th')
x2=soup.find_all('th',scope='row')
x3=soup.find_all('td')

for i in x1:
	s1.append(str(i.string))
else:
	pass

for i in x2:
	s2.append(str(i.string))
else:
	pass

for i in x3:
	s3.append(str(i.string))
else:
	pass

total=pd.DataFrame(s2[0:3])

for i in s1[1:5]:
	total[i]=0
else:
	pass

for i in range(0,11,4):
	z1.append(s3[i])
else:
	pass

for i in range(2,11,4):
	z2.append(s3[i])
else:
	pass

for i in range(3,12,4):
	z3.append(s3[i])
else:
	pass


total['溫度 (℃)']=z1
total['舒適度']=z2
total['降雨機率 (%)']=z3
total.drop(columns='天氣狀況',inplace=True)

print(total)
