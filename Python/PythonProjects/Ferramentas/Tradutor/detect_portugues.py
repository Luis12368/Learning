from translate import Translator
import translate
import pyttsx3

robo = pyttsx3.init()

idioma = input(str('Digite a sigla do idoma a ser traduzido, ex "Pt-br", "ru-ru", "pl-pl": '))

translator = Translator(from_lang=(idioma), to_lang="pt-br")


translation = translator.translate(input(str("Digite a Frase que queira traduzir: ")))


robo.say(translation)
robo.runAndWait()