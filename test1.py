import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["figure.figsize"]=[12,12]
plt.grid(True)

def dataset(astring="0.1;2.17;3.34;6.121;10.321;14.617;16.801;20.1000;22.1500"):
    lst = np.array(astring.split(';')).astype(np.float)
    x = np.arange(len(lst))
    y = lst
    return x, y
if __name__=="main":
    x,y=dataset()
x, y = dataset("0.1;2.17;3.34;6.121;10.321;14.617;16.801;20.1000;22.1500")
plt.scatter(x, y)
plt.show()