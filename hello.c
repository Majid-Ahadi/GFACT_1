#include <stdio.h>

void main()
{
printf("\nHello World!\nEnter your name : ");
int i;
char variable_1[20];

for (i=0;i<20;i++)
	variable_1[i]=' ';
//	printf("%c",variable_1[i]);}

//for (i=0;i<20;i++)
scanf("%s", variable_1);

int age=0;

printf("How Old are you %s ? ",variable_1);
scanf("%d",&age);

printf("\nYour name is : ");

//for(i=0;i<20;i++)
	printf("%s",variable_1);

printf(" and you are %d years old !\n",age);
}
