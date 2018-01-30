#include <stdio.h>


int chlong(char *pchHello){
    int compteur = 0;
    while(*(pchHello+compteur) != '\0'){
        compteur++;
    }
    //printf("TOTO");
    return compteur;
}


/*int main(){

    char *pChar = "AaBbCcDd";
    printf("La chaine \"%s\" a %i caracteres.\n", pChar, chlong(pChar));
    return 0;
}*/
