import matplotlib.pyplot as plt

plt.figure(1)
plt.plot([1,2,3,5,8,10], [200,300,353,412,456,734], color='green', label='legend')
plt.ylabel('Latency (in ms)')
plt.xlabel('No. of clients')
plt.legend(loc='lower right')
plt.title('Performance Analysis')
plt.savefig('plot1.png')
plt.figure(2)
data = [50, 100, 28, 56, 230, 80]
tot = sum(data)
plt.pie(data, labels=['A','B','C','D','E', 'F'],
        autopct = lambda p: '{:.0f}'.format(p*tot/100))
plt.ylabel('Time Spent (in ms)')
plt.xlabel('Activity')
plt.title('Data Analysis')
# plt.show()
plt.savefig('plot2.png')
