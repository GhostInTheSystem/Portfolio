from tkinter import *
top = Tk()
def russianCallBack():
   messagebox.showinfo( "Result", "Correct!")
R = Button(top, text ="Russian", command = russianCallBack)
R.pack()
def spanishCallBack():
   messagebox.showinfo( "Result", "Incorrect")
S = Button(top, text ="Spanish", command = spanishCallBack)
S.pack()

def onclick():
   pass


#text = Text(top)
#text.pack()

#text.tag_add("here", "1.0", "1.4")
#text.tag_add("start", "1.8", "1.13")
#text.tag_config("here", background="yellow", foreground="blue")
#text.tag_config("start", background="black", foreground="green")

t = Text(top)
t.pack()

top.mainloop()
print (t)
