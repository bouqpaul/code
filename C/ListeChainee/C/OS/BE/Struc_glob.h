#define MAXPAGEOS 8
#define MAXPAGESWAP 8
#define MAXPAGEPROC 2
#define TAILLEPAGE 1024


typedef struct page
{
    int ID;
    int IDProcessus;
    int adresse;
	int taille;
	int memUtilise;
	int libre;
}page;
//---------------------------------

typedef struct processus
{
	int ID;
	int tailleProc;	
	page *pproc[MAXPAGEPROC];

}processus;
//---------------------------------

typedef struct OS
{
	char * nom;
	int Nb_page;
	int Nb_page_active;
	int taille;
	page *pdisque[MAXPAGEOS];
	page *pswap[MAXPAGESWAP];

}OS;

page * newPage(int ID, int taille, int adresse);

OS * newOS(char * Nom, int NbPage, int taille);

processus * newprocess(int ID, int Nbpage);

int my_malloc(processus * P, OS * myOS);
int swap_out(page * pageASwap, OS * myOS);

int my_free(processus * P, OS * myOS);

