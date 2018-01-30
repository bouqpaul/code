#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include "Struc_glob.h"


//-------------------------------------------------------------------
page * newPage(int ID, int taille, int adresse){
    page * myPage;
	myPage = malloc(sizeof(page));
	myPage->ID = ID;
	myPage->IDProcessus = 0;
	myPage->taille = taille;
	myPage->memUtilise = 0;
	myPage->adresse = adresse;
	myPage->libre = 1;
	return myPage;
}

OS * newOS(char * Nom, int NbPage, int taille){
	OS * myOS = malloc(sizeof(OS));
	myOS->nom = Nom;
	myOS->Nb_page = NbPage;
	myOS->Nb_page_active = 0;
	myOS->taille = MAXPAGEOS * TAILLEPAGE;
    
    
    page * tabDisque[MAXPAGEOS] = {NULL};
    page * tabSwap[MAXPAGESWAP] = {NULL};
    
    *(myOS->pdisque) = *tabDisque;
    *(myOS->pswap) = *tabSwap;
    
	/*int i;
	page * tmp;

	for(i = 0; i < MAXPAGEOS; i++){
        tmp = newPage(i + 1, TAILLEPAGE, i * TAILLEPAGE);
        myOS->pdisque[i] = tmp;
	}
	
	for(i = 0; i < MAXPAGESWAP; i++){
        tmp = newPage(i + 1, TAILLEPAGE, i * TAILLEPAGE);
        myOS->pswap[i] = tmp;
	}*/
	
	return myOS;

}


processus * newprocess(int ID, int tailleProc){
	processus * process = malloc(sizeof(processus));
	process->ID = ID;
	process->tailleProc = tailleProc;
	page * tabPage[MAXPAGEPROC] = {NULL};
	*(process->pproc) = *tabPage;

	return process;
}
//--------------------------------------------------------------

int get_page(page * Page, processus * Process){
    int i = 0;
    if(Page == NULL){printf("GET PAGE NULL\n");return 1;}
    if(Page->libre == 0){
        printf("La page %i n'est pas libre.", Page->ID);
        return 1;
        }
        
    while(i < MAXPAGEPROC){
        if((Process->pproc)[i] == NULL){
            Page->IDProcessus = Process->ID;
            Page->libre = 0;
            int temp;
            temp = (Process->tailleProc < Page->taille) ? (Process->tailleProc):(Page->taille);
            Page->memUtilise = temp;
            Process->tailleProc = Process->tailleProc - temp;
            (Process->pproc)[i] = Page;
            return 0;
            }
        i++;
    }
    
    if(i >= MAXPAGEPROC - 1){
        printf("Nombre de pages maximales atteintes pour le processeur.\n");
        return 1;
        }
    //TODO : release page quand le processus a atteint le nbr limite de pages
        
    return 0;
}

int release_page(page * P, processus * Process){
    if(P == NULL){printf("RELEASE PAGE NULL\n");return 1;}
    if(P->IDProcessus != Process->ID){
        printf("La page %i n'appartient pas au processus %i\n", P->ID, Process->ID);
        return 1;
        }
        
    int i;
    for(i = 0; i < MAXPAGEPROC; i++){
        if((Process->pproc)[i] == NULL){continue;}
        if(((Process->pproc)[i])->ID == P->ID){
            ((Process->pproc)[i])->libre = 1;
            ((Process->pproc)[i])->IDProcessus = 0;
            ((Process->pproc)[i])->memUtilise = 0;
            (Process->pproc)[i] = NULL;
            return 0;
        }
    
    }
    return 0;
    
}

int add_page_disque(page * P, OS * myOS){
    int i;
    for(i = 0; i < MAXPAGEOS; i++){
        if((myOS->pdisque)[i] == NULL){
            (myOS->pdisque)[i] = P;
            break;
            }
    }
    if(i >= MAXPAGEOS){
        printf("OS : Nombre de pages maximales atteintes sur le disque.\n");
        return 1;
        }
        
    return 0;

}

int add_page_swap(page * P, OS * myOS){
    int i;
    for(i = 0; i < MAXPAGESWAP; i++){
        if((myOS->pswap)[i] == NULL){
		(myOS->pswap)[i] = P;
		return 0;
	}
    }
    printf("OS : Nombre de pages maximales atteintes pour le swap.\n");
    return 0;
}
//--------------------------------------------------------------------
int get_info_page(page * Page, char * tab){
    printf("%sPage :                      %i\n", tab, Page->ID);
    printf("%sAppartenant au processus :  %i\n", tab, Page->IDProcessus);
    printf("%sMémoire utilisé :           %i / %i\n", tab, Page->memUtilise, Page->taille);
    printf("%sLibre :                     %s\n", tab, (Page->libre == 1) ? ("OUI"):("NON"));
    printf("\n");
    return 0;
}


int get_info_process(processus * Process){
    printf("Processus :     %i\n", Process->ID);
    printf("Taille :        %i\n", Process->tailleProc);
    int j;
    
    for(j = 0; j < MAXPAGEPROC; j++){
        page * temp = (Process->pproc)[j];
        if(temp != NULL){
            get_info_page(temp, "   ");

        }
    }
    printf("\n");
    return 0;
}

int get_info_OS(OS * myOS){
    printf("Nom de l'OS : %s\n", myOS->nom);
    printf("Nombre de pages actives : %i / %i\n", myOS->Nb_page_active, myOS->Nb_page);
    
    printf("Mémoire disque :\n\n");
    int i;
    for(i = 0; i < MAXPAGEOS; i++){
        if((myOS->pdisque)[i] != NULL){
            get_info_page((myOS->pdisque)[i], "    | ");
            if(i >= MAXPAGEOS){printf("    | \n");}
        }
    
    }
    
    printf("Mémoire swap :\n\n");
    for(i = 0; i < MAXPAGESWAP; i++){
        if((myOS->pswap)[i] != NULL){
            get_info_page((myOS->pswap)[i], "    | ");
            if(i >= MAXPAGESWAP){printf("    | \n");}
        }
    
    }
    return 0;
}




