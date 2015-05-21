import goslate
import random
userRequestForTranslation = input("What would you like to translate?")
Translator = goslate.Goslate()
AvailableLanguages = Translator.get_languages()
print(AvailableLanguages)
LevelOneLanguages = ["el", "it", "sv", "fr", "ja"]
i = random.choice(LevelOneLanguages)
print(Translator.translate(userRequestForTranslation, i))
WhatLanguageIsIt = input("What language was it translated too?")
#Made by ALEX TINGEY
