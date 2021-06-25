import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def AI():
    master = pd.read_csv("master.csv")
    df = master
    print(df[df['country'] == 'Japan'])
    dfcy = df.groupby(['country', 'year'], as_index=True).sum()
    dfcy = df.groupby(['country', 'year'], as_index=False).sum()
    dfcy = df.groupby(['country', 'year'], as_index=False).sum()
    dfj = dfcy[dfcy['country'].isin(
        ['Japan', 'Uzbekistan', 'Russian Federation'])]
    dfj = dfj.set_index(['country', 'year'])
    dfun = dfj.unstack('country')
    newdf = list(dfun)
    newcols = [item for item in newdf if item[0] == 'population']
    dpop = dfun[newcols]
    dpop.plot()
    fig, axv = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
    plt.subplots_adjust(hspace=0.5)
    plt.subplots_adjust(wspace=0.5)
    axv[0][0].set_aspect(aspect='auto')
    axv[1][0].set_aspect(aspect='equal')
    axv[1][1].set_aspect(aspect='equal')
    dpop.plot(ax=axv[0][0])
    fig, axv = plt.subplots(nrows=3, ncols=1, figsize=(20, 20))
    plt.subplots_adjust(hspace=0.7)
    plt.subplots_adjust(wspace=0.5)
    axv[0].set_aspect(aspect='auto')
    axv[1].set_aspect(aspect='auto')
    axv[2].set_aspect(aspect='auto')
    dpop.plot(ax=axv[0])
    dfcl = []
    dfcl.append(dfcy[(dfcy['year'] >= 1980) & (dfcy['year'] < 1990)])
    dfcl.append(dfcy[(dfcy['year'] >= 1990) & (dfcy['year'] < 2000)])
    dfcl.append(dfcy[(dfcy['year'] >= 2000) & (dfcy['year'] < 2010)])
    dfcl.append(dfcy[(dfcy['year'] >= 2010) & (dfcy['year'] < 2020)])
    dfall = []
    for i in range(4):
        dfcymean = dfcl[i].groupby('country', as_index=False).mean()
        dfcymean['suon1'] = \
            dfcymean['suicides_no'].divide(dfcymean['population'],
                                           fill_value=0.0)
        dfcymean['suon1'] = dfcymean['suon1'] * 1e+5
        dfall.append(dfcymean)
    res = pd.concat(dfall, keys=['if1', 'if2', 'if3', 'if4'])
    resv = res.unstack(level=0)
    resv = resv.sort_values(by=[('suon1', 'if4')], ascending=False)
    ax1 = sns.scatterplot(x=('country', 'if4'), y=('suon1', 'if4'),
                          data=resv, ax=axv[1], label="2010-2020")
    sns.scatterplot(x=('country', 'if3'), y=('suon1', 'if3'),
                    data=resv, ax=axv[1], label="2000-2010")
    sns.scatterplot(x=('country', 'if2'), y=('suon1', 'if2'),
                    data=resv, ax=axv[1], label="1990-2000")
    sns.scatterplot(x=('country', 'if1'), y=('suon1', 'if1'),
                    data=resv, ax=axv[1], label="1980-1990")
    for item in ax1.get_xticklabels():
        item.set_rotation(90)
    res = res.sort_values(by='suon1', ascending=False)
    ax2 = sns.lineplot(x='country', y='suon1', data=res,
                       sort=False,
                       ax=axv[2])
    for item in ax2.get_xticklabels():
        item.set_rotation(90)
    return fig


AI()
