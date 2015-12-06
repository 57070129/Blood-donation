"""Create graph of paid blood in May"""
import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
def may_paid():
    """Show graph of paid blood in May."""
    labels = 'PrivateHospital_bkk', 'PublicHospital_bkk', 'PrivateHospital_country'\
             , 'PublicHospital_country', 'Defective', 'Activity', 'Service'
    sizes = [12973, 14966, 5363, 11682, 783, 1036, 14677]
    colors = ['gold', 'yellowgreen', 'tomato', 'dodgerblue', 'violet', 'wheat'\
              , 'deeppink']
    explode = (0, 0.1, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.savefig("may_paid.png",bbox_inches='tight')
    plt.show()
may_paid()
