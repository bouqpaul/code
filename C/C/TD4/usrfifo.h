/* Capacite (nombre maximal d'elements) de la file */
#define TAILLE 5

/*
 * @brief cree une file sous forme d'un tableau de capacite TAILLE.
 */
void creer_file(int t[], int *itete, int *iqueue, int *nb_elem);
/*
 * @brief affiche la file t contenant nb_elem, a partir de la tete itete.
 */
void afficher_file(int t[], int itete, int nb_elem);
/*
 * @brief enfile l'element nv_val dans la file t, a partir de la queue iqueue.
 */
int enfiler(int nv_val, int t[], int *iqueue, int *nb_elem);
/*
 * @brief enleve l'element tete_val de la file t, a partir de la tete itete.
 */
int defiler(int t[], int *itete, int *nb_elem, int *tete_val);
/*
 * @brief retourne l'etat de la file.
 */
char *quel_etat(int nb_elem);
/*
 * @brief donne la tete de la file.
 */
int la_tete(int t[], int itete, int nb_elem, int *tete_val);
