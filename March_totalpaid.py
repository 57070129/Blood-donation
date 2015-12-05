"""Plot Total of paid blood"""
from matplotlib import pyplot
from numpy import arange
def total_paid():
    """Show the total of paid blood graph form data list"""
    label = ['March', 'April', 'May']
    value = [64583, 64756, 61480]
    pos = arange(3)
    pyplot.xticks(pos+0.25,label)
    pyplot.bar(pos,value,width=0.5,color='deeppink')
    pyplot.show()
total_paid()