//-------------------------------------------------------------
page *swap_in(page * pageASwap, OS * myOS){
    int i, indiceSurSwap;
    
    for(indiceSurSwap = 0; indiceSurSwap < MAXPAGESWAP; indiceSurSwap++){
        if((myOS->pswap)[indiceSurSwap] == NULL){continue;}
        if(((myOS->pswap)[indiceSurSwap])->ID == pageASwap->ID){
            break;
            }
    
    }
    if(indiceSurSwap >= MAXPAGESWAP){
        printf("La page %i n'est pas présente dans le swap.\n", pageASwap->ID);
        return pageASwap;
        }

    for(i = 0; i < MAXPAGEOS; i++){
        if((myOS->pdisque)[i] == NULL){
            (myOS->pdisque)[i] = pageASwap;
            (myOS->pswap)[indiceSurSwap] = NULL;
            
            return (myOS->pdisque)[i];
        }
    
        if(((myOS->pdisque)[i])->libre == 1){
            swap_out((myOS->pdisque)[i], myOS);
            (myOS->pdisque)[i] = pageASwap;
            (myOS->pswap)[indiceSurSwap] = NULL;
            return (myOS->pdisque)[i];
        }
    }
    
    
    //A modifier : random, Least frequently used serait mieux
    int indiceRandom;
    srand(time(NULL));
    indiceRandom = rand() % MAXPAGEOS;
    
    (myOS->pswap)[indiceSurSwap] = NULL;
    (myOS->pdisque)[indiceRandom] = pageASwap;
    
    return (myOS->pdisque)[indiceRandom];
}

int swap_out(page * pageASwap, OS * myOS){
    int i, indiceSurDisque;

    for(indiceSurDisque = 0; indiceSurDisque < MAXPAGEOS; indiceSurDisque++){
        if((myOS->pdisque)[indiceSurDisque] == NULL){continue;}
        if(((myOS->pdisque)[indiceSurDisque])->ID == pageASwap->ID){
            break;
            }
    }
    
    if(indiceSurDisque >= MAXPAGEOS){
        printf("La page %i n'est pas présente sur le disque.\n", pageASwap->ID);
        return 1;
        }    
    
    for(i = 0; i < MAXPAGESWAP; i++){
        if((myOS->pswap)[i] == NULL){
            (myOS->pswap)[i] = pageASwap;
            (myOS->pdisque)[indiceSurDisque] = NULL;
            return 0;
            }
            
        if(((myOS->pswap)[i])->libre == 1){
            (myOS->pswap)[i] = pageASwap;
            (myOS->pdisque)[indiceSurDisque] = NULL;
            return 0;
            }
    }
    for(i = 0; i < MAXPAGESWAP; i++){
        if((myOS->pswap)[i] == NULL){
            (myOS->pswap)[i] = pageASwap;
            (myOS->pdisque)[indiceSurDisque] = NULL;
            return 0;
            }
            
        if(((myOS->pswap)[i])->libre == 1){
            (myOS->pswap)[i] = pageASwap;
            (myOS->pdisque)[indiceSurDisque] = NULL;
            return 0;
            }
    }

    //A modifier : random, Least frequently used serait mieux
    int indiceRandom;
    srand(time(NULL));
    indiceRandom = rand() % MAXPAGESWAP;

    (myOS->pswap)[indiceRandom] = pageASwap;
    (myOS->pdisque)[indiceSurDisque] = NULL;
    
    return 0;
}




int my_free(processus * P, OS * myOS){
    int i;
    for(i = 0; i < MAXPAGEPROC; i++){
        
        if((P->pproc)[i] != NULL){
           release_page((P->pproc)[i], P);
           (myOS->Nb_page_active)--;
           }
    
    }
    return 0;
}


int my_malloc(processus * P, OS * myOS){
    //int nbrPage = (P->tailleProc % TAILLEPAGE) + 1;
    int i;
    
    for(i = 0; i < MAXPAGESWAP; i++){
        printf("%i\n", i);
        if((myOS->pswap)[i] == NULL){continue;}
        if(((myOS->pswap)[i])->IDProcessus == P->ID){
            page * new;
            new = swap_in((myOS->pswap)[i], myOS);
            
	    printf("TAILLE PROC AV %i\n", P->tailleProc);
	    printf("NEW MEM %i\n", new->memUtilise);
            P->tailleProc = (P->tailleProc > new->memUtilise) ? (P->tailleProc - new->memUtilise):(new->memUtilise);
            (myOS->Nb_page_active)++;
            printf("!!!!!!!!!!!!!!!!!!!TAILLE PROC : %i\n", P->tailleProc);        
            if(P->tailleProc > 0){continue;}else{return 0;}
            }
    }
    
    for(i = 0; i < MAXPAGEOS; i++){
        if((myOS->pdisque)[i] == NULL){continue;}
        if(((myOS->pdisque)[i])->libre == 1){
            get_page((myOS->pdisque)[i], P);
            (myOS->Nb_page_active)++;
            
            if(P->tailleProc > 0){
                continue;
                }
            else{
                return 0;
                }
        }
    }
    
    //A modifier : random, Least frequently used serait mieux
    int indiceRandom;
    srand(time(NULL));
    indiceRandom = rand() % MAXPAGEOS;
    
    swap_out((myOS->pdisque)[indiceRandom], myOS);
    get_page((myOS->pdisque)[indiceRandom], P);
    
	return 0;
}
