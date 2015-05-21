#Made By Kira
import goslate
import random
from tkinter import *
#first window that lets you input phrase for translation and press go
top = Tk()
top.minsize(500,500)
translator = goslate.Goslate()
availableLanguages = translator.get_languages()
#print(availableLanguages)
levelOneLanguageCodes = ["fr","es","el","ru","zh-CN","ar"]
levelTwoLanguageCodes = ["de","ja","la","es","it","sv"]
levelOneLanguages = ["french","spanish","greek","russian","chinese","arabic"]
levelTwoLanguages = ["german","japanese","latin","spanish","italian","swedish"]
startLabel = Label(top, text = "Enter phrase to be translated")
startLabel.pack()
E = Entry(top)
E.pack()

#make drop down menu for language level selection
var = StringVar(top)
var.set("select a level")

languageOption = OptionMenu(top, var,"1","2")
languageOption.pack()

def startTranslation():
    global languageLevel
    global userRequestForTranslation
    userRequestForTranslation = E.get()
    languageLevel = var.get()
    top.destroy()

startButton = Button(top,text = "GO",command = startTranslation, height = 3, width = 30)
startButton.pack()
top.mainloop()

#second window that has translated phrase and language button options
top = Tk()
top.minsize(500,500)
if (languageLevel == "1"):
    i = random.choice(levelOneLanguageCodes)
    languageCodes = levelOneLanguageCodes
    languages = levelOneLanguages
    print(i)
if (languageLevel == "2"):
    i = random.choice(levelTwoLanguageCodes)
    languageCodes = levelTwoLanguageCodes
    languages = levelTwoLanguages
    print(i)
translation = translator.translate(userRequestForTranslation,i)
printTranslation = Label(top, text=translation)
printTranslation.pack()
languageLocation = languageCodes.index(i)
wrongLanguages = languages[:]
del wrongLanguages[languageLocation]
random.shuffle(wrongLanguages)

def correctCallBack():
    global correctness
    correctness = "Correct"
    top.destroy()

def incorrectCallBack():
    global correctness
    correctness = "Incorrect"
    top.destroy()

correct = Button(top, text = languages[languageLocation],command = correctCallBack)
incorrect = Button(top, text = wrongLanguages[0],command = incorrectCallBack)
incorrect2 = Button(top, text = wrongLanguages[1],command = incorrectCallBack)
incorrect3 = Button(top, text = wrongLanguages[2],command = incorrectCallBack)
#this is awkward but i couldn't figure out how else to randomize the order of the buttons
buttonList = [correct,incorrect,incorrect2,incorrect3]
random.shuffle(buttonList)
for element in buttonList:
    element.pack()

top.mainloop()

#third window that shows if the answer is correct or not - should have option to play again or something
top = Tk()
top.minsize(500,500)
showCorrectness = Label(top,text = correctness)
showCorrectness.pack()
top.mainloop()


