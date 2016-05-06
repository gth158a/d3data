import datetime
import requests
# import plotly.plotly as py
import numpy as np
import matplotlib.pyplot as plt

# /repos/:owner/:repo/stats/punch_card
url = 'https://api.github.com/repos/mbostock/d3/stats/commit_activity'
#url = 'https://api.github.com/repos/mbostock/d3/stats/punch_card'

r = requests.get(url)
data = r.json()


week_days = [0,0,0,0,0,0,0]
week_days_text = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
week_total = []
week = []

for w in data:
    week_total.append(w ['total'])
    week.append(w ['week'])
    week_days[0] += w['days'][0]
    week_days[1] += w['days'][1]
    week_days[2] += w['days'][2]
    week_days[3] += w['days'][3]
    week_days[4] += w['days'][4]
    week_days[5] += w['days'][5]
    week_days[6] += w['days'][6]

# print(max(week_total))
index = week_total.index(max(week_total))
# print(week_total.index(max(week_total)))
# print(week[index])
# print(datetime.date(week[index]).isoformat())

print(datetime.datetime.fromtimestamp(week[index]).isocalendar()[0])
print(datetime.datetime.fromtimestamp(week[index]).isocalendar()[1])

week_year = str(datetime.datetime.fromtimestamp(week[index]).isocalendar()[0])\
            + '-' + str(datetime.datetime.fromtimestamp(week[index]).isocalendar()[1])

print("-----------------------------")
print(" The maximum number of commits")
print(" Week: {} - Commits: {}".format(week_year, max(week_total) ))
print("-----------------------------")
print(week_days)
print(max(week_days))
print(week_days_text[week_days.index(max(week_days))])



# date = plt.figure()
#
# x =  week_days_text
# y = week_days
#
# ax = plt.subplot(111)
# ax.bar(x, y, width=10)
#
# plot_url = py.plot_mpl(date, filename='mpl-date-example')