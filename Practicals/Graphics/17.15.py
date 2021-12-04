import matplotlib.pyplot as plt

def plotHistogram (data):
    """
    Objective: To plot a histogram
    Input Parameter: data list
    Return Value: None
    """
    plt.hist(data)
    plt.xlabel('value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    #For setting limits of x axis
    plt.xlim (min(data)-1, max(data)+1)
    plt.show()

def main():
    """
    Objective: To plot a histogram based on user input
    Input Parameter: None
    Return value: None
    """
    data = eval (input('Enter data to be plotted as histogram: '))
    plotHistogram (data)

if __name__ == '__main__':
    main()