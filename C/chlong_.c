#include <stdio.h>

int chlong (char chaine []){
	int resul = 0;
	char toto = chaine [resul];
	while (toto != '\0'){
		resul++;
		toto = chaine [resul];
	}

return resul;
}



/*int main (void){

char toto [] = "ABCDEFGHIF\0";
int l = chlong (toto);

printf ("Taille de la chaine \"%s\" : %d \n", toto, l);

return 0;
}*/
