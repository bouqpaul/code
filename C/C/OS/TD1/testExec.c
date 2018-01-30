#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>


int main(){
    int string;
    string = 42;
    int ret;
    int code_retour;
    char * cmd [3];
    code_retour = fork();
    
    switch (code_retour){
        case -1 :
            printf("Pbm lors de la creation du processus.\n");
            break;
            
        case 0 :
            printf("CHOIX: lister(0) - lister les droits(1) - Manuel gcc(2)\n");
            printf("Commande: ");
            scanf("%i", &string);
            switch(string){
                case 0 :
                    printf("CHOIX 0 \n");
                    cmd[0] = "ls";
                    cmd[1] = "-a";
                    cmd[2] = NULL;
                    execvp("ls", cmd);
                    break;
                    
                case 1:
                    printf("CHOIX 1 \n");
                    cmd[0] = "ls";
                    cmd[1] = "-l";
                    cmd[2] = NULL;
                    execvp("ls", cmd);
                    break;
                    
                case 2 :
                    printf("CHOIX 2 \n");
                    cmd[0] = "man";
                    cmd[1] = "gcc";
                    cmd[2] = NULL;
                    execvp("man", cmd);
                    break;
                    
                default:
                    printf("CHOIX non valide.\n");
                    break;
            
            }
            break;
            
        default:
            wait(&ret);
            cmd[0] = "testExec";
            cmd[1] = NULL;
            execvp("testExec", cmd);
            printf("Fail.\n");
            break;
            
    return 0;
}
