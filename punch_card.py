import datetime
import requests
import matplotlib.pyplot as plt
import numpy as np
import statistics

url = 'https://api.github.com/repos/mbostock/d3/stats/punch_card'

r = requests.get(url)
data = r.json()

#3
week_days = [0,0,0,0,0,0,0]
week_days_text = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
week_total = []
week = []
wednesdays_info = []

for w in data:
    if w[0] == 3:
        wednesdays_info.append(w)


print(wednesdays_info)

hourly = []
number = []
for d in wednesdays_info:
    number.append(d[1])
    hourly.append(d[2])

print(number)
print(hourly)

mean = statistics.mean(hourly)
median = statistics.median(hourly)
print('The mean is {} and the median is {}'. format(mean, median))

N = len(wednesdays_info)
x = np.arange(1, N+1)
y = hourly

labels = number
width = 1
bar1 = plt.bar( x, y, width, color="g" )
plt.ylabel( 'Hourly Commits' )
plt.xticks(x + width/2.0, labels )
plt.show()

