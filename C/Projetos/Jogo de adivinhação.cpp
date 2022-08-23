#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main(void){
	setlocale(LC_ALL, "Portuguese");
	printf("************************************\n");
	printf("* Bem-vindo ao Jogo da Adivinha��o *\n");
	printf("************************************\n");
	
	int numero_secreto, chute;
	numero_secreto = 5;
	printf("Qual �  o seu chute?: ");
	scanf("%d",&chute);
	printf("Seu chute foi %d!\n", chute);
	int acertou = chute == numero_secreto;
	if(acertou){
		printf("Parab�ns! voc� acertou!\n");
		printf("Jogue de novo, voc� � um bom jogador :)\n");
	}else{
		printf("Voc� errou :(\n");
		printf("Mas n�o desanime, tente de novo!\n");
		if(chute > numero_secreto){
			printf("Seu n�mero foi maior que o n�mero secreto!\n");
		}
		if(chute < numero_secreto){
			printf("Seu n�mero foi menor que o n�mero secreto!\n");
		}
	}


}
