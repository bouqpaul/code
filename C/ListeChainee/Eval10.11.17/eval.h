#include "evalStruct.h"

/* Initialise un graphe */
void * initGraphe();

/* Initialise un noeud */
void * initNoeud(char * nom);

/* Create un lien de poids cout entre les noeux  pDebut et pFin */
void * createLien(int cout, struct noeud * pDebut, struct noeud * pFin);

/* Ajoute le noeud pN au graphe pG */
void addNoeud(struct graphe * pG, struct noeud * pN);

/* Ajoute le lien pL au graphe pG */
void addLien(struct graphe * pG, struct lien * pL);

