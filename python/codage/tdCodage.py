# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
P = [0.19, 0.13, 0.31, 0.07, 0.03, 0.09, 0.18]
T = sum(P)
#print(T)
def sumH(x):
    return -x*np.log2(x)

H = sum(list(map(sumH, P)))
#print("H = ", H)

codage = ["11", "011", "00", "1000", "1001", "101", "010"]
codageP = [(p,x) for (p,x) in zip(P, codage)]
def sumR(t):
    (p,x) = t
    return p*len(x)

R = sum(list(map(sumR, codageP)))
#print("R = ", R)
#print("Eff = ", (H/R)*100)
kraft = sum(list(map(lambda x: 2 ** (-len(x)), codage)))
#print("Kraft = ", kraft)


P2 = [0.17, 0.25, 0.11, 0.13, 0.08, 0.1, 0.07, 0.09]
print("TT = ", sum(P2))
codageP2 = [["000", "001", "010", "011", "100", "101", "110", "111"],
           ["0", "1", "01", "10", "11", "101", "110", "111"],
           ["0", "10", "110", "1110", "11110", "111110", "1111110", "1111111"],
           ["10", "0", "1110", "110", "1111110", "11110", "1111111", "111110"]]
H2 = sum(list(map(sumH, P2)))
print("H2 = ", H2)

RR = []
for elt in codageP2:
    RR.append(sum(list(map(sumR, zip(P2, elt)))))

print("R = ", RR)
Eff2 = [H2/r for r in RR]
print("Eff = ", Eff2)
KK2=[]
for elt in codageP2:
    KK2.append(sum(list(map(lambda x: 2**(-len(x)), elt))))
print("Kraft = ", KK2)

print("\n")
codage3 = ["000", "01", "101", "100", "0010", "110", "0011", "111"]
R3 = sum(list(map(sumR, zip(P2, codage3))))
print("R3 = ", R3)
kraft3 = sum(list(map(lambda x: 2**(-len(x)), codage3)))
print("Kraft3 = ", kraft3)
print("Eff3 = ", (H2/R3)*100)


10101100001110111101110

