#include <stdlib.h>
#include <stdio.h>
#include "eval.h"

void * initGraphe() {
    struct graphe * pG;
    pG = malloc(sizeof(struct graphe));
    pG->pointEntree = NULL;
    return pG;
}

void * initNoeud(char * nom){
    struct noeud * pN;
    pN = malloc(sizeof(struct noeud));
    pN->nom = nom;
    pN->nextNoeud = NULL;
    return pN;
}

void * createLien(int cout, struct noeud * pDebut, struct noeud * pFin){
    struct lien * pL;
    pL = malloc(sizeof(struct lien));
    pL->cout = cout;
    pL->fin = pFin;
    pL->debut = pDebut;
    
    pDebut->nextNoeud = pFin;
    return pL;

}


void addNoeud(struct graphe * pG, struct noeud * pNext){
    
    if(pG->pointEntree == NULL){
        pG->pointEntree = pNext; 
        }
    else{
        pNext->nextNoeud = pG->pointEntree;
        pG->pointEntree = pNext;
    }
}

void addLien(struct graphe * pG, struct lien * pL) {
    if(pG->lienEntree == NULL){
        pG->lienEntree = pL; 
        }
    else{
        pL->nextLien = pG->lienEntree;
        pG->lienEntree = pL;
    }

}

int existeChemin(struct graphe * pG, struct noeud * pDebut,struct noeud * pFin){
    struct lien * lienCourant;
    int trouveDeb = 0;
    int trouveFin = 0;
    lienCourant = pG->lienEntree;
    while(lienCourant != NULL){
        if(trouveDeb = 0 && lienCourant->debut == pDebut){
            trouveDeb = 1;
        }
        if(trouveFin = 0 && lienCourant->fin == pFin){
            trouveFin = 1;
            }
        lienCourant = lienCourant->nextLien;
    }
    if(trouveDeb == 1 && trouveFin == 1){
        int chemin;
        //int chemin = cheminMax(pG, pDebut, pFin);
        chemin = 1;
        return chemin;
        }
    else{
        return -1;
    }
    

}

/*int cheminMax(struct graphe * pG, struct noeud * pDebut,struct noeud * pFin){
    while(){
        
    
    }


}*/



int main(){
    char * nom1 = "A";
    struct noeud * n1;
    n1 = initNoeud(nom1);
    
    char * nom2 = "B";
    struct noeud * n2;
    n2 = initNoeud(nom2);
    
    struct graphe * g;
    g = initGraphe();
    
    struct lien * l1;
    l1 = createLien(4, n1, n2);
    
    char * nom3 = "C";
    struct noeud * n3;
    n3 = initNoeud(nom3);
    
    addNoeud(g, n3);
    addLien(g, l1);
    
    printf("Done.\n");


    return 0;
}
