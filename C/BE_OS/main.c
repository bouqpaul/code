//#include "Struc_glob.h"
#include "new.c"
#include <pthread.h>
int main(){
    /*page * tab[10] = {NULL};
    int i;
    for(i = 0; i < 10; i++){
        printf("%i", tab[i]);
    
    }*/
    
    
	page *p1, *p2, *p3, *p4;
	processus * P1;
	OS * toto;
	
    P1 = newprocess(123, 2000);
    
	char * nom;
	nom = "azefrazfr";
	toto = newOS(nom, MAXPAGEOS, TAILLEPAGE);
	
	p1 = newPage(321, TAILLEPAGE, 54321);
	p2 = newPage(42, TAILLEPAGE, 54321);
	p3 = newPage(4242, TAILLEPAGE, 54321);
	p4 = newPage(4243, TAILLEPAGE, 54321);
	
	


    /*get_page(p1, P1);
        
    get_page(p2, P1);

    get_page(p3, P1);

    get_info_process(P1);   
    my_free(P1, toto);
    get_info_process(P1);  */  

    add_page_disque(p1, toto);
    add_page_disque(p2, toto);
    add_page_disque(p3, toto);    
    add_page_swap(p4, toto);
    get_page(p4, P1);
    
    get_info_OS(toto);

    my_malloc(P1, toto);
    get_info_OS(toto);



    /*printf("SWAP OUT\n");
    swap_out(p4, toto);
    swap_out(p2, toto);*/
    
   /* printf("SWAP IN\n");
    swap_in(p4, toto);
    swap_out(p4, toto);*/
    
//    swap_in(p3, toto);
    
	//get_info_process(P1);

	//release_page(p2, P1);
	//get_info_process(P1);


/*
    //my_malloc(P1, toto);
//    int i;
  //  for(i = 0; i < MAXPAGEOS; i++){
    //    int ID = (((toto->pdisque)[i])->ID);
      //  printf("MAIN ID : %i\n", ID);
    //
  //  }*/
    
	printf("DONE.\n");

	return 0;
}
