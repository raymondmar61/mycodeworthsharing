#A shift code is where a message can be easily encoded and is one of the simplest codes to use. Each letter is moved forwards through the alphabet a set number of letters to be represented by a new letter. For instance, “abc” becomes “bcd” when the code is shifted by one (i.e. each letter in the alphabet is moved forward one character).
alphabetlist = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def getinput():
    word = input("Enter your message: ")
    word = word.lower()
    changenumber = ""
    while True:
        changenumber = int(input("Enter a number between 1 and 26: "))
        if changenumber >= 1 and changenumber <= 26:
            break
        else:
            print(changenumber, "is out of range")
            continue
    return(word, changenumber)


def makeacode(originalword, changenumber):
    codedword = []
    for eachoriginalword in originalword:
        alphabetlistindexnumber = alphabetlist.index(eachoriginalword)
        if alphabetlistindexnumber == 0:
            codedword.append(eachoriginalword)
        elif alphabetlistindexnumber + changenumber > 26:
            shiftindexnumber = abs(26 - alphabetlistindexnumber - changenumber)
            codedword.append(alphabetlist[shiftindexnumber])
        else:
            shiftindexnumber = alphabetlistindexnumber + changenumber
            codedword.append(alphabetlist[shiftindexnumber])
    print("".join(codedword))

def decodeaword(decodedword, changenumber):
    originalword = []
    for eachdecodedword in decodedword:
        alphabetlistindexnumber = alphabetlist.index(eachdecodedword)
        if alphabetlistindexnumber == 0:
            originalword.append(eachdecodedword)
        elif alphabetlistindexnumber - changenumber == 0:
            originalword.append(alphabetlist[-1])
        elif alphabetlistindexnumber - changenumber < 0:
            originalword.append(alphabetlist[26 + (alphabetlistindexnumber - changenumber)])
        else:
            originalword.append(alphabetlist[alphabetlist.index(eachdecodedword) - changenumber])
    print("".join(originalword))


while True:
    try:
        print("\n1) Make a code\n2) Decode a message\n3) Quit")
        userinput = int(input("Enter your selection: "))
    except ValueError:
        print("Invalid.  Enter a number 1, 2, or 3\n")
        continue
    if userinput == 1:
        (word, changenumber) = getinput()
        makeacode(word, changenumber)
    elif userinput == 2:
        (word, changenumber) = getinput()
        decodeaword(word, changenumber)
    elif userinput == 3:
        break
    else:
        print(userinput, "is an invalid number\n")
