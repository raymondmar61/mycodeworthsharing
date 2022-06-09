#Create program store user id and passwords for users.
specialcharacterslist = ["!", "@", "#", "$", "%", "^", "*", ".", ",", "?", ";", ":"]
def readcsvfile():
    temporarydictionary = {}
    with open("passwords148csv.csv", "r") as fileobjecttemporarydictionary:  #https://www.geeksforgeeks.org/update-column-value-of-csv-in-python
        for eachfileobject in fileobjecttemporarydictionary:
            firstcomma = eachfileobject.find(",")
            userid = eachfileobject[0:firstcomma]
            password = eachfileobject[firstcomma + 1:-1]
            temporarydictionary[userid] = password
    return temporarydictionary

def createnewpassword(useridinput, passwordstatus="write"):
    newpasswordinput = input("Enter a password: ")
    #Instructions says password must earn five points at least 8 characters, lowercase, uppercase, number, and selected special characters.
    points = 0
    while points != 5:
        if len(newpasswordinput) >= 8:
            points += 1
        if any(eachnewpasswordinput.isupper() for eachnewpasswordinput in newpasswordinput) == True: #https://www.geeksforgeeks.org/python-test-if-string-contains-any-uppercase-character/
            points += 1
        if any(eachnewpasswordinput.islower() for eachnewpasswordinput in newpasswordinput) == True:
            points += 1
        if any(eachnewpasswordinput.isdecimal() for eachnewpasswordinput in newpasswordinput) == True:
            points += 1
        for eachnewpasswordinput in newpasswordinput:
            if eachnewpasswordinput in specialcharacterslist:
                points += 1
                break
        if points != 5:
            points = 0
            newpasswordinput = input("Your password is not strong enough.  Password must contain at least eight characters with upper case and lower case, a number, and any special character !, @, #, $, %, ^, *, ., ,, ?, ;, or :.  Enter a password: ")
        #User changes password
        if passwordstatus == "append":
            temporarydictionary = readcsvfile()
            temporarydictionary[useridinput] = newpasswordinput
            with open("passwords148csv.csv", "w") as fileobject:  #https://www.geeksforgeeks.org/update-column-value-of-csv-in-python
                for userid, password in temporarydictionary.items():
                    newaccount = userid + "," + password + "\n"
                    fileobject.write(newaccount)
        #New user and new password
        if passwordstatus == "write":
            with open("passwords148csv.csv", "a") as fileobject:
                newaccount = useridinput + "," + newpasswordinput + "\n"
                fileobject.write(newaccount)

def newuserid():
    useridinput = input("Enter a User ID: ")
    temporarydictionary = readcsvfile()
    while True:
        if useridinput in temporarydictionary.keys():
            useridinput = input(useridinput + " is already taken.  Enter another User ID: ")
        else:
            break
    createnewpassword(useridinput)

def checkuserid():
    useridinput = input("Enter a User ID: ")
    temporarydictionary = readcsvfile()
    while True:
        if useridinput in temporarydictionary.keys():
            createnewpassword(useridinput, passwordstatus="append")
            break
        else:
            print(useridinput + " User ID doesn't exist.")
            break

def printuserid():
    with open("passwords148csv.csv", "r") as fileobject:
        for eachfileobject in fileobject:
            firstcomma = eachfileobject.find(",")
            #Avoid printing the csv file header
            if (eachfileobject[0:firstcomma]) == "userid":
                pass
            else:
                print(eachfileobject[0:firstcomma])


while True:
    print("""
1) Create a new User ID
2) Change a password
3) Display all User IDs
4) Quit
    """)
    #Enter number to run program
    userinput = input("Enter Selection: ")
    if userinput == "1":
        newuserid()
    elif userinput == "2":
        checkuserid()
    elif userinput == "3":
        printuserid()
    elif userinput == "4":
        break
    else:
        print("Incorrect input.  Try again.")
