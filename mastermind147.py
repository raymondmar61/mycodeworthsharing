#On screen version of Mastermind.  The computer generate four colors from a list of possible colors.  The computer can select the same color more than once.  User enters their choice of four colors from the same list the computer used.  The program checks the user's answers how many correct and how many correct in the wrong position.  User continues guessing.  The end of the game a message displays correct and the number of guesses.
#RM:  I checked part of the solution for the colors used.  Colors used are red, blue, orange, yellow, pink, green, and white.
import random
colorslist = ["red", "blue", "orange", "yellow", "pink", "green", "white"]
# choosefourcolors = random.choices(colorslist, k=4)
# choosefourcolors = ["red", "blue", "yellow", "orange"]
choosefourcolors = ["red", "blue", "red", "green"]
print(choosefourcolors)
print(choosefourcolors.count("red"))
for eachchoosefourcolors in choosefourcolors:
    print(eachchoosefourcolors, choosefourcolors.count(eachchoosefourcolors))
computercolorname = [(eachchoosefourcolors, choosefourcolors.count(eachchoosefourcolors)) for eachchoosefourcolors in choosefourcolors]
print(computercolorname)
# inputfourcolors = input("Enter four colors separated by a space ").split()
inputfourcolors = choosefourcolors
# inputfourcolors = ["red", "blue", "orange", "white"]
# inputfourcolors = ["pink", "blue", "yellow", "red"]
inputfourcolors = ["blue", "blue", "blue", "blue"]
print(inputfourcolors)
for eachinputfourcolors in inputfourcolors:
    print(eachinputfourcolors, inputfourcolors.count(eachinputfourcolors))
inputcolorname = [(eachinputfourcolors, inputfourcolors.count(eachinputfourcolors)) for eachinputfourcolors in inputfourcolors]
print(inputcolorname) #print [('red', 1), ('blue', 1), ('orange', 1), ('yellow', 1)]
print(inputcolorname[2][0]) #print orange
correctcolorcorrectplace = 0
correctcolorwrongplace = 0
for n in range(0, 4):
    print(inputcolorname[n][0], computercolorname[n][0])
    if (inputcolorname[n][0] == computercolorname[n][0]):
        correctcolorcorrectplace += 1
        continue
    # if (inputcolorname[n][0] == computercolorname[n][0]) and (inputcolorname[n][0] in choosefourcolors):
    #     continue
    if inputcolorname[n][0] in choosefourcolors and (inputcolorname[n][0] == computercolorname[n][0]):
        correctcolorwrongplace += 1
        print(inputcolorname[n][0], "is in choosefourcolors list as computercolorname[n]")
        continue
    if inputcolorname[n][0] in choosefourcolors:
        correctcolorwrongplace += 1
    print(correctcolorcorrectplace, correctcolorwrongplace)

print(correctcolorcorrectplace)
print(correctcolorwrongplace)

# inputfourcolors = [eachinputfourcolors.lower() for eachinputfourcolors in inputfourcolors]
# print(inputfourcolors)
# print(inputfourcolors == choosefourcolors)

#Second attempt
computerfourcolors = ["red", "blue", "red", "green"]
userfourcolors = ["pink", "blue", "yellow", "red"]

colorchecklist = []
for n in range(0, 4):
    colorchecklist.append(userfourcolors[n] + computerfourcolors[n])
print(colorchecklist) #print ['pinkred', 'blueblue', 'yellowred', 'redgreen']

colorchecklist = []
correctcolorcorrectplace = 0
correctcolorwrongplace = 0
for n in range(0, 4):
    colorchecklist.append(userfourcolors[n] + computerfourcolors[n])
    if (userfourcolors[n] == computerfourcolors[n]):
        print("correct correct" + userfourcolors[n], computerfourcolors[n])
        correctcolorcorrectplace += 1
    elif (userfourcolors[n] in computerfourcolors) and (userfourcolors[n] + computerfourcolors[n] not in colorchecklist):
        print("correct wrong" + userfourcolors[n], computerfourcolors[n])
        correctcolorwrongplace += 1
print(correctcolorcorrectplace) #print 1
print(correctcolorwrongplace) #print 0  Incorrect.  Answer is 1.


computerfourcolors = ["red", "blue", "red", "green"]
userfourcolors = ["blue", "blue", "blue", "blue"]

colorchecklist = []
correctcolorcorrectplace = 0
correctcolorwrongplace = 0
for n in range(0, 4):
    colorchecklist.append(userfourcolors[n] + computerfourcolors[n])
    if (userfourcolors[n] == computerfourcolors[n]):
        print("correct correct" + userfourcolors[n], computerfourcolors[n])
        correctcolorcorrectplace += 1
    elif (userfourcolors[n] in computerfourcolors) and (userfourcolors[n] + computerfourcolors[n] not in colorchecklist):
        print("correct wrong" + userfourcolors[n], computerfourcolors[n])
        correctcolorwrongplace += 1
print(correctcolorcorrectplace) #print 1
print(correctcolorwrongplace) #print 0

#Third attempt
import random
def computergeneratefourcolors(colorslist):
    computerfourcolors = random.choices(colorslist, k=4)
    return computerfourcolors

def compareusercolorscomputercolors(userfourcolors, computerfourcolors):
    colorcheckedlist = [] #colorcheckedlist to avoid double counting a color already checked
    correctcolorcorrectplace = 0
    correctcolorwrongplace = 0
    for n in range(0, 4):
        if (userfourcolors[n] == computerfourcolors[n]):
            correctcolorcorrectplace += 1
        elif (userfourcolors[n] in computerfourcolors) and (userfourcolors[n] not in colorcheckedlist):
            colorcheckedlist.append(userfourcolors[n])
            correctcolorwrongplace += 1
        elif (userfourcolors[n] != computerfourcolors[n]) and (userfourcolors[n] in colorcheckedlist):
            correctcolorwrongplace -= 1
        if correctcolorwrongplace < 0:
            correctcolorwrongplace = 0
    return correctcolorcorrectplace, correctcolorwrongplace


