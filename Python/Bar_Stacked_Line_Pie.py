import pandas as pd
import pprint
import matplotlib.pyplot as plt
import numpy as np
import datetime

# Read data
postage = pd.read_excel('../data/us-postage.xlsm')
world_pop = pd.read_excel('../data/world-population.xlsm')
obama = pd.read_excel('../data/obama-approval-ratings.xls')
winners = pd.read_excel('../data/hotdog-contest-winners.xlsm')

# Line plot
postage['Year'] = pd.to_datetime(postage['Year'], format='%Y')
plt.plot(postage['Year'], postage['Price'])
plt.xlabel('Year')
plt.ylabel('Price')
plt.title('US Postage Price Over Time')
plt.show()

# Bar chart
plt.bar(world_pop['Year'], world_pop['Population'], align='center', alpha=0.5)
plt.ylabel('Population')
plt.xlabel('Year')
plt.title('World Population Growth')
plt.show()

# Stacked bar
width = 0.35       # the width of the bars: can also be len(x) sequence
N=13
ind = np.arange(N)
plt.rcParams['figure.figsize'] = [15, 15]
p1 = plt.bar(ind, obama['Approve'], width)
p3 = plt.bar(ind, obama['None'], width, bottom=obama['Approve'])
p2 = plt.bar(ind, obama['Disapprove'], width, bottom=obama['Approve'] + obama['None'])
plt.ylabel('Approval')
plt.title('Approval by Issue')
plt.legend((p1[0], p2[0], p3[0]), ('Approve', 'Disapprove', 'None'))
plt.xticks(ind, obama['Issue'])
plt.show()

# Pie
grouped_by = winners.groupby('Country').count()
labels = grouped_by.index.values
sizes = grouped_by['Winner']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()

