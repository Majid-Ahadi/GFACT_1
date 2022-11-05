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

printf("\nYour name is : ");

for(i=0;i<20;i++)
	printf("%c",variable_1[i]);

printf("\n");
}
