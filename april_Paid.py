"""Create graph of paid blood in April"""
import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
def april_paid():
    """Show graph of paid blood in April."""
    labels = 'PrivateHospital_bkk', 'PublicHospital_bkk', 'PrivateHospital_country'\
             , 'PublicHospital_country', 'Defective', 'Activity', 'Service'
    sizes = [14145, 12530,  10923, 4862,1303, 1166, 8720]
    colors = ['gold', 'yellowgreen', 'tomato', 'dodgerblue', 'violet', 'wheat'\
              , 'deeppink']
    explode = (0.1, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.savefig("april_paid.png",bbox_inches='tight')
    plt.show()
april_paid()
