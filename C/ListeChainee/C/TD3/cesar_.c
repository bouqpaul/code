#include <stdio.h>
#include <stdlib.h>

int char2int(char c){return c;}
char int2char(int x){return x;}

int c2m(char c){
    int x = char2int(c);
    return x - 97;
}

char m2c(int x){
    char c = int2char(x + 97);
    return c;
}

char addc(char x, char y){
    int a = c2m(x);
    int b = c2m(y);
    int temp = (a + b) % 26;
    char c = m2c(temp);
    return c;
}


char* chiffrement (char* str, char cle){
    int indice = 0;
    int tailleStr = 0;
    
    while(*(str + tailleStr) != '\0'){
        tailleStr++;
    }
    
    char temp = *str;
    char* code = malloc(sizeof(char) * (tailleStr + 1));
    while(temp != '\0'){
        char c = addc(temp, cle);
        code [indice] = c;
        indice++;
        temp = *(str + indice);
    }
    //code [indice + 1] = '\0';
    return code;
}

int main(){
    char* message = "lacleestsouslepaillasson";
    char cle = 'u';
    char* code = chiffrement(message, cle);
    printf ("Message: %s\nCode: %s\n", message, code);
    free(code);
    return 0;
}
