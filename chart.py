from transactions import net_worth_by_day

import matplotlib.pyplot as plt


x = list(net_worth_by_day.keys())[::3]
y = list(net_worth_by_day.values())[::3]

plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=5)
plt.xlabel('Date')
plt.ylabel('Canadian net worth in millions')

plt.xticks(ticks=range(len(x)), rotation=90, size=5)
plt.yticks(size=12)

plt.title('Net Worth By Day!')

plt.savefig('net_worth_chart.jpg')
