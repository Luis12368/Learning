#include <stdio.h>
#include <stdlib.h>

int main()
{
int num, maior, cont;
maior = 0;
cont = 1;	
while(cont<=15)
{
	
	printf("Digite um n�mero: ");
    scanf("%d", &num);
    if(num > maior)
	{
    	
    	maior =  num;
	}
    cont++;
}
   printf("o maior numero = %d\n", maior);
  return 0;
}
