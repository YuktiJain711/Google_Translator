from tkinter import *
import string
import os
from tkinter import ttk
import googletrans
import gtts
from googletrans import Translator


root = Tk()
root.title("Google Translator")
root.wm_iconbitmap("Translator.ico")
root.geometry("1000x400")
root.resizable(False, False)
root.configure(background="white")


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)




def translate_now():

    text_ = text1.get(1.0, END)
    t1 = Translator()
    trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
    trans_text = trans_text.text

    text2.delete(1.0, END)
    text2.insert(END, trans_text)



# arrow

arrow_image = PhotoImage(file="arrow.1.png")
image_label = Label(root, image=arrow_image, width=180)
image_label.place(x=415, y=50)


language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()


# first combobox
combo1 = ttk.Combobox(root, values=languageV, font="Lucida 12", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="segoe 20 ", bg="white", width=15, bd=5, relief=GROOVE)
label1.place(x=85, y=50)


# second combobox
combo2 = ttk.Combobox(root, values=languageV, font="Lucida 12", state="r")
combo2.place(x=700, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="segoe 20", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=640, y=50)


# first frame
f = Frame(root, bg="Black", bd=5)
f.place(x=35, y=118, width=350, height=230)

text1 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=340, height=220)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


# second frame
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=350, height=230)

text2 = Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=340, height=220)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


# translate button
translate = Button(root, text="Translate", font=("Roboto", 15), activebackground="white",
                   cursor="hand2", bd=1, width=12,
                   height=2, bg="black", fg="white", command=translate_now)
translate.place(x=435, y=250)


label_change()

root.mainloop()
