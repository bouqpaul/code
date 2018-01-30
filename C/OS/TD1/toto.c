#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>

int main(){
    int code_retour ;
    char string[4];
    int id, pid;
    char * path = "/home5/bouquepa/C/OS/TD1/ABC.txt";
    int fd;
    code_retour = fork() ;
    fd = open(path, O_RDWR);
    switch (code_retour) {
        case -1 :
            printf("Pbm lors de la creation du processus.\n");
            break;
        case 0 :
            write(fd, "Fils", sizeof(char) * 4);
            sleep(2);
            read(fd, string, sizeof(char) * 4);
            printf("Lecture Fils: %s", string);    
            /*sleep(3);
            id = getpid();
            pid = getppid();
            printf("Je suis le processus fils: %d\n. Père: %d\n", id, pid);*/
           
            break;
        default :
            sleep(1);
            read(fd, string, sizeof(char) * 4);
            printf("Lecture Pere: %s", string);
            write(fd, "Pere", sizeof(char) * 4);
            
            /*id = getpid();
            printf("Je suis le processus père: %d\n", id);
            printf("Je viens de créer le processus fils dont le pid est %d.\n",code_retour);*/
            break;
        }
    close(fd);
    return 0;
}
