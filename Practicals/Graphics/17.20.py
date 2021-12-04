import matplotlib.pyplot as plt
import math

def sineCurve():
    """
    Objective: To plot sine function
    Input Parameter: None
    Return value: None
    """
    plt.subplot(2,1,1)
    degrees = range(0, 360 + 1)
    sineValues = [math.sin(math.radians (i)) for i in degrees]
    plt.plot(sineValues)
    plt.xlabel ('Degree')
    plt.ylabel('Sine Values')
    plt.title('Sine Curve')
    plt.grid()

def cosineCurve ():
    """
    Objective: To plot cosine function
    Input Parameter: None
    Return Value: None
    """
    plt.subplot(2,1,2)
    degrees = range (0, 360 + 1)
    cosineValues = [math.cos(math.radians (i)) for i in degrees]
    plt.plot(cosineValues)
    plt.xlabel('Degree')
    plt.ylabel ('Cosine Valves')
    plt.title('Cosine Curve')
    plt.grid()

def main():
    """
    Objective: To Plot sine and cosine curves
    Input Parameter: None
    Return Value: None
    """
    sineCurve()
    cosineCurve()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()