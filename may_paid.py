import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
def may_paid():
    labels = 'PublicHospital_bkk', 'PrivateHospital_bkk', 'PublicHospital_country'\
             , 'PrivateHospital_country', 'Activity', 'Service', 'Defective\n'
    sizes = [14966, 12973, 11682, 5363, 1036, 14677, 783]
    colors = ['yellowgreen', 'gold', 'dodgerblue', 'tomato', 'violet'\
              , 'deeppink', 'wheat']
    explode = (0.1, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.show()
may_paid()
