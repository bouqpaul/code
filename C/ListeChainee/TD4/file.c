#include "usrfifo.h"
#include <stdio.h>

void creer_file(int t[], int *itete, int *iqueue, int *nb_elem){

    int i;
    t = malloc(sizeof(int) * TAILLE);
    for(i=0; i<TAILLE; i++){
        t[i]=0;
    }
    *itete = 0;
    *nb_elem = 0;
    *iqueue = 0;
    
}



void afficher_file(int t[], int itete, int nb_elem){
     int i;
     printf ("Indice de tete: %i\n", itete % TAILLE);
     for(i = 0; i < TAILLE; i++){
        printf("%i ", t[i]);
     
     }
     printf("\n");
     printf("Indice de queue: %i", (nb_elem + 1) % TAILLE);

}


int enfiler(int nv_val, int t[], int *iqueue, int *nb_elem){
    if( nb_elem < TAILLE - 1){
    t[*iqueue] = nv_val;
    ((*iqueue)++) % TAILLE;
    (*nb_elem)++;
    } else{
    printf("Opération impossible: File pleine.");
    }
}

int defiler(int t[], int *itete, int *nb_elem, int *tete_val){
    


}
