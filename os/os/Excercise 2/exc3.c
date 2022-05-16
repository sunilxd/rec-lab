#include<stdio.h>
#include<unistd.h>
int main()
{
printf("Unix System Call\n");
fork();
fork();
fork();
printf("fork system call\n");
printf("Process id = %d\n", getpid());
}
