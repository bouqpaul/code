#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ISS import running
from ISS import pc

regs = [0 for i in range(32)]   #Nombre de registres
mem = [0 for i in range(32)]    #Nombre d'espace mémoire


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
    

def jmp(pc, imm, o, r):
    if not imm:
        o = regs[o]
    adresseJmp = o
    regs[r] = pc + 1
    print("DANS JMP : ", regs[r])
    return adresseJmp

def braz(r, a):
    return 1

def branz(r, a):
    return 1

def scall(n):
    if n:
        print(regs[1])
    else:
        input("Valeur à mettre dans le registre R1 : \n")

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
    running = 0

def div(reg1, imm, o, reg2):
    if o == 0:
        if imm == 1:
            regs[reg2] = regs[reg1] / o

        else:
            regs[reg2] = regs[reg1] / regs[o]

    else:
        print("Erreur division par 0")

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
    
    