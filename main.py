# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
