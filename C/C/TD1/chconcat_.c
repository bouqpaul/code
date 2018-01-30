#include <stdio.h>
//#include "chcopie_.c"
#include "chlong_.c"

int chconcat(char chDest [], char chSrc []){
    int tailleDest = chlong(chDest);
    int tailleSrc = chlong(chSrc);
    char newchDest [tailleDest + tailleSrc + 1];
    int indice;
    for(indice = 0; indice < tailleDest + tailleSrc; indice++){
        if(indice < tailleDest){
            newchDest[indice] = chDest[indice];
        } else {
            newchDest[indice] = chSrc[indice-tailleDest];
        }
        
    }
    newchDest[tailleDest + tailleSrc] = '\0';
    printf ("%s\n", newchDest);
    return 0;


}




/*int main(){
char ch1 [] = "ABCD";
char ch2 [] = "abcd";
chconcat(ch1, ch2);
return 0;
}*/
