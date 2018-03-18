# -*- coding: utf-8 -*-
import time
import Fonctions as ff

def decodeStop(instr, running, *args):
    """
    Décode l'appel à la fonction  stop.
    Renvoie 0 pour signifier la fin du programme et l'arrêt de la machine.
    """
    return (running,)

def decodeScall(instr, *args):
    """
    Décode l'appel à la fonction scall.
    Renvoie le numéro de l'appel système.
    """
    n = (instr & 0x7ffffff)
    return (n,)


def decode3Braz(instr, *args):
    """
    Décode l'appel à la fonction Braz et Branz.
    """
    r = (instr & 0x7c00000) >> 22
    a = (instr & 0x3fffff)
    return (r, a)

def decode3Jmp(instr, *args):
    """
    Décode l'appel à la fonction jmp.
    """
    imm = (instr & 0x4000000) >> 26
    o = (instr & 0x3ffffe0) >> 5
    r = (instr & 0x1f)
    return (imm, o, r)


def decode4(instr, *args):
    """
    Décode l'appel à l'ensemble des fonctions ayant 4 arguments.
    Par exemple, add, sub, mult, ...
    """
    reg1 = (instr & 0x07C00000) >> 22
    imm = (instr & 0x00200000) >> 21
    o = (instr & 0x001FFFE0) >> 5
    reg2 = (instr & 0x0000001F)
    return (reg1, imm, o, reg2)


# Regroupement des fonctions comptant pour 2 cycles
# mult, div, braz, branz, jmp
# (cf switch pour le numéro des fonctions)  
deux = [3, 4, 15, 16, 17]
cycle = {i : 2 for i in deux}


## Dictionnaire associant le numéro d'instructions à la fonction correspondante
switch = {0     : ff.stop,
          1     : ff.add,
          2     : ff.sub,
          3     : ff.div,
          4     : ff.mult,
          5     : ff.And,
          6     : ff.Or,
          7     : ff.xor,
          8     : ff.shl,
          9     : ff.shr,
          10    : ff.slt,
          11    : ff.sle,
          12    : ff.seq,
          13    : ff.load,
          14    : ff.store,
          15    : ff.jmp,
          16    : ff.braz,
          17    : ff.branz,
          18    : ff.scall
          }

def evaluation(pc, running, instrNum, *args):
    """
    Évalue la fonction appelée suivant le numéro d'instruction.
    Renvoie également le nombre de cycle de cette fonction.
    """
    tmpFct = switch[instrNum]
    
    try:
        # nombre de cycle spécial pour certaines fonctions
        tmpPerf = cycle[instrNum]

    except KeyError:
        tmpPerf = 1

    return tmpFct(*args), tmpPerf


## Dictionnaire regroupant les fonctions "spéciales",
## c'est-à-dire, des fonctions ne prenant pas 4 arguments.
executionDict = {0  : decodeStop,
                 15 : decode3Jmp,
                 16 : decode3Braz,
                 17 : decode3Braz,
                 18 : decodeScall
                 }

def fetch(pathBinaire, running):
    """
    Transforme les instructions hexadécimal contenues dans le fichier
    qui se trouve au chemin passé en argument.
    Renvoie le programme décodé dans la liste program.
    Chaque fonctions est associée à une ligne.
    """
    program = []
    with open(pathBinaire, "r") as f:
        for lines in f.readlines():
            # On transforme la chaine de caractère en nombre
            chiffLigne = int(lines, 16)
            
            # On décode le numéro d'instructions
            instrNum = (chiffLigne & 0xF8000000) >> 27
            try:
                # Traitement "normal"
                # Fonctions avec 4 arguments
                execution = executionDict[instrNum](chiffLigne, running)

            except KeyError:
                # Traitement spécial
                execution = decode4(chiffLigne, running)

            program.append((instrNum, *execution))

    return program

def execution(program, pc, running):
    """
    Exécute l'ensemble des fonctions contenues dans la liste program.
    """
    # Compteur de cycles
    cycle = 0
    
    # Tant que l'on a pas rencontré "STOP"
    while running:
        # On récupère la fonction à la position pc
        elt = program[pc]
        # On renvoie l'exécution de la fonction et sa performance (nombre de cycles)
        temp, tmpPerf = evaluation(pc, running, *elt)
        cycle += tmpPerf

        # On arrête l'exécution
        if temp == "STOP":
            running = 0

        # Les fonctions qui effectue des sauts dans le code renvoie un entier
        # Cet entier est la ligne à laquelle l'exécution doit se poursuivre
        # Sinon, les fonctions renvoie None
        elif isinstance(temp, int):
            pc = temp

        else:
            pc += 1

    return cycle


def calcPerf(pathBinaire, running, pc, nbrExe):
    """
    Calcule la performance de l'ISS et fait la moyenne sur nbrExe nombre d'exécution.
    """
    # On récupère le programme
    program = fetch(pathBinaire, running)
    
    # Liste contenant les nbrExe performance du programme
    performance = []
    
    for i in range(nbrExe):
        # Calcule du temps d'exécution du programme
        debut = time.time()
        cycles = execution(program, pc, running)
        fin = time.time() - debut
        performance.append(cycles / fin)
    
    # Calcule de la moyenne
    Moy = sum(performance) / len(performance)
    return Moy
