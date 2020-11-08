#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 19:15:22 2020

@author: Alaisha Naidu
Name: Geodesy Gravity Data ETL
Creds: UCT

"""
#First Order
import pandas as pd 
from pandas import DataFrame
import numpy as np

#Extract
table = pd.read_excel(r'/Users/user/Desktop/DataPoints.xlsx')

list = []

#Transform
for i in range(len(table)):
    new_list =[]
    new_list.append(1)
    new_list.append(table.Longitude__deg_[i])
    new_list.append(table.Latitude__deg_[i])
    new_list.append(table.Longitude__deg_[i]**2)
    new_list.append(table.Longitude__deg_[i]*table.Latitude__deg_[i])
    new_list.append(table.Latitude__deg_[i]**2)
    new_list.append(table.Longitude__deg_[i]**3)
    new_list.append((table.Longitude__deg_[i]**2)*(table.Latitude__deg_[i]))
    new_list.append((table.Longitude__deg_[i])*(table.Latitude__deg_[i]**2))
    new_list.append(table.Latitude__deg_[i]**3)
    list.append(new_list)

A = np.matrix(list)
P = np.identity(500)

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


N = A.T*P*A
n = np.array(N).astype(np.float64) #convert N into a numpy array/matrix from a sympy matrix
NIn = np.linalg.inv(n) #invert N
u = A.T*P*l_sb
x = NIn*u
print(x)

print()

N = A.T*P*A
n = np.array(N).astype(np.float64) #convert N into a numpy array/matrix from a sympy matrix
NIn = np.linalg.inv(n) #invert N
u = A.T*P*l_fa
x = NIn*u
print(x)


