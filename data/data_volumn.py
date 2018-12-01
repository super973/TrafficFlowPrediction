# -*- coding: utf-8 -*-
__Author__ = 'zhangbaojun'
__Time__ = '2018/6/6 14:00'
__File__ = 'data_volumn.py'

import pandas as pd

# time='DTCOLLECTTIME'
# volumn = 'SUM(D.NVOLUME)'
data = 'D:/Hisense/TrafficFlowPrediction/data/100211gaizao.csv'
df1 = pd.read_csv(data, encoding='utf-8', header=None, ).fillna(0)
df1.columns = ['time', 'volumn']
a = []
b=[]
# print(df1['time'].values[0][0:9])

for i in range(0, len(df1)):
    if df1['time'].values[i][0:9] == '2018/1/20' or df1['time'].values[i][0:9] == '2018/1/21'\
            or df1['time'].values[i][0:9] == '2018/1/27'or df1['time'].values[i][0:9] == '2018/1/28'\
            or df1['time'].values[i][0:8] == '2018/2/3'or df1['time'].values[i][0:8] == '2018/2/4'\
            or df1['time'].values[i][0:9] == '2018/2/10'or df1['time'].values[i][0:9] == '2018/2/15'\
            or df1['time'].values[i][0:9] == '2018/2/16'or df1['time'].values[i][0:9] == '2018/2/17'\
            or df1['time'].values[i][0:9] == '2018/2/18'or df1['time'].values[i][0:9] == '2018/2/19'\
            or df1['time'].values[i][0:9] == '2018/2/20'or df1['time'].values[i][0:9] == '2018/2/21'\
            or df1['time'].values[i][0:9] == '2018/2/25'\
            or df1['time'].values[i][0:8] == '2018/3/3'or df1['time'].values[i][0:8] == '2018/3/4'\
            or df1['time'].values[i][0:9] == '2018/3/10'or df1['time'].values[i][0:9] == '2018/3/11'\
            or df1['time'].values[i][0:9] == '2018/3/17'or df1['time'].values[i][0:9] == '2018/3/18'\
            or df1['time'].values[i][0:9] == '2018/3/24'or df1['time'].values[i][0:9] == '2018/3/25'\
            or df1['time'].values[i][0:9] == '2018/3/31'or df1['time'].values[i][0:8] == '2018/4/1'\
            or df1['time'].values[i][0:8] == '2018/4/5'or df1['time'].values[i][0:8] == '2018/4/6'\
            or df1['time'].values[i][0:8] == '2018/4/7'or df1['time'].values[i][0:9] == '2018/4/14'\
            or df1['time'].values[i][0:9] == '2018/4/15'or df1['time'].values[i][0:9] == '2018/4/21'\
            or df1['time'].values[i][0:9] == '2018/4/22'or df1['time'].values[i][0:9] == '2018/4/29'\
            or df1['time'].values[i][0:9] == '2018/4/28'or df1['time'].values[i][0:9] == '2018/4/30'\
            or df1['time'].values[i][0:8] == '2018/5/1'or df1['time'].values[i][0:8] == '2018/5/5'\
            or df1['time'].values[i][0:9] == '2018/5/6':
        a.append([df1['time'].values[i],df1['volumn'].values[i]])
zhoumo=pd.DataFrame(a)
zhoumo.to_csv('100211_jiejiari.csv',index=None)

for i in range(0, len(df1)):
    if  df1['time'].values[i][0:9] != '2018/1/20' and df1['time'].values[i][0:9] != '2018/1/21'\
            and df1['time'].values[i][0:9] != '2018/1/27'or df1['time'].values[i][0:9] != '2018/1/28'\
            and df1['time'].values[i][0:8] != '2018/2/3'or df1['time'].values[i][0:8] != '2018/2/4'\
            and df1['time'].values[i][0:9] != '2018/2/10'or df1['time'].values[i][0:9] != '2018/2/15'\
            and df1['time'].values[i][0:9] != '2018/2/16'or df1['time'].values[i][0:9] != '2018/2/17'\
            and df1['time'].values[i][0:9] != '2018/2/18'or df1['time'].values[i][0:9] != '2018/2/19'\
            and df1['time'].values[i][0:9] != '2018/2/20'or df1['time'].values[i][0:9] != '2018/2/21'\
            and df1['time'].values[i][0:9] != '2018/2/25'\
            and df1['time'].values[i][0:8] != '2018/3/3'and df1['time'].values[i][0:8] != '2018/3/4'\
            and df1['time'].values[i][0:9] != '2018/3/10'and df1['time'].values[i][0:9] != '2018/3/11'\
            and df1['time'].values[i][0:9] != '2018/3/17'and df1['time'].values[i][0:9] != '2018/3/18'\
            and df1['time'].values[i][0:9] != '2018/3/24'and df1['time'].values[i][0:9] != '2018/3/25'\
            and df1['time'].values[i][0:9] != '2018/3/31'and df1['time'].values[i][0:8] != '2018/4/1'\
            and df1['time'].values[i][0:8] != '2018/4/5'and df1['time'].values[i][0:8] != '2018/4/6'\
            and df1['time'].values[i][0:8] != '2018/4/7'and df1['time'].values[i][0:9] != '2018/4/14'\
            and df1['time'].values[i][0:9] != '2018/4/15'and df1['time'].values[i][0:9] != '2018/4/21'\
            and df1['time'].values[i][0:9] != '2018/4/22'and df1['time'].values[i][0:9] != '2018/4/29'\
            and df1['time'].values[i][0:9] != '2018/4/28'and df1['time'].values[i][0:9] != '2018/4/30'\
            and df1['time'].values[i][0:8] != '2018/5/1'and df1['time'].values[i][0:8] != '2018/5/5'\
            and df1['time'].values[i][0:9] != '2018/5/6':
        b.append([df1['time'].values[i],df1['volumn'].values[i]])
zhoumo=pd.DataFrame(b)
zhoumo.to_csv('100211_gongzuori.csv',index=None)


# print(a)
# print(df1['time'].values[0])
