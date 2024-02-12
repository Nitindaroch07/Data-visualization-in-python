# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:20:30 2023

@author: Nitin
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv(r"C:\Users\Nitin\Downloads\world_population.csv")
pd.set_option('display.max_columns',17)
pd.set_option("display.width",None)
df.columns
df.set_index(['Rank','CCA3'],inplace=True)
df.reset_index(inplace=True)
k=(df.loc[(df['CCA3']=='AFG'),['1970 Population','1980 Population','1990 Population','2000 Population',
                              '2010 Population','2015 Population','2020 Population','2022 Population']])
l=np.array([0,1,2,3,4,5,6,7])
u=(df.loc[(df['CCA3']=='ALB'),['1970 Population','1980 Population','1990 Population','2000 Population',
                              '2010 Population','2015 Population','2020 Population','2022 Population']])
m=k.iloc[0]
u=u.iloc[0]
m=m.astype(int)
o=['1970','1980','1990','2000','2010','2015','2020','2022']


plt.xticks(l,o)
plt.bar(l-0.2,m,width=.4,color='red')
plt.bar(l+0.2,u,width=.4,color='blue')
plt.xlabel('Years',fontsize=20,color='green',labelpad=20)
plt.ylabel('Population',fontsize=20,color='red',labelpad=20)
plt.title("Afghanistan's vs ALB poplulation growth",fontsize=20,pad=40)
plt.grid()
plt.show()

ch='y'
while ch=='y':
    we=input('enter continent name')
    wer=df.loc[(df['Continent']==we)].value_counts()
    print('no of countries  in the (dataset)in ',we,"=",wer.count())
    print('want to continue to get number of countries in other continentsy/n')
    ch=input()

ch='y'
while ch=='y':
    print('enter the countries name u want to compare')
    first=input()
    second=input()
    k=(df.loc[(df['Country']==first),['1970 Population','1980 Population','1990 Population','2000 Population',
                                  '2010 Population','2015 Population','2020 Population','2022 Population']])
    l=np.array([0,1,2,3,4,5,6,7])
    u=(df.loc[(df['Country']==second),['1970 Population','1980 Population','1990 Population','2000 Population',
                                  '2010 Population','2015 Population','2020 Population','2022 Population']])
    m=k.iloc[0]
    u=u.iloc[0]
    m=m.astype(int)
    o=['1970','1980','1990','2000','2010','2015','2020','2022']


    plt.xticks(l,o)
    plt.bar(l-0.2,m,width=.4,color='red')
    plt.bar(l+0.2,u,width=.4,color='blue')
    plt.xlabel('Years',fontsize=20,color='green',labelpad=20)
    plt.ylabel('Population',fontsize=20,color='red',labelpad=20)
 

    plt.grid()
    plt.show()
    ch=input()



