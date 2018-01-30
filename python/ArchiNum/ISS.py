# -*- coding: utf-8 -*-
import timeit, time

def init():
    global running, pc
    running = 0
    pc = 0

pc = 0
running = 1

##############################################################"
regs = [0 for i in range(32)] #Nombre de registres
mem = [0 for i in range(32)]#Nombre d'espace mémoire


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
#    print("Je compare {} à {}".format(regs[r1], o))
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
#######################################################################

def bin2hex(liste):
    tmp = ["0" for i in range(32)]
    for indice in liste:
        tmp[indice] = "1"
    binaire = hex(int("".join(tmp[::-1]), 2))
    return binaire

def decodeStop(instr, running, *args):
    return (running,)

def decodeScall(instr, *args):
    n = (instr & 0x7ffffff)
    return (n,)


def decode3Braz(instr, *args):
    r = (instr & 0x7c00000) >> 22
    a = (instr & 0x3fffff)
    return (r, a)

def decode3Jmp(instr, *args):
    imm = (instr & 0x4000000) >> 26
    o = (instr & 0x3ffffe0) >> 5
    r = (instr & 0x1f)
    return (imm, o, r)


def decode4(instr, *args):
    reg1 = (instr & 0x07C00000) >> 22
    imm = (instr & 0x00200000) >> 21
    o = (instr & 0x001FFFE0) >> 5
    reg2 = (instr & 0x0000001F)
    return (reg1, imm, o, reg2)

deux = [3, 4, 15, 16, 17]
cycle = {i : 2 for i in deux}

switch = {0     : stop,
          1     : add,
          2     : sub,
          3     : div,
          4     : mult,
          5     : And,
          6     : Or,
          7     : xor,
          8     : shl,
          9     : shr,
          10    : slt,
          11    : sle,
          12    : seq,
          13    : load,
          14    : store,
          15    : jmp,
          16    : braz,
          17    : branz,
          18    : scall
          }

def evaluation(pc, running, instrNum, *args):
    tmpFct = switch[instrNum]
#    print(perf)
    try:
        tmpPerf = cycle[instrNum]
#        print("PERF FUNCT : ", performance[instrNum])

    except KeyError:
#        print("PERF FUNCT : ", 1)
        tmpPerf = 1
#    print("PERF AP / ", perf)
#    print("APPEL FCT : ", tmpFct.__name__, " || PC = ", pc)
    return tmpFct(*args), tmpPerf

executionDict = {0  : decodeStop,
                 15 : decode3Jmp,
                 16 : decode3Braz,
                 17 : decode3Braz,
                 18 : decodeScall
                 }

def execution(pathBinaire, running):
    program = []
    with open("binaire.txt", "r") as f:
        for lines in f.readlines():
            chiffLigne = int(lines, 16)
            instrNum = (chiffLigne & 0xF8000000) >> 27
            try:
                execution = executionDict[instrNum](chiffLigne, running)

            except KeyError:
                execution = decode4(chiffLigne, running)

            program.append((instrNum, *execution))

    return program

def fetch(program, pc, running):
#    tmp = []
#    for tt in program:
#        tmp.append(switch[tt[0]].__name__)
#    print(tmp)
#    print(program)
    cycle = 0
    while running:
#        print("REGS : ", regs)
#        print("RUNNING = ", running)
#        print("REGS 1 : ", regs[1])
        elt = program[pc]
        temp, tmpPerf = evaluation(pc, running, *elt)
        cycle += tmpPerf
#        print("PC : ", pc)
        if temp == "STOP":
            running = 0

        elif isinstance(temp, int):
            pc = temp

        else:
            pc += 1
#    print("PERFORMANCE : ", cycle)
    return cycle

if __name__ == "__main__":

    program = execution("binaire.txt", running)
    performance = []
    for i in range(1000):
        debut = time.time()
    #    toto = timeit.timeit("fetch(program, pc, running)", setup="from ISS import fetch;from ISS import execution;running=0;pc=0;program = execution('binaire.txt', running)")
    #    print("TIMEIT : ", toto)
        cycles = fetch(program, pc, running)
        fin = time.time() - debut
#        print("TEMPS : ", fin)
#        print("CYCLES : ", cycles)
#        print("durée : ", temps)
        performance.append(cycles / fin)
#        print("PERFORMANCE : ", cycles / temps)

    Moy = sum(performance)/len(performance)
    print("PERF MOY  : ", Moy)
