from translate import Translator
import translate


s = Translator(from_lang="pt-br", to_lang="english")


recebe = s.translate(input("Digite a Frase que queira traduzir: "))


print(recebe)