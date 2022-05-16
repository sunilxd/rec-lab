#include<stdio.h>
#include<sys/ipc.h>
#include<sys/shm.h>
#include<string.h>
#include<unistd.h>
void main()
{
int child,i,shmid;
char *shmadd,buff[100];
child=fork();
if(!child)
{
shmid=shmget(1041,32,0666|IPC_CREAT);
printf("Key of shared memory is %d\n",shmid);
shmadd=shmat(shmid,0,0);
printf("Process attached at %p\n",shmadd);
printf("PARENT IS WRITING\n");
printf("Enter some data to write to shared memory\n");
read(0,buff,100);
strcpy(shmadd,buff);
}
else
{
sleep(5);
shmid=shmget(1041,32,0666);
printf("Key of shared memory is %d\n",shmid);

shmadd=shmat(shmid,0,0);
printf("Process attached at %p\n",shmadd);
printf("CHILD IS READING\n");
printf("Data read from shared memory is : %s\n",(char *)shmadd);
shmdt(NULL);
shmctl(shmid,IPC_RMID,0);
}
}
