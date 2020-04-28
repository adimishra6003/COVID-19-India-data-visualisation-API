import requests
import pprint
from itertools import count
import matplotlib.pyplot as plt
import seaborn as sns
import math


plt.style.use('ggplot')
url = "https://api.covid19india.org/data.json"

response = requests.request("GET", url)

Dates=count()
x=[]
y=[]

for i in range(len(response.json()['cases_time_series'])):
	y.append(int(response.json()['cases_time_series'][i].get('totalconfirmed')))
	x.append(1+next(Dates))

plt.figure(figsize=(18,6))
ax=plt.subplot(2,1,1)
ax.tick_params(axis='both', which='major', labelsize=8)
ax.tick_params(axis='both', which='minor', labelsize=8)
plt.plot(x, y)
plt.xlabel('Days')
plt.ylabel('Total Confirmed Cases')
plt.tight_layout()


x1=[]
y1=[]

for j in range(len(response.json()['statewise'])):
	if j>=1:
		x1.append(response.json()['statewise'][j].get('state')[0:4])
		y1.append(int(response.json()['statewise'][j].get('confirmed')))

list.reverse(x1)
list.reverse(y1)
ax1=plt.subplot(2,1,2)
ax1.tick_params(axis='both', which='major', labelsize=8)
ax1.tick_params(axis='both', which='minor', labelsize=4)
plt.bar(x1, y1, align='center')
plt.xlabel('States')
plt.ylabel('Confirmed Cases')
plt.tight_layout()
plt.show()