makeWord = input('Enter a word or phrase:')
def makePig(original):
    countWords = 0
    countLetters = 0
    i = []
    original = original.split()
    for word in (original):
        word = word.lower()
        countLetters = 0
        for x in word:
            if (x=='a')|(x=='e')|(x=='i')|(x=='o')|(x=='u'):
                break;
            else:
                countLetters += 1
        for x in word:
            if (not(x.isalpha())):
                word = word.replace (x,"")
        if (countLetters == 0):
            first = None
            pig = 'way'
            new_word = word + pig
        else:
            pig = 'ay'
            first = word[0:(countLetters)]
            new_word = word + first + pig
        new_word = new_word[countLetters:len(new_word)]
        i.insert(countWords, new_word)
        countWords += 1
    print (" ".join(i))
makePig(makeWord)
