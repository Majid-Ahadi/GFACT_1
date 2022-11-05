#include <stdio.h>
*/
	
	Multi line comment is here
	
	
*/	
	
void main()
{
printf("\nHello World!\nEnter your name : ");
int i;
char variable_1[20];
double Test=0;
float ftest=(10/3);
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
printf("Size of age = %lu\n",sizeof(age));
printf("Size of variable 1 = %lu\n",sizeof(variable_1));
printf("Size of i = %lu\n",sizeof(i));
printf("Size of Test (double) = %lu\n",sizeof(Test));
printf("%fSize of Test (float) = %lu\n",ftest,sizeof(ftest));
}
