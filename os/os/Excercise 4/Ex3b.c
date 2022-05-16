#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<string.h>
#include<stdlib.h>
void main()
{
int fd1,fd2;
char ch[1];
fd1=open("Sample.txt",O_RDONLY);
fd2=open("New.txt",O_RDWR|O_APPEND);
while(read(fd1,ch,1)>0)
{
write(fd2,ch,1);
}
close(fd2);
close(fd1);

fd2=open("New.txt",O_RDONLY);
while(read(fd2,ch,1)>0)
{
printf("%c",ch[0]);
}
close(fd2);
}
