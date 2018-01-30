#include <stdio.h>
#include "chlong_.c"

int chnmotif(char chMotif [], char chCher []){    
    int compteur = 0;
    int iCher = 0;
    int iMotif;
    int tailleMotif = chlong(chMotif);
    while(chCher[iCher] != '\0'){
        int old = iCher;
        while(chCher[iCher] == chMotif[iMotif]){
            iMotif++;
            iCher++;
        }
        if(iMotif == tailleMotif){compteur++;}
        printf ("%c\n", chCher[iCher]);
        iMotif = 0;
        iCher = old;
        iCher++;

    }   

    return compteur;
}



int main(){
char motif [] = "ra";
char cher [] = "Abracadabra";
printf ("%i motif \"%s\" dans \"%s\"\n", chnmotif(motif, cher), motif, cher);
return 0;
}
