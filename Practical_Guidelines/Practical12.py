"""
12. Write a program that makes use of a function to accept a list of n integers
    and displays a histogram.
"""
import matplotlib.pyplot as plt


def plot_histogram(data):
    """
    Objective: Plot a histogram.
    Input Parameter: data - a list of n integers
    Return Value: None
    """
    lstbins = [x-0.5 for x in range(0,max(data)+2)]
    plt.hist(data,bins = lstbins)
    plt.title('Histogram')
    plt.xlabel('value')
    plt.ylabel('frequency')
    plt.xlim(min(data)-1,max(data)+1)
    plt.show()


def main():
    n = int(input("Enter the number of elements in the list: "))
    data = []
    for i in range(n):
        data.append(int(input("Enter the value: ")))
    # data = [1,1,2,2,2,2,3,4,4,4,5,5,5,5,5,5,5]
    plot_histogram(data)


if __name__ == '__main__':
    main()
