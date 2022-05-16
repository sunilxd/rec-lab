#include<stdio.h>
#include<unistd.h>
int main()
{
printf("Current program PID = %d\n", getpid());
char *a[]={"./add",NULL};
execv(a[0],a);
printf("Back to current process");
}

