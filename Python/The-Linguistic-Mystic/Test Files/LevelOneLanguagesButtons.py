#BY KIRA
import goslate
import random
from tkinter import *
#first window that lets you input phrase for translation and press go
top = Tk()
top.minsize(500,500)
translator = goslate.Goslate()
levelOneLanguageCodes = ["fr","es","el","ru","zh-CN","ar"]
levelOneLanguages = ["french","spanish","greek","russian","chinese","arabic"]
i = random.choice(levelOneLanguageCodes)
startLabel = Label(top, text = "Enter phrase to be translated")
startLabel.pack()
E = Entry(top)
E.pack()
def startTranslation():
    global userRequestForTranslation
    userRequestForTranslation = E.get()
    top.destroy()
startButton = Button(top,text = "GO",command = startTranslation)
startButton.pack()
top.mainloop()

#second window that has translated phrase and language button options
top = Tk()
top.minsize(500,500)
translation = translator.translate(userRequestForTranslation,i)
printTranslation = Label(top, text=translation)
printTranslation.pack()
languageLocation = levelOneLanguageCodes.index(i)
levelOneWrongLanguages = levelOneLanguages[:]
del levelOneWrongLanguages[languageLocation]
random.shuffle(levelOneWrongLanguages)

def correctCallBack():
    global correctness
    correctness = "Correct"
    top.destroy()

def incorrectCallBack():
    global correctness
    correctness = "Incorrect"
    top.destroy()

correct = Button(top, text = levelOneLanguages[languageLocation],command = correctCallBack)
incorrect = Button(top, text = levelOneWrongLanguages[0],command = incorrectCallBack)
incorrect2 = Button(top, text = levelOneWrongLanguages[1],command = incorrectCallBack)
incorrect3 = Button(top, text = levelOneWrongLanguages[2],command = incorrectCallBack)
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
