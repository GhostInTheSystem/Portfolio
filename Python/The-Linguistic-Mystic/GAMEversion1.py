#Made By Kira
#Debugged by Alex, Otis, and Preston
# -*- coding: utf-16 -*-
from __future__ import print_function
from __future__ import unicode_literals
from googleapiclient.discovery import build
import random
from Tkinter import *
import os
import json
service = build('translate', 'v2',
            developerKey='AIzaSyBUQS5Uc1v8Iq8kTbSkhdnNPkF6icsBG3w')
timesThrough = 0
#as long as you get the translation right you can play again and again
correctness = "Correct"
def changeWindowIcon(windowName):
    iconLocation = os.path.dirname(os.path.realpath(__file__)) + "\Icon1.ico"
    windowName.iconbitmap(r'' + iconLocation)
def windowSettings(windowName):
    top.minsize(500,500)
    top.wm_title("The Linguistic Mystic")
    h = 500
    w = 500
    ws = top.winfo_screenwidth()
    hs = top.winfo_screenheight()
    x = (ws/2) - (h/2)
    y = (hs/2) - (h/2)
    windowName.geometry('%dx%d+%d+%d' % (w, h, x, y))
levelOneLanguageCodes = ["fr", "es", "el", "ru", "zh", "ar"]
levelTwoLanguageCodes = ["de", "ja", "la", "it", "sv"]
levelThreeLanguageCodes = ["fi", "ko", "iw", "ga", "is", "ro"]
levelFourLanguageCodes = ["af", "vi", "hi", "th", "ta", "no"]
levelFiveLanguageCodes = ["fa", "bg", "uk", "zh-TW","mn","ka","km", "yi", "tg"]
levelOneLanguages = ["French", "Spanish", "Greek", "Russian", "Chinese", "Arabic"]
levelTwoLanguages = ["German", "Japanese", "Latin", "Italian", "Swedish"] + levelOneLanguages
levelThreeLanguages = ["Finnish", "Korean", "Hebrew", "Irish", "Icelandic", "Romanian"] + levelTwoLanguages
levelFourLanguages = ["Afrikaans", "Vietnamese", "Hindi", "Thai", "Tamil", "Norwegian"] + levelThreeLanguages
levelFiveLanguages = ["Persian", "Bulgarian", "Ukrainian", "Traditional Chinese", "Mongolian",
                      "Georgian","Khmer","Yiddish","Tajik"] + levelFourLanguages
africaLanguageCodes = ["af","ny","ha","ig","st","so","su","sw","yo","zu"]
africaLanguages = ["Afrikaans","Chichewa","Hausa","Igbo","Sesotho","Somali","Sundanese","Swahili",
                   "Yoruba","Zulu"]
eastAsiaLanguageCodes = ["zh","zh","zh-TW","hmn","ja","km","ko","lo","mn","my","ne","th","vi"]
eastAsiaLanguages = ["Chinese","Chinese (Simplified","Chinese (Traditional","Hmong","Japanese","Khmer","Korean",
                     "Lao","Mongolian","Myanmar","Nepali","Thai","Vietnamese"]
europeLanguageCodes = ["sq","eu","bg","ca","cs","da","nl","fi","fr","gl","de","el","hu","is","ga","it",
                       "mt","no","pl","pt","ro","sk","es","sv","cy","yi"]
europeLanguages = ["Albanian","Basque","Bulgarian","Catalan","Czech","Danish","Dutch","Finnish","French",
                   "Galician","German","Greek","Hungarian","Icelandic","Irish","Italian","Maltese","Norvegian",
                   "Polish","Portuguese","Romanian","Slovak","Spanish","Swedish","Welsh","Yiddish"]
sovietLanguageCodes = ["hy","az","be","et","ka","kk","lv","lt","ru","tg","uk","uz"]
sovietLanguages = ["Armenian","Azerbaijani","Belarusian","Estonian","Georgian","Kazakh","Latvian","Lithuanian",
                   "Russian","Tajik","Ukrainian","Uzbek"]
