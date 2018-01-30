#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lectureSMS(nom):
    result = []
    with open(nom, "r") as f:
        for line in f.readlines():
            temp = line.split(" ")
            res = temp[:3]
            res.append(" ".join(temp[3:]))
            result.append(res)
    for lst in result:
        lst[-1] = lst[-1].strip("\n")
    return result
            
SMS = lectureSMS("/home5/bouquepa/Python/donnee.txt")
#print(SMS)

def estPublicitaire(sms):
    [num, date, heure, mess] = sms
    if mess.count("€"):
        return True
    return False

def estSPAM(sms):
    [num, date, heure, mess] = sms
    temp = mess.split(" ")
    for elt in temp:
        if elt.isnumeric() and elt.startswith("089") and len(elt) == 10:
            return True
    return False

for elt in SMS:
    if estSPAM(elt):
        print("SPAM : {}".format(elt))
    elif estPublicitaire(elt):
        print("PUB : {}".format(elt))