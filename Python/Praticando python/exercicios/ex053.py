frase = str(input('Insira a frase:')).upper().replace(" ", "")
frase_nova = frase[:: - 1].replace(" ", "").upper()
print(f'O iverso de {frase} é {frase_nova}.')
if frase == frase_nova:
    print('Sua frase é um palindromo')
else:
    print('Sua frase não é um palindromo')