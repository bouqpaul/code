#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:04:14 2018

@author: doofy
"""

def syra(n):
    res = [n]
    while res[-1] != 1:
        tmp = res[-1]
        if tmp % 2 != 0:
            res.append(3*tmp + 1)
        else:
            res.append(tmp // 2)
    return res

print(syra(23))