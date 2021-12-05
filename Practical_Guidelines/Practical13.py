"""
13. Write a program that makes use of a function to display sine, cosine,
    polynomial and exponential curves.
"""

import matplotlib.pyplot as plt
import math

def sineCurve():
    # y = sin(degree)
    degrees = [x for x in range(0,360+1)]
    y = [math.sin(math.radians(i)) for i in degrees]
    plt.subplot(2,2,1)
    plt.plot(y)
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('y = sin(x)')

def cosineCurve():
    # y = cos(degree)
    degrees = [x for x in range(0,360+1)]
    y = [math.cos(math.radians(i)) for i in degrees]
    plt.subplot(2,2,3)
    plt.plot(y)
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    plt.title('y = cos(x)')

def polynomialCurve():
    # y = x**2
    x = [i for i in range(10+1)]
    y = [i**2 for i in x]
    plt.subplot(2,2,2)
    plt.plot(y)
    plt.xlabel('x')
    plt.ylabel('x^2')
    plt.title('y = x^2')

def exponentialCurve():
    # y = Exp(x)
    x = [i for i in range(10+1)]
    y = [math.exp(i) for i in x]
    plt.subplot(2,2,4)
    plt.plot(y)
    plt.xlabel('x')
    plt.ylabel('exp(x)')
    plt.title('y = exp(x)')

def main():
    """
    Objective: To Plot sine and cosine curves
    Input Parameter: None
    Return Value: None
    """
    sineCurve()
    cosineCurve()
    polynomialCurve()
    exponentialCurve()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()