def mastermind(colorslist):
    print("Let's play Mastermind")
    computerfourcolors = computergeneratefourcolors(colorslist)
    playgame = "yes"
    guessnumber = 1
    while playgame != "quit":
        checker = 0
        print("Solution cheat:", computerfourcolors)
        #User inputs four colors from left to right to match computer generated four colors from left to right
        playgame = input("Enter any four colors separated by a space from left to right:  red, blue, orange, yellow, pink, green, and white.  Type quit to exit: ")
        if playgame == "quit":
            break
        else:
            #Convert input to a list
            userfourcolors = playgame.split()
            for eachuserfourcolors in userfourcolors:
                if eachuserfourcolors not in colorslist or len(userfourcolors) != 4:
                    print("\nError in colors input.  Enter any four colors red, blue, orange, yellow, pink, green, and white.  Try again.\n")
                    break
                else:
                    checker += 1
        #compareusercolorscomputercolors function checks user colors with computer generated colors
        if checker == 4 and len(userfourcolors) == 4:
            print("Your colors entered from left to right are", ", ".join(userfourcolors))
            compareusercolorscomputercolors(userfourcolors, computerfourcolors)
        else:
            continue
        #Return the correct answers and correct answers incorrect position
        if compareusercolorscomputercolors(userfourcolors, computerfourcolors)[0] == 4:
            print("Winner guessed color positions correctly.  Total guesses {}.".format(guessnumber))
            playgame = "quit"
        else:
            print("\nCorrect color in the correct place {}.  Correct color in the incorrect place {}.\n"  .format(compareusercolorscomputercolors(userfourcolors, computerfourcolors)[0], compareusercolorscomputercolors(userfourcolors, computerfourcolors)[1]))
            guessnumber += 1


colorslist = ["red", "blue", "orange", "yellow", "pink", "green", "white"]
mastermind(colorslist)

#Fourth attempt final
import random
def computergeneratefourcolors(colorslist):
    computerfourcolors = random.choices(colorslist, k=4)
    return computerfourcolors

def compareusercolorscomputercolors(userfourcolors, computerfourcolors):
    colormatchlist = [] #colormatchlist to log matching colors to avoid incorrect count for correctcolorwrongplace
    colorcheckedlist = [] #colorcheckedlist to log matching colors in incorrect place to avoid double checking
    correctcolorcorrectplace = 0
    correctcolorwrongplace = 0
    #Count correct colors in correct position
    for x in range(4):
        if userfourcolors[x] == computerfourcolors[x]:
            #print("Match", userfourcolors[x], computerfourcolors[x])
            colormatchlist.append(str(userfourcolors[x]) + "" + str(computerfourcolors[x]))
            correctcolorcorrectplace += 1
    #Count correct colors in incorrect positions
    for x in range(4):
        for y in range(4):
            #Skip counting correct colors in correct position
            if x == y:
                pass
            #Incorect color positions are counted if there is no correct color in correct position
            elif (userfourcolors[x] == computerfourcolors[y]) and ((str(userfourcolors[x]) + "" + str(computerfourcolors[y])) not in colormatchlist) and ((str(userfourcolors[x]) + "" + str(computerfourcolors[y])) not in colorcheckedlist):
                #print("Match incorrect place" + userfourcolors[x], computerfourcolors[y])
                colorcheckedlist.append(str(userfourcolors[x]) + "" + str(computerfourcolors[y]))
                correctcolorwrongplace += 1
            else:
                continue
    return correctcolorcorrectplace, correctcolorwrongplace


def mastermind(colorslist):
    print("Let's play Mastermind")
    computerfourcolors = computergeneratefourcolors(colorslist)
    playgame = "yes"
    guessnumber = 1
    while playgame != "quit":
        checker = 0
        print("Solution cheat:", computerfourcolors)
        #User inputs four colors from left to right to match computer generated four colors from left to right
        playgame = input("Enter any four colors separated by a space from left to right:  red, blue, orange, yellow, pink, green, and white.  Type quit to exit: ")
        if playgame == "quit":
            break
        else:
            #Convert input to a list
            userfourcolors = playgame.split()
            for eachuserfourcolors in userfourcolors:
                if eachuserfourcolors not in colorslist or len(userfourcolors) != 4:
                    print("\nError in colors input.  Enter any four colors red, blue, orange, yellow, pink, green, and white.  Try again.\n")
                    break
                else:
                    checker += 1
        #compareusercolorscomputercolors function checks user colors with computer generated colors
        if checker == 4 and len(userfourcolors) == 4:
            print("Your colors entered from left to right are", ", ".join(userfourcolors))
            compareusercolorscomputercolors(userfourcolors, computerfourcolors)
        else:
            continue
        #Return the correct answers and correct answers incorrect position
        if compareusercolorscomputercolors(userfourcolors, computerfourcolors)[0] == 4:
            print("Winner guessed color positions correctly.  Total guesses {}.".format(guessnumber))
            playgame = "quit"
        else:
            print("\nCorrect color in the correct place {}.  Correct color in the incorrect place {}.\n"  .format(compareusercolorscomputercolors(userfourcolors, computerfourcolors)[0], compareusercolorscomputercolors(userfourcolors, computerfourcolors)[1]))
            guessnumber += 1


colorslist = ["red", "blue", "orange", "yellow", "pink", "green", "white"]
mastermind(colorslist)
