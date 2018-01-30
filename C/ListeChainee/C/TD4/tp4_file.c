#include <stdio.h>
#include "usrfifo.h"
/*---------------------------------------------------------------- 
   Implantation du TAD FILE à l'aide d'un tableau : gestion
   circulaire du tableau à l'aide de deux indices, un indice
   de lecture et un indice d'écriture.
   On peut placer dans la file au plus TAILLE éléments 
----------------------------------------------------------------*/

int main() {

  int tab[TAILLE];
  int curseur_lecture;   /* la prochaine case à lire (0 à TAILLE-1)   */
  int curseur_ecriture;  /* la prochaine case à écrire (0 à TAILLE-1) */
  int op = 0;
  int nb_entrees_clavier;
  /* À COMPLÉTER PAR LA DÉCLARATION DE NOUVELLES VARIABLES SI
   * NECESSAIRE */

  /* boucle du menu */
  do {
    printf("terminer    (0) \n");
    printf("initialiser (1) \n");
    printf("enfiler     (2) \n");
    printf("défiler     (3) \n");
    printf("afficher    (4) \n");

    /* boucle de saisie de l'opération à effectuer */
    do {
      printf("\nopération ? \n");
      nb_entrees_clavier = scanf("%d", &op);
      while( getchar() != '\n' ){
        /* empty */;
      }
    } while ( nb_entrees_clavier != 1 );
   
    printf("opération choisie : %d\n",op);

    /* traitement de l'opération choisie */
    switch (op) { 
      case 0 :   printf("Au revoir \n\n");
                 break;
      case 1 :   printf("initialiser \n\n");
                 /* À COMPLÉTER AVEC L'APPEL AU SOUS-PROGRAMME QUI INITIALISE*/
                 break;
      case 2 :   printf("enfiler \n\n");
                 /* À COMPLÉTER AVEC L'APPEL AU SOUS-PROGRAMME QUI AJOUTE UNE
                    VALEUR */
                 break;
      case 3 :   printf("défiler \n\n");
                 /* À COMPLÉTER AVEC L'APPEL AU SOUS-PROGRAMME QUI ENLÈVE UNE
                    VALEUR */
                 break;
      case 4 :   printf("afficher \n\n");
                 /* À COMPLÉTER AVEC L'APPEL AU SOUS-PROGRAMME QUI AFFICHE */
                 break;
      default  : printf(" \n\n\007opération non conforme\n\n");
                 break; 
    }
  } while (op != 0);

  return 0;
}

/* À COMPLÉTER AVEC L'IMPLANTATION DES SOUS-PROGRAMMES */
