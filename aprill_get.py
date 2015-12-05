import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
def aprill_get():
    labels = 'FirstDonation', 'GetPlace', 'GetMove', 'GetFebruary'
    sizes = [8511, 30904, 26880, 6972]
    colors = ['mediumorchid', 'teal', 'gold', 'indianred']
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.show()
aprill_get()
