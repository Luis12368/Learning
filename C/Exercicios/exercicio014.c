/* esse programa vai ler 5 numeros e armazenalos em um vetor.
vai copiar para um segundo vetor, com as seguintes regras:
*Se o n�mero for par, preencha a mesma posi��o do segundo vetor com o
n�mero sucessor do contido na mesma posi��o do primeiro vetor.
*Se o n�mero for �mpar, preencha a mesma posi��o do segundo vetor com o n�mero 
antecessor do contido na mesma posi��o do primeiro vetor.*/

#include <stdio.h>

int main(){
const int tamvet=5;
int vet1[tamvet],vet2[tamvet], posicao;
for (posicao=0; posicao<tamvet;posicao++){
	scanf("%d",&vet1[posicao]);
	if(vet1[posicao]%2 == 0){
		vet2[posicao] = vet1[posicao]+1;
	}else{
		vet2[posicao] = vet1[posicao]-1; 
	}
		
}
printf("Elementos do Vetor1 e Vetor2: ");
for (posicao=0; posicao<tamvet;posicao++){
	printf("%d ", vet1[posicao]);
	printf("%d ", vet2[posicao]);
}


return 0;	
	
	
}
