#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regroupe toutes les fonctions utilisables par l'ISS
"""
import memory
import cache

# Variable du système
NBR_REGS = 32
pc = 0
running = 1

# Mémoire et cache
M = memory.Memory(size=16)
C = cache.Cache(4, 1, 2, 4, M)

# Registres
regs = [0 for i in range(NBR_REGS)]   #Nombre de registres

## Fonctions de l'ISS

def xor(r1, imm, o, r2):
    """
    Ou exclusif
    """
    if not imm:
        o = regs[o]
        
    regs[r2] = o ^ regs[r2]

def shl(r1, imm, o, r2):
    """
    Shift gauche
    """
    if not imm:
        o = regs[o]
    regs[r2] = regs[r1] << o

def shr(r1, imm, o, r2):
    """
    Shift droite
    """
    if not imm:
        o = regs[o]
    regs[r2] = regs[r2] >> o

def slt(r1, imm, o, r2):
    """
    Inférieur stricte
    """
    if not imm:
        o = regs[o]

    if regs[r1] < o:
        regs[r2] = 1
    else:
        regs[r2] = 0

def sle(r1, imm, o, r2):
    """
    Inférieur ou égale
    """
    if not imm:
        o = regs[o]

    if regs[r1] <= o:
        regs[r2] = 1
    else:
        regs[r2] = 0

def seq(r1, imm, o, r2):
    """
    Égalité
    """
    if not imm:
        o = regs[o]
    if regs[r1] == o:
        regs[r2] = 1

    else:
        regs[r2] = 0

def load(r1, imm, o, r2):
    """
    Transfert une donnée de la mémoire dans les registres
    """
    if not imm:
        o = regs[o]
    
    # On vient lire dans le cache    
    regs[r2] = C.lire(("{:0" + str(C.addrBits) + "b}").format(r1 + o))


def store(r1, imm,  o, r2):
    """
    Stocke une variable dans la mémoire
    """
    if not imm:
        o = regs[o]
    
    # On écrit directement dans la mémoire
    M.ecrit(("{:0" + str(M.nbrBits) + "b}").format(r1 + o), regs[r2])


def jmp(imm, o, r):
    """
    Saute d'une ligne à une autre
    """
    if not imm:
        o = regs[o]
    
    # Décalage dans les indices
    adresseJmp = o - 1
    regs[r] = pc + 1
    
    return adresseJmp

def braz(r, a):
    """
    Branchement si zéro
    """
    if regs[r] == 0:
        adresseJump = a
        return adresseJump

def branz(r, a):
    """
    Branchement si non zéro
    """
    if regs[r] != 0:
        return a

def scall(n):
    """
    System call
    0 - change la valeur du registre 1
    1 - affiche la valeur du registre 1
    """
    if n:
        print(regs[1])
    else:
        temp = input("Valeur à mettre dans le registre R1 : ")
        regs[1] = int(temp)

def add(reg1, imm, o, reg2):
    """
    Addition
    """
    if imm == 1:
        regs[reg2] = o + regs[reg1]
    else:
        regs[reg2] =  regs[reg1] + regs[o]

def sub(reg1, imm, o, reg2):
    """
    Soustraction
    """
    if imm == 1:
        regs[reg2] =  regs[reg1] - o

    else:
        regs[reg2] =  regs[reg1] - regs[o]

def div(reg1, imm, o, reg2):
    """
    Division
    """
    if not imm:
        o = regs[o]

    try:
        regs[reg2] = regs[reg1] // o
        
    except ZeroDivisionError:
        raise

def mult(reg1, imm, o, reg2):
    """
    Multiplication
    """
    if imm == 1:
        regs[reg2] = regs[reg1] * o
    else:
        regs[reg2] = regs[reg1] * regs[o]

def And(reg1, imm, o, reg2):
    """
    Et logique
    """
    if imm == 1:
        regs[reg2] = regs[reg1] & o
    else:
        regs[reg2] = regs[reg1] & regs[o]

def Or(reg1, imm, o, reg2):
    """
    Ou logique
    """
    if imm == 1:
        regs[reg2] = regs[reg1] | o
    else:
        regs[reg2] = regs[reg1] | regs[o]

def stop(running):
    """
    Arrêt de l'exécution
    """
    return "STOP"
