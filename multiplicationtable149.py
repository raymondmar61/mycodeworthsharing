#Create a times table for which user enters a number.  The program returns a multiplication table from 1 to 12 times the user's inputted number.
import tkinter as tk

def multiply():
    numberinput = inputbox.get()
    for n in range(1, 13):
        multiplication = n * int(numberinput)
        multiplicationlist.insert(tk.END, (str(n) + " x " + str(numberinput) + " = " + str(multiplication))) #book hint You want to display the number sentence in the list rather than just the answers.  RM:  the hint was in the exercises listvariable.insert(tk.END,inputvariable)

def clearmultiplicationlist():
    inputbox.delete(0, tk.END)
    multiplicationlist.delete(0, tk.END)
    inputbox.focus()


windowobject = tk.Tk()
windowobject.title("Times Table")
windowobject.geometry("800x600")
label = tk.Label(text="Enter a number:")
label.place(x=20, y=20, width=100, height=25)
inputbox = tk.Entry(text="")
inputbox.place(x=130, y=20, width=165, height=25)
inputbox.focus()
multiplybutton = tk.Button(text="View Multiplication Table", command=multiply)
multiplybutton.place(x=300, y=20, height=25)
multiplicationlist = tk.Listbox()
multiplicationlist.place(x=130, y=60, width=165, height=300)
clearbutton = tk.Button(text="Clear", command=clearmultiplicationlist)
clearbutton.place(x=300, y=60)
windowobject.mainloop()

#create a blank window 400x280 with title Window Title
# firsttkwindowobject = tk.Tk()
# firsttkwindowobject.title("Window Title")
# firsttkwindowobject.geometry("400x280")
# firsttkwindowobject.mainloop()

# def pressbuttonfunction():
#     messagebelowbutton = tk.Label(window, text="You pressed button label from the top left 30 going to the right and 150 going down begin at its top left.\n  Change button background color to blue and font color to white")
#     messagebelowbutton.place(x=30, y=150)
#     button["bg"] = "blue"
#     button["fg"] = "white"

# def buttonfunction():
#     nouninput = inputbox.get()
#     outputbox["bg"] = "yellow"
#     outputbox["fg"] = "blue"
#     outputbox["text"] = nouninput
#     nounlist.insert(tk.END, nouninput)
#     inputbox.delete(0, tk.END)
#     inputbox.focus()

# def clearentry():
#     outputbox["text"] = "inputboxcleared Enter a noun"
#     outputbox["bg"] = "white"
#     inputbox.delete(0, tk.END)
#     inputbox.focus()

# def clearlist():
#     nounlist.delete(0, tk.END)
#     inputbox.focus()


# window = tk.Tk()
# window.title("Crash courage tkinter library")
# window.geometry("800x600")
# button = tk.Button(text="button Press Me from the top left 30 going to the right and\n 20 going down begin button at its top left", command=pressbuttonfunction)
# button.place(x=30, y=20, width=400, height=100)
# inputbox = tk.Entry(text="inputbox Enter a noun")
# inputbox["text"] = "inputbox really Enter a noun I didn't appear"
# inputbox.place(x=30, y=200)
# inputbox.focus()
# buttonnoun = tk.Button(text="buttonnoun Press button for action", command=buttonfunction)
# buttonnoun.place(x=30, y=250)
# outputbox = tk.Message(text="outputbox Default text")
# outputbox.place(x=30, y=300, width=200, height=50)
# outputbox["bg"] = "white"
# outputbox["fg"] = "black"
# outputbox["relief"] = "ridge"
# nounlist = tk.Listbox()
# nounlist.place(x=350, y=200, width=200, height=200)
# clearbutton = tk.Button(text="clearbutton Clear", command=clearentry)
# clearbutton.place(x=30, y=375, width=200, height=75)
# clearbuttonlist = tk.Button(text="clearbuttonlist Clear", command=clearlist)
# clearbuttonlist.place(x=30, y=450, width=200, height=100)
# window.mainloop()
