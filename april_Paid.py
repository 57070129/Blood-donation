import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
def april_paid():
    labels = 'PublicHospital_bkk', 'PrivateHospital_bkk', 'PublicHospital_country'\
             , 'PrivateHospital_country', 'Activity', 'Service', 'Defective\n'
    sizes = [12530, 14145, 4862, 10923, 1166, 8720,1303]
    colors = ['yellowgreen', 'gold', 'dodgerblue', 'tomato', 'violet'\
              , 'deeppink', 'wheat']
    explode = (0.1, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.show()
april_paid()
