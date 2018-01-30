#include "usrfifo.h"


int main(){
    int tab[TAILLE];
    int itete;
    int iqueue;
    int nb_elem;
    int tete_val;
    creer_file(tab, &itete, &iqueue, &nb_elem);
    enfiler(32, tab, &iqueue, &nb_elem);
    enfiler(132, tab, &iqueue, &nb_elem);
    enfiler(232, tab, &iqueue, &nb_elem);
    enfiler(332, tab, &iqueue, &nb_elem);
    afficher_file(tab, itete, nb_elem);
    la_tete(tab, itete, iqueue, &tete_val);
    defiler(tab, &itete, &iqueue, &tete_val);
    afficher_file(tab, itete, nb_elem);
    quel_etat(nb_elem);
    la_tete(tab, itete, nb_elem, &tete_val);

                
    return 0;

}
