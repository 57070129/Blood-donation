'''Plot Graph'''
import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
def march_get():
    """Show the graph of incoming blood in march."""
    labels = 'FirstDonation', 'GetDonate_inplace', 'GetDonate_outing', 'GetFebruary'
    sizes = [10831, 34975, 34170, 2410]
    colors = ['mediumorchid', 'teal', 'gold', 'indianred']
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.savefig("march_get.png",bbox_inches='tight')
    plt.show()
march_get()
