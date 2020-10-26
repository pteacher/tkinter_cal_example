from tkinter import *


def get_sum():
	global e1text
	global e2text
	global t
	a = int(e1text.get())
	b = int(e2text.get())
	t.set(str(a + b))

window = Tk()
window.geometry("600x400")
window.title("Calculator")

t = StringVar()
t.set("0")
e1text = StringVar()
e1text.set("2")
e2text = StringVar()
e2text.set("3")

e1 = Entry(window, textvariable=e1text, font="Verdana 24 bold").pack()
e2 = Entry(window, textvariable=e2text, font="Verdana 24 bold").pack()
text = Label(window, textvariable=t, font="Verdana 24 bold").pack()
button_sum = Button(window, text="SUM", 
					command=get_sum, font="Verdana 24 bold").pack()

window.mainloop()