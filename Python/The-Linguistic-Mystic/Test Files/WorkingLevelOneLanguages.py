#Kira Parker
import goslate
import random
userRequestForTranslation = input("What would you like to translate?")
translator = goslate.Goslate()
availableLanguages = translator.get_languages()
#print(AvailableLanguages)
levelOneLanguageCodes = ["fr","es","el","ru","zh-CN","ar"]
levelOneLanguages = ["french","spanish","greek","russian","chinese","arabic"]
i = random.choice(levelOneLanguageCodes)
print(translator.translate(userRequestForTranslation,i))
whatLanguageIsIt = input("What language was it translated to?")
guessedLanguageLowerCase = whatLanguageIsIt.lower()
languageLocation = levelOneLanguageCodes.index(i)
if(guessedLanguageLowerCase == levelOneLanguages[languageLocation]):
    print("correct")
else:
    print("incorrect")
