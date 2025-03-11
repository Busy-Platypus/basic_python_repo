import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(0,10,100)
    y = np.sin(x)
    plt.plot(x,y)
    plt.grid()
    plt.xlabel("Time (s)")
    plt.ylabel("$sin(t)$")
    plt.title("Is this really working ?")
    plt.show()
    return 0


if __name__ == "__main__":
    main()