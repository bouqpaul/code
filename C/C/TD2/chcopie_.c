#include <stdio.h>
#include "chlong_.c"


int chcopie(char *pSrc){
    int tailleSrc = chlong(pSrc);
    int debut = 0;
    int fin = tailleSrc - 1;
    while(*(pSrc + debut) == ' '){
        debut++;
    }
    while(*(pSrc + fin) == ' '){
        fin--;
    }
    printf("%c\n%c\n", *(pSrc+debut), *(pSrc+fin));
    return 1;
}

int main(){
    char *pChar = "  Z    Aa Bb cC    z ";
    chcopie(pChar);
    return 0;


}
