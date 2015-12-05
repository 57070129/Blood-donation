"""Plot Total of donation blood"""
from matplotlib import pyplot
from numpy import arange
def total_donation():
    """Show the total of donation blood graph form data list"""
    label = ['March', 'April', 'May']
    value = [71555, 57784, 50006]
    pos = arange(3)
    pyplot.xticks(pos+0.25,label)
    pyplot.bar(pos,value,width=0.5,color='mediumblue')
    pyplot.show()
total_donation()
