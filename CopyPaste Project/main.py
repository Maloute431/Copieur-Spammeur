from tkinter import *
import pyperclip
import sys
import io

def getstring():       
    string = entry.get()

def getnumber():       
    nombre = number.get()

def on_focus_in(event, entry, hint_text):
    if entry.get() == hint_text:
        entry.delete(0, END)
        entry.config(fg='black')

def on_focus_out(event, entry, hint_text):
    if entry.get() == '':
        entry.insert(0, hint_text)
        entry.config(fg='gray')

def on_focus_in2(event, entry, hint_text2):
    if entry.get() == hint_text2:
        entry.delete(0, END)
        entry.config(fg='black')

def on_focus_out2(event, entry, hint_text2):
    if entry.get() == '':
        entry.insert(0, hint_text2)
        entry.config(fg='gray')

window = Tk()
window.geometry("420x420")
window.title("Copieur-Colleur")

hint_text = "Mot(s) à copier"
hint_text2 = "Nombre de fois"


window.config(background="#b8c9e6")

label = Label(window, text="Copieur Colleur", font=('Poppins', 25, 'bold'), bg='#b8c9e6')
label.pack()

entry = Entry(window, font=('Poppins'))
entry.insert(0, hint_text)
entry.config(fg='gray')
entry.pack(pady=10)
entry.bind("<FocusIn>", lambda event: on_focus_in(event, entry, hint_text))
entry.bind("<FocusOut>", lambda event: on_focus_out(event, entry, hint_text))

number = Entry(window, font=('Poppins'))
number.insert(0, hint_text2)
number.config(fg='gray')
number.pack(pady=10)
number.bind("<FocusIn>", lambda event: on_focus_in2(event, number, hint_text2))
number.bind("<FocusOut>", lambda event: on_focus_out2(event, number, hint_text2))


captured_output = io.StringIO()

def copy(captured_text):
    pyperclip.copy(captured_text)

def transform():
    sys.stdout = captured_output
    
    try:
        number_value = int(number.get())
    except ValueError:
        
        sys.stdout = sys.__stdout__
        return

    for i in range(number_value):      
        print(entry.get())

    sys.stdout = sys.__stdout__

    captured_text = captured_output.getvalue()

    copy(captured_text)

    



button = Button(window, text="Copier", command=transform, font=("Poppins",15), relief="flat", borderwidth=5)
button.pack()



window.mainloop()
