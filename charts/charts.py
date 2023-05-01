import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 32, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    #plt.show()
    plt.savefig('torta.png')
    plt.close()




