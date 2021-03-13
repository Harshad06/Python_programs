from googletrans import Translator

translator = Translator()

output = translator.translate("Hello Joy. I love python programming.", dest="fr")

print(output.text)