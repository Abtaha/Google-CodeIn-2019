import tkinter as tk

import subprocess
import webbrowser


# Opens Github
def openGH():
    webbrowser.open("https://www.github.com")

# Opens Youtube
def openYT():
    webbrowser.open("https://www.youtube.com")

# Opens Visual Studio Code
def openVSC():
    command = 'C:\\Program Files\\Microsoft VS Code\\Code.exe'
    subprocess.call(command)


# Create Button
def createButton(text, command):
    if text == "Open GitHub":
        b = "#24292E"
        f = "#BEBFC1"
    elif text == "Open YouTube":
        b = "#FF0000"
        f = "#FFFFFF"
    elif text == "Open Visual Studio Code":
        b = "#0075B7"
        f = "#DDDDEE"
        
    btn = tk.Button(app, bg=b, fg=f, text=text, command=command)
    btn.pack(ipadx=20, ipady=10, padx=20, pady=20)


#! Define the structure of the app
root = tk.Tk()
root.title("Automate Tasks")

root.geometry("500x500")

app = tk.Frame(root)
app.place(relwidth=1, relheight = 1)


# ! define the buttons
createButton("Open GitHub", openGH)
createButton("Open YouTube", openYT) 
createButton("Open Visual Studio Code", openVSC)


root.mainloop()
