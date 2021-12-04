import matplotlib.pyplot as plt

def plotPiechart(data, labels):
    """
    Objective: To plot a pie chart
    Input Parameters: data, labels - list
    Return Value: None
    """
    plt.pie(data, labels=labels, autopct='%.2f')
    plt.title('Pie Chart')
    plt.show()

def main():
    """
    Objective: To plot pie chart based on user input
    Input Parameter: None
    Return value: None
    """
    data = eval(input('Enter data to be plotted as pie chart: '))
    labels = eval(input('Enter the labels: '))
    plotPiechart(data, labels)

if __name__ == '__main__':
    main()