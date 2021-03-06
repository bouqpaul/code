#include "usrfifo.h"
#include <stdio.h>
#include <stdlib.h>

void creer_file(int t[], int *itete, int *iqueue, int *nb_elem){

    int i;
    //t = malloc(sizeof(int) * TAILLE);
    for(i = 0; i < TAILLE; i++){
        t[i] = 0;
    }
    *itete = 0;
    *nb_elem = 0;
    *iqueue = 0;
    
}

void afficher_file(int t[], int itete, int nb_elem){
     int i;
     printf ("Indice de tete: %i\n", itete % TAILLE);

     for(i = 0; i < TAILLE; i++){
        if(t[i] != 0){
            printf("%i ", t[i]);
        }else{
            printf(". ");
            }
     }
     
     printf("\n");
     printf("Indice de queue: %i\n", (nb_elem) % TAILLE);
}

int enfiler(int nv_val, int t[], int *iqueue, int *nb_elem){
    if( *nb_elem < TAILLE - 1){
        int temp = ((*iqueue)++) % TAILLE;
        //printf("Indice Q enfiler: %i\n", *iqueue);
        iqueue = &temp;
        //*iqueue = (((*iqueue)++) % TAILLE);
        t[*iqueue] = nv_val;
        (*nb_elem)++;
        
        return 1;
        
        } else{
        
        printf("Opération impossible: File pleine.");
        return 0;
    }
}

char *quel_etat(int nb_elem){
    
    char* c = malloc(sizeof(char) * 1);
    char vide = 'V';
    char pleine = 'P';
    if(nb_elem == 0){
        c = &vide;
        }else{
        c = &pleine;
        }
    return c;
}

int defiler(int t[], int *itete, int *nb_elem, int *tete_val){
    if(nb_elem > 0){
        t[*itete] = 0;
        (*itete)++;
        int indice = (*itete);
        *tete_val = t[indice];
        
        return 1;
    } else{
        printf("Operation impossible: File vide.");
        return 0;
    }
}

int la_tete(int t[], int itete, int nb_elem, int *tete_val){
    if(*(quel_etat(nb_elem)) == 'P'){
    *tete_val = t[itete];
    return *tete_val;
    
    }else{
        printf("Operation impossile: File vide.");
        return 0;
    }
}
