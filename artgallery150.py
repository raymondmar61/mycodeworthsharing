import sqlite3

def addartist(artistid, name, address, town, country, postcode):
    # def addartist():
    db = sqlite3.connect("artgallery.db")
    cursor = db.cursor()
    # cursor.execute("SELECT count(*) from artists;")
    # artistid = cursor.fetchall()[0][0] + 1
    # name = input("Enter artist's name: ")
    # address = input("Enter artist's address: ")
    # town = input("Enter artist's town: ")
    # country = input("Enter artist's country: ")
    # postcode = input("Enter artist's postcode: ")
    cursor.execute("""
    INSERT into artists values(?,?,?,?,?,?);
    """, (artistid, name, address, town, country, postcode))
    db.commit()
    db.close()

def addpiece(pieceid, artistid, title, medium, price):
    # def addpiece():
    db = sqlite3.connect("artgallery.db")
    cursor = db.cursor()
    # cursor.execute("SELECT count(*) from pieces;")
    # pieceid = cursor.fetchall()[0][0] + 1
    # artistid = int(input("Enter artist's id: "))
    # title = input("Enter piece's title: ")
    # medium = input("Enter piece's medium: ")
    # price = int(input("Enter piece's price: "))
    cursor.execute("""
    INSERT into pieces values(?,?,?,?,?);
    """, (pieceid, artistid, title, medium, price))
    db.commit()
    db.close()

def soldpiece(pieceid):
    # def soldpiece():
    db = sqlite3.connect("artgallery.db")
    cursor = db.cursor()
    # pieceid = input("Enter sold piece id:")
    pieceid = "2"
    cursor.execute("SELECT * from pieces where pieceid = (?)", (pieceid))
    soldpiece = str(cursor.fetchall()[0])
    print("Sold piece:", soldpiece)
    #Write the sold art piece to a text file
    with open("soldpiecetextfile.txt", "a") as textfileobject:
        textfileobject.write(soldpiece)
        textfileobject.write("\n")
    cursor.execute("""
    DELETE from pieces
    where pieceid = (?);""", (pieceid))
    db.commit()
    db.close()


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
3) Temp test add new artist and new piece of art
5) Exit

Your selection: """
while (userinput := input(menuprompt)) != "5":  #RM:  need paranthesis for (userinput := input(menuprompt))
    if userinput == "1":
        addartist(1, "Martin Leighton", "5 Park Place", "Peterborough", "Cambridgeshire", "PE32 5LP")
        addartist(2, "Eva Czarniecka", "77 Warner Close", "Chelmsford", "Essex", "CM22 5FT")
        break
    elif userinput == "2":
        addpiece(4, 5, "Woman with black Labrador", "Oil", 220)
        addpiece(2, 5, "Bees & thistles", "Watercolour", 85)
        break
    elif userinput == "3":
        addartist(1, "Martin Leighton", "5 Park Place", "Peterborough", "Cambridgeshire", "PE32 5LP")
        addartist(2, "Eva Czarniecka", "77 Warner Close", "Chelmsford", "Essex", "CM22 5FT")
        addpiece(4, 5, "Woman with black Labrador", "Oil", 220)
        addpiece(2, 5, "Bees & thistles", "Watercolour", 85)
        break
    else:
        print("Invalid input.  Please try again.")
cursor.execute("SELECT * from artists;")
print(cursor.fetchall())
cursor.execute("SELECT * from pieces;")
print(cursor.fetchall())
soldpiece(2)
cursor.execute("SELECT * from pieces;")
print(cursor.fetchall())
cursor.execute("""
DROP table artists;
""")
cursor.execute("""
DROP table pieces;
""")
db.commit()
db.close()

#Reminder pass a function value to another function
def secondfunction(a):
    print(a + 1)

def firstfunction(n):
    secondfunction(n + 1)
    return n


print(firstfunction(5))
