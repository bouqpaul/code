#include <stdio.h>
#include "chlong_.c"



int chcopie(char chSrc []){
    int debutMot = 0;
    int finMot = 0;
    int indice = 0;
    char test = chSrc [indice];
    while(test == ' ' && debutMot == 0){
        indice++;
        test = chSrc[indice];
    }
    debutMot = indice;
    test = chSrc[debutMot];
    while(test != '\0'){
    if(test != ' '){finMot = indice;}
        indice++;
        test = chSrc[indice];
    }
    char chDest [finMot-debutMot+1];
    int i = 0;
    int j;
    for(j = debutMot; j <= finMot; j++){
        chDest [i] = chSrc[j];
        i++;
    
    }
    chDest[i+1] = '\0';
    printf("%s\n", chDest);
    return 0; 
}

/*int main (){
    char chaine [] = "Aa Bb  Cc  Dd";
    printf ("%i\n", chcopie(chaine));
    return 0;
}*/
