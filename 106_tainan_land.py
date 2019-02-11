import requests as rq
import pandas as pd
import re

pd.set_option('max_columns',None)

url=r'http://data.tainan.gov.tw/dataset/afc35b32-bd5b-40db-a59d-3f4c46c81b60/resource/5e4b936f-332d-47e6-ab97-ac99a8fc6eca/download/tnlandvalue031060202.csv'

original=pd.read_csv(url)
original=original.set_index('行政區')

#處理資料
for i in range(len(original.index)):
	for j in range(len(original.columns)):
		original.iloc[i,j]=re.sub('\D','',str(original.iloc[i,j]))
		if len(original.iloc[i,j])==0:
			original.iloc[i,j]=0
		else:
			pass
	else:
		pass
else:
	for i in original.columns:
		original[i]=original[i].astype('int')
	else:
		pass

#排序:依照一般路線價最高
original=original.sort_values(by='一般路線價最高',ascending=False)
#抓出前五名
top5=original.iloc[:5,:]
print(top5)