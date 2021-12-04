import matplotlib.pyplot as plt


def main():
    x = [2,4,6,8,10]
    y = [3,5,7,9,11]

    plt.plot(x, y,'r*--',markersize=10.5,linewidth=2.2)
    plt.axis([1,11,2,12])
    plt.xlabel('X')
    plt.ylabel('X * X')
    plt.title('X vs X * X')
    plt.grid()
    plt.show()