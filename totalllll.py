"""Total Donation,Paid and Stock of blood"""
import numpy as np
import matplotlib.pyplot as plt

N = 3
totalDonation = (71555, 57784,50006)
MarchStd = (2, 3, 4)

ind = np.arange(N)  # the x locations for the groups
width = 0.2      # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, totalDonation, width, color='r')

totalPaid = (64583, 64756, 61480)
AprilStd = (3, 5, 2)
rects2 = ax.bar(ind + width, totalPaid, width, color='deepskyblue')

totalStock = (6972, 11107, 2033)
MayStd = (3, 5, 2)
rects3 = ax.bar(ind + width*2, totalStock, width, color='gold')

ax.set_ylim([0, 100000])
ax.margins(0.1)
# add some text for labels, title and axes ticks
ax.set_ylabel('Blood (Unit)')
ax.set_title('The graph of blood donation and paid in 3 mounth')
ax.set_xticks(ind + 0.3)
ax.set_xticklabels(('March', 'April', 'May'))
ax.legend((rects1[0], rects2[0], rects3[0]), ('TotalDonation', 'TotalPaid',\
                                              'TotalStock'))


def autolabel(rects):
    """Put number above graph"""
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.savefig("total.png",bbox_inches='tight')
plt.show()
