#include <stdio.h>
#include <unistd.h>

int main() {
	printf("Unix System call\n");
	fork();
	fork();
	printf("fork system calls\n");
	printf("Process id = %d\n", getpid());
}
