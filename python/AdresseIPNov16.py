#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def estNombre(s):
    if s.isdecimal() and -1 < int(s) < 256:
        return True
    return False

def estIP(s):
    lst = s.split(".")
    if len(lst) != 4:
        print("IP non valide")
        return False
    
    for elt in lst:
        if not estNombre(elt):
            print("IP non valide")
            return False
        
    print("IP valide")
    return True

#estIP("212.85.150.134")

def modifier(s):
    if estIP(s):
        lst = s.split(".")
        lst[0], lst[1] = "255", "255"
        return ".".join(lst)

print(modifier("212.85.150.134"))