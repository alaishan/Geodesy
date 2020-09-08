#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:55:08 2020

@author: Alaisha Naidu
Name: Geodetic Coords to Curvilinear 
Creds: University of Cape Town
"""


import math
from math import sqrt, pi, atan, sin, cos
import numpy as np
from numpy import matmul
import sympy as sp
from sympy import Matrix, symbols, atan, sqrt

#WGS84 to Local
X1 = sp.Matrix([[5384125.138],[3402602.734],[-377241.673]])
x01 = sp.Matrix([[162.3],[14.5],[308.4]])
K1 = 1.000001
Rot1 = sp.Matrix([[1,-0.000000198773609,0.000001139312],[0.000000198773609,1,-0.000001677455],[-0.000001139312,0.000001677455,1]])

X = np.array(X1).astype(np.float64)
x0 = np.array(x01).astype(np.float64)
K = np.array(K1).astype(np.float64)
Rot = np.array(Rot1).astype(np.float64)
#Geodetic to Local Datum
B = np.matmul(Rot,X)
x = x0 + K*B
print(x)
print("")
#Local to Curvilinear
u = x[0]
v = x[1]
w = x[2]
f = (1/293.46)
a = 6378249.14 
e2 = 2*f - (f*f)

p = math.sqrt((u*u)+(v*v))
r = math.sqrt((p*p)+(w*w))
fir = (w*(1-f))/p
sec = 1+((e2*a)/(r*(1-f)))
thir = fir*sec
U = math.atan(thir)
j = v/u

lamda = math.atan(j)
print("Lamda in Radians = ", lamda)

o = pow(math.sin(U), 3)
m = w+e2*a*o
q = pow(math.cos(U), 3)
n = (p - e2*a*q)*(1-f)
phi = math.atan(m/n)
print("Phi in Radians = ", phi)

z = pow(math.sin(phi),2)
W = math.sqrt(1 - e2*z)
N = a/W
h1 = math.cos(phi) 
h2 = math.sin(phi)
h3 = ((a*a)/N)
h = p*h1 +w*h2 - h3
print("Height = ", h)




