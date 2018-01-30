#include <stdio.h>
#include <stdlib.h>
int char2int(char c){return c;}
char int2char(int x){return x;}


int c2m(char x){
	int i = char2int(x);
	return i - 97;
}

char m2c(int i){
	char c = int2char(i + 97);
	return c;
}

char addc(char x, char y){
	int a = c2m(x);
	int b = c2m(y);
	int somme = (a + b) % 26;
	char c = m2c(somme);
	return c;
}

char diffc(char x, char y){
	int a = c2m(x);
	int b = c2m(y);
	int somme = (a - b) % 26;
	if(somme < 0){somme += 26;}
	char c = m2c(somme);
	return c;
}

int len(char* chaine){
	int taille = 0;
	while(*(chaine + taille) != '\0'){
		taille++;		
	}
	return taille;	
}


char* chiffrement(char* message, char cle){
	int indice = 0;
	int tailleMessage = len(message);
	char* code = malloc(sizeof(char) * (tailleMessage + 1));
	char temp = *message;
	
	while(temp != '\0'){
		char chiff = addc(temp, cle);
		code[indice] = chiff;
		indice++;
		temp = *(message + indice);		
	}
	code [tailleMessage + 1] = '\0';
	return code;
}

char cleD(char cle){
	char c = diffc('a', cle);
	return c;
}

char* cesarD(char* mc, char cle){
	char cleDechiff = cleD(cle);
	printf("Cle de dechiffrement: %c\n", cleDechiff);
	char* decode = chiffrement(mc, cleDechiff);
	return decode;
}

void allD(char* message){
	int indice;
	for(indice = 0; indice < 26; indice++){
		char cle = m2c(indice);
		char* temp = chiffrement(message, cle);
		printf("Clef: %c --- Message possible: %s\n", cle, temp);
	}
	
	// return 0;
}

int* frequence(char* mc){
	int tailleMc = len(mc);
	int* freq = malloc(sizeof(int) * 26);
	int indice;
	for(indice = 0; indice <= 26; indice++){
		freq[indice] = 0;
	}
	
	for(indice = 0; indice <= tailleMc; indice++){
		char temp = mc[indice];
		int tempI = c2m(temp);
		freq[tempI]++;
	}
	return freq;
}

char* cleA(char* mc){
	int* freq = frequence(mc);
	int max = freq[0];
	int i;
	for(i = 0; i <= 25; i++){
		if(freq[i] > max){max = freq[i];}		
	}
	char* clePossible = malloc(sizeof(char) * 30);
	for(i = 0; i <= 25; i++){
		if(freq[i] == max){
			char temp = m2c(i);
			printf("ClePossible: %c\n", temp);
			clePossible[i] = temp;}
		
	}
	
	return clePossible;
}

void cesarA(char* mc){
	// int taille = len(mc);
	char* cle = cleA(mc);
	int i;
	for(i = 0; i <= 30; i++){
		char testCle = cle[i];
		printf("TestClef: %c\n", testCle);
		if(testCle){
			char cleDe = cleD(testCle);
			char* decode = cesarD(mc, cleDe);
			printf("Message decode: %s\n", decode);
			}
	}
	// return 0;
}


int main(){
	// char* message = "laclefestsouslepaillasson";
	// char* message = "eczaelcoultopulnlddpfypgtecp";
	
	// char* testC1 = "jljvklulzawhzaylzyvibzal";
	// allD(testC1);
	
	// char* testC2 = "nmtqkqbibqwvadwcaidmhbzwcdmdwcaxwcdmhxiaamzickwlmlmdqomvmzm";
	// allD(testC2);
	// char gg = diffc('e', 'm');
	// char* code = chiffrement(testC2, gg);
	// printf("%s", code);
	// int* toto = frequence(testC2);
	// int i;
	// for(i = 0; i <= 25; i++){
		// char c = m2c(i);
		// printf("%c: %d\n", c, toto[i]);
	// }
	// char cc = cleD('m');
	// printf("Cle?: %c", cc);
	// char* tt = chiffrement(testC2, cc);
	// printf("Message?: %s", tt);
	// char* message = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz";
	// int* f = frequence(message);
	
	// char cle = 'l';
	
	// char* code = cesarD(message, cle);
	// printf("Message: %s\nCode: %s", message, code);
	// int indice;
	// printf("Dans %s, il y a: \n", message);
	// for(indice = 0; indice <= 25; indice++){
		// char t = m2c(indice);
		// int i = f[indice];
		// printf("Il y a %i fois %c\n", i, t);
	// }
	// printf("%d", *(f + 2));
	//free(code);
	return 0;
}
