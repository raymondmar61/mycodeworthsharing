import sqlite3
import os

def addartist():
    cursor.execute("SELECT count(*) from artists;")
    #Automatically create an artist id
    artistid = cursor.fetchall()[0][0] + 1
    name = input("Enter artist's name: ")
    address = input("Enter artist's address: ")
    town = input("Enter artist's town: ")
    country = input("Enter artist's country: ")
    postcode = input("Enter artist's postcode: ")
    cursor.execute("INSERT into artists values(?,?,?,?,?,?);", (artistid, name, address, town, country, postcode))
    db.commit()

def addpiece():
    cursor.execute("SELECT count(*) from pieces;")
    #Automatically create an art piece id
    pieceid = cursor.fetchall()[0][0] + 1
    artistid = int(input("Enter artist's id: "))
    title = input("Enter piece's title: ")
    medium = input("Enter piece's medium: ")
    price = int(input("Enter piece's price: "))
    cursor.execute("INSERT into pieces values(?,?,?,?,?);", (pieceid, artistid, title, medium, price))
    db.commit()

def soldpiece():
    pieceid = input("Enter sold piece id: ")
    cursor.execute("SELECT * from pieces where pieceid = (?);", (pieceid,))
    soldpiece = str(cursor.fetchall()[0])
    print("Sold piece:", soldpiece)
    #Write the sold art piece to a text file
    with open("soldpiecetextfile.txt", "a") as textfileobject:
        textfileobject.write(soldpiece)
        textfileobject.write("\n")
    cursor.execute("DELETE from pieces where pieceid = (?);", (pieceid,))
    db.commit()

def viewartist():
    cursor.execute("SELECT * from artists;")
    print(cursor.fetchall())

def viewpieceofart():
    cursor.execute("SELECT * from pieces;")
    print(cursor.fetchall())

#Write a SQL join to view the artist and his or her pieces of art
def viewartistpieceofart():
    cursor.execute("""
        SELECT a.name, p.title, p.medium, p.price
        from artists a join pieces p
        on a.artistid = p.artistid;""")
    print(cursor.fetchall())

def searchartist():
    searchartistname = input("Enter artist name: ")
    searchartistname = "%" + searchartistname + "%"
    cursor.execute("SELECT * from artists where name like (?);", (searchartistname,))
    print(cursor.fetchall())

def searchpieceofartname():
    searchpieceofartname = input("Enter piece of art name: ")
    searchpieceofartname = "%" + searchpieceofartname + "%"
    cursor.execute("SELECT * from pieces where title like (?);", (searchpieceofartname,))
    print(cursor.fetchall())

def searchpieceofartmedium():
    searchpieceofartmedium = input("Enter piece of art medium: ")
    searchpieceofartmedium = "%" + searchpieceofartmedium + "%"
    cursor.execute("SELECT * from pieces where medium like (?);", (searchpieceofartmedium,))
    print(cursor.fetchall())

def searchpieceofartprice():
    priceinput = input("Enter piece of art price range separated by a space.  For example, 100 200: ")
    splitprice = priceinput.split()
    cursor.execute("SELECT * from pieces where price between (?) and (?);", (splitprice[0], splitprice[1]))
    print(cursor.fetchall())

def exportartist():
    #remove existing artiststextfile.txt to create a new artiststextfile.txt file.  Try except in case artiststextfile.txt file doesn't exist
    try:
        os.remove("artiststextfile.txt")
    except FileNotFoundError:
        filewrite = open("artiststextfile.txt", "w")
        filewrite.close()
    cursor.execute("SELECT * from artists;")
    artiststotextfile = cursor.fetchall()
    for eachartiststotextfile in artiststotextfile:
        with open("artiststextfile.txt", "a") as textfileobject:
            textfileobject.write(str(eachartiststotextfile))
            textfileobject.write("\n")

def exportpieceofartprice():
    #remove existing piecesofarttextfile.txt to create a new piecesofarttextfile.txt file.  Try except in case piecesofarttextfile.txt file doesn't exist
    try:
        os.remove("piecesofarttextfile.txt")
    except FileNotFoundError:
        filewrite = open("piecesofarttextfile.txt", "w")
        filewrite.close()
    cursor.execute("SELECT * from pieces;")
    piecesofarttotextfile = cursor.fetchall()
    for eachpiecesofarttotextfile in piecesofarttotextfile:
        with open("piecesofarttextfile.txt", "a") as textfileobject:
            textfileobject.write(str(eachpiecesofarttotextfile))
            textfileobject.write("\n")

def clearartisttable():
    cursor.execute("DELETE from artists;")
    db.commit()
def clearpiecettable():
    cursor.execute("DELETE from pieces;")
    db.commit()


#Connect to artgallery database
db = sqlite3.connect("artgallery.db")
cursor = db.cursor()
#Create two tables artists table and pieces table
cursor.execute("""
CREATE table if not exists artists (artistid integer, name text, address text, town text, country text, postcode text);
""")
cursor.execute("""
CREATE table if not exists pieces (pieceid integer, artistid integer, title text, medium text, price integer);
""")
#Create Python user interface.  Functions include tempoary artists data and pieces of art data.
menuprompt = """---Art Gallery---
Please choose one of these options:
1) Add new artist
2) Add new piece of art
3) Enter sold piece of art
4) View artists
5) View pieces of art
6) View artists and their pieces of art
7) Search artist
8) Search piece of art name
9) Search piece of art medium
10) Search piece of art price
11) Export artists to text file
12) Export pieces of art to text file
13) Exit
14) Clear artist table
15) Clear pieces table

Your selection: """
while (userinput := input(menuprompt)) != "13":  #RM:  need paranthesis for (userinput := input(menuprompt))
    if userinput == "1":
        addartist()
    elif userinput == "2":
        addpiece()
    elif userinput == "3":
        soldpiece()
    elif userinput == "4":
        viewartist()
    elif userinput == "5":
        viewpieceofart()
    elif userinput == "6":
        viewartistpieceofart()
    elif userinput == "7":
        searchartist()
    elif userinput == "8":
        searchpieceofartname()
    elif userinput == "9":
        searchpieceofartmedium()
    elif userinput == "10":
        searchpieceofartprice()
    elif userinput == "11":
        exportartist()
    elif userinput == "12":
        exportpieceofartprice()
    elif userinput == "13":
        break
    elif userinput == "14":
        clearartisttable()
    elif userinput == "15":
        clearpiecettable()
    else:
        print("Invalid input.  Please try again.")
    print("\n")
db.close()
