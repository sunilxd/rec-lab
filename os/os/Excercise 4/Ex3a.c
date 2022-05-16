#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>
#include<sys/types.h>
#include<stdlib.h>
#include<string.h>
int main()
{
char str[20],ch[1];
int c=0,i=0,l,fd;
fd=open("Sample.txt",O_RDWR,O_APPEND);
if(fd==-1)
{
printf("\n Error!");
exit(1);
}
while(c==0)
{
fflush(stdin);
printf("\n Enter the text:");
scanf("%s",str);
strcat(str,"\n");
write(fd,str,strlen(str));
fflush(stdin);
printf("Press 0 to continue");
scanf("%d",&c);
}

close(fd);
fd = open("Sample.txt",O_RDONLY);
printf("\nContent of File: ");
while(read(fd,ch,1)>0)
printf("%c",ch[i]);
close(fd);
}
