#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>


int main(){
char * cmd [5];
cmd[0] = "ls";
cmd[1] = "-l";
cmd[2]=NULL;
execvp("ls", cmd);
printf("T");
return 0;
}
