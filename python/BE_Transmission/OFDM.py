#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mescol import *
plt.close("all")


def ber(bits, PS):
    bits_PS = P2S(PS)
    return np.sum( abs(bits - bits_PS) ) / len(bits)

def S2P(bits, mu):
    """
    Série à Parallèle
    Groupe les bits par paquets de mu (1 groupe pour chaque porteuse)
    """
    print(bits)
    return bits.reshape((len(bits) // mu, mu))

def P2S(bits):
    """
    Parallèle à Série
    Dégroupe les paquets de bits
    """
    return bits.reshape((-1,))

def Demapping(QAM, demapping_table):
    """
    Transforme les points de la constellation en groupes de bits correspondant.
    """
    # Toutes les possibilités
    constellation = np.array([x for x in demapping_table.keys()])
    
    # Calcule de la distance
    dists = abs(QAM.reshape((-1, 1)) - constellation.reshape((1, -1)))
    
    # Indice en fonction de la distance la plus petite
    const_indice = dists.argmin(axis=1)
    
    # Le véritable point de la constelation
    vraiPoints = constellation[const_indice]
    
    # On récupère le groupe de bits associé
    return np.vstack([demapping_table[C] for C in vraiPoints]), vraiPoints

def Mapping(bits, mapping_table):
    """
    Transforme les groupes de bits envoyé par SP en symboles définis dans mapping_table
    """
#    for paquet in bits:
#        print(paquet)
#        for i in range(len(paquet)):
#            paquet[i] = int(paquet[i][1:], 2)
#    print(bits)
#    ss
    return np.array([mapping_table[tuple(b)] for b in bits])

def DFT(signal):
    """
    Transformée de Fourier
    """
    return np.fft.fft(signal)

def IDFT(signal):
    """
    Transformée de Fourier Inverse
    """
    return np.fft.ifft(signal)

def ajoutPC(signal, PC):
    """
    Ajoute un préfixe cyclique
    """
    pc = signal[-PC:]         
    return np.hstack([pc, signal])

def enlevePC(signal, PC, K):
    """
    Enlève le préfixe cyclique
    """
    return signal[PC:(PC+K)]

def canal(signal, SNRdb):
    """
    Modélisation du canal sans fil entre les antennes émeteur et récepteur.
    """
    P_signal = np.mean(abs(signal**2))
    sigma2 = P_signal * 10**(-SNRdb / 10)  # Calcul de la puissance du bruit par rapport à la puissance du signal et du SNR
    
    # Génération du bruit gaussien avec la variance sigma
    noise = np.sqrt(sigma2/2) * (np.random.randn(*signal.shape) + 1j * np.random.randn(*signal.shape))
    return signal + noise

def OFDM(bits, mu, K, PC, mapping_table, affichage=True):
    """
    Génère une modulation OFDM avec préfixe cyclique
    """
    #Groupe les bits par paquets de mu
    bits_SP = S2P(bits, mu)
    print(bits_SP)
    
    #On associe un symbole par paquet selon mapping_table
    QAM = Mapping(bits_SP, mapping_table)
    
    #On fait une FFT inverse
    OFDM_temps = IDFT(QAM)
    
    #On ajoute un préfix cyclique
    OFDM_PC = ajoutPC(OFDM_temps, PC)
    
    if affichage:
        plt.figure(figsize=(8, 2))
        plt.plot(abs(OFDM_PC), label='Signal transmis')

        plt.legend(fontsize=10)
        plt.xlabel('Time'); plt.ylabel('$|x(t)|$');
        plt.grid(True);
    
    return OFDM_PC
    
def DemodOFDM(OFDM_Recu, K, PC, demapping_table, affichage=True):
    """
    Démodule un signal OFDM
    """
    if affichage:
        plt.plot(abs(OFDM_Recu), label='Signal reçu')
       
        plt.legend(fontsize=10)
        plt.xlabel('Time'); plt.ylabel('$|x(t)|$');
        plt.grid(True);
        
    #On enlève le préfixe cyclique du signal reçu
    OFDM_sansPC = enlevePC(OFDM_Recu, PC, K)
    
    #On fait une FFT
    OFDM_demod = DFT(OFDM_sansPC)
    
    # On fait la correspondance entre les paquets reçus
    # et les symboles selon demapping_table
    PS, QAM = Demapping(OFDM_demod, demapping_table)
    
    
    if affichage:
        plt.figure()
        for demod, qam in zip(OFDM_demod, QAM):
             plt.plot([demod.real, qam.real], [demod.imag, qam.imag], 'k-o')
        plt.plot(QAM.real, QAM.imag, 'ro')
         
        
    return PS, QAM, OFDM_demod
    

K = 128 # nombre de porteuse

PC = K // 4  # longueur du préfixe cyclique. Permet une meilleure détection des symboles

mu = 4 # bits par symbole. 4 car QAM 16
info_par_bits = K * mu

mapping_table = {
    (0,0,0,0) : -3-3j,
    (0,0,0,1) : -3-1j,
    (0,0,1,0) : -3+3j,
    (0,0,1,1) : -3+1j,
    (0,1,0,0) : -1-3j,
    (0,1,0,1) : -1-1j,
    (0,1,1,0) : -1+3j,
    (0,1,1,1) : -1+1j,
    (1,0,0,0) :  3-3j,
    (1,0,0,1) :  3-1j,
    (1,0,1,0) :  3+3j,
    (1,0,1,1) :  3+1j,
    (1,1,0,0) :  1-3j,
    (1,1,0,1) :  1-1j,
    (1,1,1,0) :  1+3j,
    (1,1,1,1) :  1+1j
}

demapping_table = {v : k for k, v in mapping_table.items()}

SNRdb = -5 #Signal to Noise Ratio

#bits = np.random.binomial(n=1, p=0.5, size=(info_par_bits, )) #Message aléatoire
bits = np.array(mescol(5000, 44000))
print("....", bits)
ss

OFDM_Transmis = OFDM(bits, mu, K, PC, mapping_table)
OFDM_Recu = canal(OFDM_Transmis, SNRdb)
PS, hardDecision, QAM_est = DemodOFDM(OFDM_Recu, K, PC, demapping_table)

print ("Bit Error Rate: ", ber(bits, PS))
plt.show()
