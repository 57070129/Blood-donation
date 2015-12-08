'''Plot Graph'''
import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
def may_get():
    """Show the graph of incoming blood in may."""
    labels = 'FirstDonation', 'GetPlace', 'GetMove', 'GetFebruary'
    sizes = [6571, 24377, 25692, 13507]
    colors = ['mediumorchid', 'teal', 'gold', 'indianred']
    explode = (0, 0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.savefig("may_get.png",bbox_inches='tight')
    plt.show()
may_get()
