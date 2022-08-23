frase = str(input('Insira a frase: ')).upper().strip()
print('A letra A aparece ', frase.count('A'), 'Vezes')
print(f'A primeira letra A apareceu na posição', frase.find('A') + 1)
print(f'A última letra A aparece na posição', frase.rfind('A') + 1)