indiaLanguageCodes = ["bn","gu","hi","kn","ml","mr","pa","si","ta","te","ur"]
indiaLanguages = ["Bengali","Gujarati","Hindi","Kannada","Malayalam","Marathi","Punjabi","Sinhala","Tamil",
                  "Telugu","Urdu"]
wildcardLanguageCodes = ["ar","iw","fa","tr","ceb","tl","id","jw","mg","ml","mi","eo","ht","la"]
wildcardLanguages = ["Arabic","Hebrew","Persian","Turkish","Cebuano","Filipino","Indonesian","Javanese","Malagasy",
                     "Malay","Maori","Esperanto","Haitian Creole","Latin"]
score = 0
levelFiveComplete = False

while(correctness == "Correct"):
    if(timesThrough == 0):
        correctness = 0
        #first window that lets you input phrase for translation and press go
        top = Tk()
        windowSettings(top)
        changeWindowIcon(top)
        ###translator = goslate.Goslate()
        ###availableLanguages = translator.get_languages()
        #print(availableLanguages)
        startLabel1 = Label(top, text = "Hello, welcome to The Linguistic Mystic!")
        startLabel2 = Label(top, text = "First, enter some text.")
        startLabel3 = Label(top, text = "Then, choose a level. Level 1 is the easiest, level 5 is the hardest.")
        startLabel4 = Label(top, text = "If you beat level 5, you unlock levels based on different regions.")
        startLabel5 = Label(top, text = "The text you entered will be translated into different languages")
        startLabel6 = Label(top, text = "You have to guess what language, among the four options, it is.")
        startLabel7 = Label(top, text = "Let's do it!!!!!")
        unlockedLabel1 = Label(top, text = "The language regions have been unlocked.")
        unlockedLabel2 = Label(top, text = "Enter a new phrase to be translated and select a level.")
        if (levelFiveComplete == False):
            startLabel1.pack()
            startLabel2.pack()
            startLabel3.pack()
            startLabel4.pack()
            startLabel5.pack()
            startLabel6.pack()
            startLabel7.pack()
        else:
            unlockedLabel1.pack()
            unlockedLabel2.pack()
        E = Entry(top)
        E.pack()

        #make drop down menu for language level selection
        var = StringVar(top)
        var.set("select a level")

        if (levelFiveComplete == False):
            languageOption = OptionMenu(top, var,"1","2","3","4","5")
        else:
            languageOption = OptionMenu(top, var,"1","2","3","4","5","Africa","East Asia","Europe","Former Soviet State",
                                    "India","Wild Card")
        if(timesThrough == 0):
            languageOption.pack()
            E.pack()
        if(timesThrough == 10):
            languageLevel  = str(int(languageLevel)+1)
            score += 10
            timesThrough = 0

        def startTranslation():
            global languageLevel
            global userRequestForTranslation
            userRequestForTranslation = E.get()
            if(timesThrough == 0):
                languageLevel = var.get()
            top.destroy()
        startButton = Button(top,text = "Play!",command = startTranslation, height = 3, width = 30)
        startButton.pack()
        top.mainloop()

    if(languageLevel == "select a level"):
        languageLevel = "1"
    if (languageLevel == "1"):
        i = random.choice(levelOneLanguageCodes)
        languageCodes = levelOneLanguageCodes
        languages = levelOneLanguages
    if (languageLevel == "2"):
        i = random.choice(levelTwoLanguageCodes)
        languageCodes = levelTwoLanguageCodes
        languages = levelTwoLanguages
    if (languageLevel == "3"):
        i = random.choice(levelThreeLanguageCodes)
        languageCodes = levelThreeLanguageCodes
        languages = levelThreeLanguages
    if (languageLevel == "4"):
        i = random.choice(levelFourLanguageCodes)
        languageCodes = levelFourLanguageCodes
        languages = levelFourLanguages
    if (languageLevel == "5"):
        i = random.choice(levelFiveLanguageCodes)
        languageCodes = levelFiveLanguageCodes
        languages = levelFiveLanguages
    if (languageLevel == "African"):
        i = random.choice(africaLanguageCodes)
        languageCodes = africaLanguageCodes
        languages = africaLanguages
    if (languageLevel == "East Asia"):
        i = random.choice(eastAsiaLanguageCodes)
        languageCodes = eastAsiaLanguageCodes
        languages = eastAsiaLanguages
    if (languageLevel == "Europe"):
        i = random.choice(europeLanguageCodes)
        languageCodes = europeLanguageCodes
        languages = europeLanguages
    if (languageLevel == "Former Soviet State"):
        i = random.choice(sovietLanguageCodes)
        languageCodes = sovietLanguageCodes
        languages = sovietLanguages
    if (languageLevel == "India"):
        i = random.choice(indiaLanguageCodes)
        languageCodes = indiaLanguageCodes
        languages = indiaLanguages
    if (languageLevel == "Wild Card"):
        i = random.choice(wildcardLanguageCodes)
        languageCodes = wildcardLanguageCodes
        languages = wildcardLanguages

    #second window that has translated phrase and language button options
    top = Tk()
    windowSettings(top)
    changeWindowIcon(top)
    correctness = 0
    translator = (service.translations().list(
        source='en',
        target=i,
        q=[userRequestForTranslation]
    ).execute())
    translator = str(translator)
    
    countI = 0
    translationStart = 0
    translationEnd = 0
    while countI<(len(translator)-2):
        if(translator[countI]==':' and translator[countI+1]==' ' and translator[countI+2]=='u'):
            translationStart = countI + 4
        countI += 1
    countJ = 2
    while countJ<(len(translator)-2):
        if(translator[countJ]=='}'and translator[countJ+1]==']' and translator[countJ+2]=='}'):
            translationEnd = countJ -1
        countJ +=1
    translation = translator[translationStart:translationEnd]
    translation2 = translation.decode("unicode_escape")
    printTranslation = Label(top, text=translation2)
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
    buttonList = [correct,incorrect,incorrect2,incorrect3]
    random.shuffle(buttonList)
    for element in buttonList:
        element.pack()

    top.mainloop()

    #third window that shows if the answer is correct or not - should have option to play again or something
    if (userRequestForTranslation.lower() == "trutle"):
            timesThrough = 9
            correctness = "Correct"
            languageLevel = "5"
    top = Tk()
    windowSettings(top)
    changeWindowIcon(top)
    def playAgain():
        top.destroy()
    showCorrectness = Label(top,text = correctness)
    showCorrectness.pack()
    playagain = Button(top, text = "CONTINUE",command = playAgain,height = 3, width = 30,bg = "green")
    mainmenu = Button(top, text = "MAIN MENU",command = playAgain,height = 3, width = 30,bg = "green")
    gameOver = Label(top,text = "GAME OVER",bg="red",fg="white")
    showScore = Label(top, text = "Your Score is: " +str(timesThrough + score))
    youWin = Label(top,text = "YOU WIN!!!!!!!")
    regionsUnlock = Label(top,text = "Regions have been unlocked!")
    regionsUnlock2 = Label(top,text = "The cheat code to unlock regions in the future is trutle")
    if(correctness  == "Correct"):
        if(timesThrough != 9):
            playagain.pack()
        if((timesThrough%10 == 9) and (languageLevel == "1" or languageLevel == "2" or languageLevel ==  "3" or languageLevel == "4")):
            levelUp = Label(top, text = "Congratulations! You are moving up to level "+str(int(languageLevel)+1))
            levelUp.pack()
            add = int(languageLevel)
            add += 1
            languageLevel = str(add)
            playagain.pack()
        if(timesThrough == 9 and languageLevel == "5"):
            youWin.pack()
            regionsUnlock.pack()
            regionsUnlock2.pack()
            levelFiveComplete = True
            timesThrough = -1
            mainmenu.pack()
    else:
        gameOver.pack()
        showScore.pack()
    top.mainloop()
    timesThrough += 1
