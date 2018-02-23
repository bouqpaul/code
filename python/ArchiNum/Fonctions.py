#!/usr/bin/env python3
# -*- coding: utf-8 -*-
<<<<<<< HEAD
import numpy as np
regs = [0 for i in range(32)] #Nombre de registres
mem = [0 for i in range(32)]#Nombre d'espace mémoire
=======

regs = [0 for i in range(32)]   #Nombre de registres
mem = [0 for i in range(32)]    #Nombre d'espace mémoire
>>>>>>> 4b996067beaab4b0c7fbb5e801f4d5db5e4be804

pc = 0
running = 1

def log(nbr, base):
    res = np.log(nbr) / np.log(base)
    if res.is_integer():
        res = int(res)
    return res


def xor(r1, imm, o, r2):
    if not imm:
        o = regs[o]
    regs[r2] = o ^ regs[r2]

def shl(r1, imm, o, r2):
    if not imm:
        o = regs[o]
    regs[r2] = regs[r1] << o

def shr(r1, imm, o, r2):
    if not imm:
        o = regs[o]
    regs[r2] = regs[r2] >> o

def slt(r1, imm, o, r2):
    if not imm:
        o = regs[o]

    if regs[r1] < o:
        regs[r2] = 1
    else:
        regs[r2] = 0

def sle(r1, imm, o, r2):
    if not imm:
        o = regs[o]

    if regs[r1] <= o:
        regs[r2] = 1
    else:
        regs[r2] = 0

def seq(r1, imm, o, r2):
    if not imm:
        o = regs[o]
    if regs[r1] == o:
        regs[r2] = 1

    else:
        regs[r2] = 0

def load(r1, imm, o, r2):
    if not imm:
        o = regs[o]
        
    regs[r2] = mem[r1 + o]


def store(r1,imm,  o, r2):
    if not imm:
        o = regs[o]
        
    mem[r1 + o] = regs[r2]


def jmp(imm, o, r):
    if not imm:
        o = regs[o]
    adresseJmp = o - 1
    regs[r] = pc + 1
    return adresseJmp

def braz(r, a):
    if regs[r] == 0:
        adresseJump = a
        return adresseJump

def branz(r, a):
    if regs[r] != 0:
        return a

def scall(n):
    if n:
        print(regs[1])
    else:
        temp = input("Valeur à mettre dans le registre R1 : ")
        regs[1] = int(temp)

def add(reg1, imm, o, reg2):
    if imm == 1:
        regs[reg2] = o + regs[reg1]
    else:
        regs[reg2] =  regs[reg1] + regs[o]

def sub(reg1, imm, o, reg2):
    if imm == 1:
        regs[reg2] =  regs[reg1] - o

    else:
        regs[reg2] =  regs[reg1] - regs[o]

def stop(running):
    return "STOP"

def div(reg1, imm, o, reg2):
    if not imm:
        o = regs[o]

    try:
        regs[reg2] = regs[reg1] // o
    except ZeroDivisionError:
        print("Division par zéro.")

def mult(reg1, imm, o, reg2):
    if imm == 1:
        regs[reg2] = regs[reg1] * o
    else:
        regs[reg2] = regs[reg1] * regs[o]

def And(reg1, imm, o, reg2):
    if imm == 1:
        regs[reg2] = regs[reg1] & o
    else:
        regs[reg2] = regs[reg1] & regs[o]

def Or(reg1, imm, o, reg2):
    if imm == 1:
        regs[reg2] = regs[reg1] | o
    else:
        regs[reg2] = regs[reg1] | regs[o]