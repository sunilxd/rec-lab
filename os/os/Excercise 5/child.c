#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
int main()
{
int pid;
pid=fork();
if(pid == 0)
printf("Child Process is in execution ... Process ID = %u and Parent PID =%u\n",getpid(),getppid());
else
printf("Parent Process is in execution .. Process Id = %u\n",getpid());
return 0;
}
