#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:51:18 2020

@author: Alaisha Naidu
Name: Levelling Loop Closure 
Creds: University of Cape Town
"""

class Precise_levelling:
    def __init__(self, BS1, FS1, FS2, BS2):
        self.BS1 =BS1
        self.BS2 =BS2
        self.FS1 =FS1
        self.FS2 =FS2
    
    def leg_misclosure(self):
        misclosure =(self.BS1-self.FS1)-(self.BS2-self.FS2)
        return print("Misclosure for leg is:", misclosure)