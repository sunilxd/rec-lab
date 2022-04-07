#include <stdio.h>
#include <unistd.h>

int main () {
	pid_t p;
	p = fork();

	if (p<0)
		printf("Error in creating the process\n");
	else if (p==0)
		prinf("Child process is executing process id = %d, parendt process is %d\n", getpid(), getppid());
	else
		prinf("Parent process is executing = %d\n", getppid());
