#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Nov  6 10:24:17 2020

@author: Alaisha Naidu
Name: Geodesy Gravity Data ETL 30%
Creds: UCT

"""
#First Order
import pandas as pd 
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

#Extract
table = pd.read_excel(r'/Users/user/Desktop/Geodesy1.xlsx')

list = []
df = table.sample(n=150)
print(df)
df.to_excel("/Users/user/Desktop/150Points.xlsx",
              sheet_name='Sheet_name_1') 
table = pd.read_excel(r'/Users/user/Desktop/150Points.xlsx')

#Plot points

BBox = ((df.Longitude__deg_.min(),   df.Longitude__deg_.max(),      
         df.Latitude__deg_.min(), df.Latitude__deg_.max()))
       
fig,ax = plt.subplots(figsize = [8,7])
ax.scatter(df.Longitude__deg_, df.Latitude__deg_, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title('Plotting Randomly Generated Spatial Data 30%')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])


#Transform
def First_Order(list, table):
    for i in range(len(table)):
        new_list =[]
        new_list.append(1)
        new_list.append(table.Lat_Rad[i])
        new_list.append(table.Long_Rad[i])
        list.append(new_list)

        A = np.matrix(list)
        P = np.identity(150)

        fa_list = []
        sb_list = []

    for i in range(len(table)):
        fa_l = []
        sb_l = []
        fa_l.append(table.Free_Air_Gravity_Anomaly[i])
        sb_l.append(table.Simple_Bouguer_Gravity_Anomaly[i])
        fa_list.append(fa_l)
        sb_list.append(sb_l)
 
        l_sb = np.matrix(sb_list)
        l_fa = np.matrix(fa_list)

    print("First Order Simple Bouger coefficients")
    N = A.T*P*A
    n = np.array(N).astype(np.float64) #convert N into a numpy array/matrix from a sympy matrix
    NIn = np.linalg.inv(n) #invert N
    u = A.T*P*l_sb
    x = NIn*u
    print(x)

    print()
    print("First Order Free Air coefficients")
    N = A.T*P*A
    n = np.array(N).astype(np.float64) #convert N into a numpy array/matrix from a sympy matrix
    NIn = np.linalg.inv(n) #invert N
    u = A.T*P*l_fa
    x = NIn*u
    print(x)
    print()

def Second_Order(list, table):
    for i in range(len(table)):
        new_list =[]
        new_list.append(1)
        new_list.append(table.Lat_Rad[i])
        new_list.append(table.Long_Rad[i])
        new_list.append(table.Lat_Rad[i]**2)
        new_list.append(table.Lat_Rad[i]*table.Long_Rad[i])
        new_list.append(table.Long_Rad[i]**2)
        list.append(new_list)

    A = np.matrix(list)
    P = np.identity(150)

    fa_list = []
    sb_list = []

    for i in range(len(table)):
        fa_l = []
        sb_l = []
        fa_l.append(table.Free_Air_Gravity_Anomaly[i])
        sb_l.append(table.Simple_Bouguer_Gravity_Anomaly[i])
        fa_list.append(fa_l)
        sb_list.append(sb_l)
 
    l_sb = np.matrix(sb_list)
    l_fa = np.matrix(fa_list)


    print("Second Order Simple Bouger coefficients")
    N = A.T*P*A
    n = np.array(N).astype(np.float64) #convert N into a numpy array/matrix from a sympy matrix
    NIn = np.linalg.inv(n) #invert N
    u = A.T*P*l_sb
    x = NIn*u
    print(x)

    print()

    print("Second Order Free Air coefficients")
    N = A.T*P*A
    n = np.array(N).astype(np.float64) #convert N into a numpy array/matrix from a sympy matrix
    NIn = np.linalg.inv(n) #invert N
    u = A.T*P*l_fa
    x = NIn*u
    print(x)
    print()

  

def Third_Order(list, table):
    for i in range(len(table)):
        new_list =[]
        new_list.append(1)
        new_list.append(table.Lat_Rad[i])
        new_list.append(table.Long_Rad[i])
        new_list.append(table.Lat_Rad[i]**2)
        new_list.append(table.Lat_Rad[i]*table.Long_Rad[i])
        new_list.append(table.Long_Rad[i]**2)
        new_list.append(table.Lat_Rad[i]**3)
        new_list.append((table.Lat_Rad[i]**2)*(table.Long_Rad[i]))
        new_list.append((table.Lat_Rad[i])*(table.Long_Rad[i]**2))
        new_list.append(table.Long_Rad[i]**3)
        list.append(new_list)

        A = np.matrix(list)
        P = np.identity(150)

        fa_list = []
        sb_list = []

        for i in range(len(table)):
            fa_l = []
            sb_l = []
            fa_l.append(table.Free_Air_Gravity_Anomaly[i])
            sb_l.append(table.Simple_Bouguer_Gravity_Anomaly[i])
            fa_list.append(fa_l)
            sb_list.append(sb_l)
 
        l_sb = np.matrix(sb_list)
        l_fa = np.matrix(fa_list)

    print("Third order Simple Bouger coefficients")
    N = A.T*P*A
    n = np.array(N).astype(np.float64) #convert N into a numpy array/matrix from a sympy matrix
    NIn = np.linalg.inv(n) #invert N
    u = A.T*P*l_sb
    x = NIn*u
    print(x)

    print()
    print("Third Order Free Air coefficients")
    N = A.T*P*A
    n = np.array(N).astype(np.float64) #convert N into a numpy array/matrix from a sympy matrix
    NIn = np.linalg.inv(n) #invert N
    u = A.T*P*l_fa
    x = NIn*u
    print(x)
    
First_Order(list, table)
list=[]
table = pd.read_excel(r'/Users/user/Desktop/150Points.xlsx')
Second_Order(list, table)
list=[]
table = pd.read_excel(r'/Users/user/Desktop/150Points.xlsx')
Third_Order(list, table)