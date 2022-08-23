from translate import Translator
import translate
import pyttsx3

robo = pyttsx3.init()


translator = Translator(from_lang="pt-br", to_lang="de-DE")


translation = translator.translate(input(str("Digite a Frase que queira traduzir: ")))


robo.say(translation)
robo.runAndWait()