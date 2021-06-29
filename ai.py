import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib import style
from dateutil import parser as dt_parser
import math
from matplotlib.ticker import ScalarFormatter


def AI(mode, country):
    master = pd.read_csv("master.csv")
    df = master
    style.use('fast')
    dfcy = df.groupby(['country', 'year'], as_index=False).sum()
    mmm = dfcy[dfcy['country'] == country]
    x = mmm['year']
    y = mmm[mode].to_numpy()
    if (mode == "population"):
        label = 'Население'
    else:
        label = 'Суициды'
    plt.xlabel('Год')
    plt.ylabel(label)
    plt.title(f'{label} в стране {country}')
    plt.plot(x, y)
    return plt
