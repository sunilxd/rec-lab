#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
int main()
{
int pid = fork();
if (pid > 0)
{
printf("Parent Process ID : %d\n", getpid());
printf("\nProcess Terminated\n");
}
else if (pid == 0)
{
sleep(5);
printf("\nChild process ... ID: %d\n", getpid());
printf("Parent -ID: %d\n\n", getppid());
}
return 0;
}
