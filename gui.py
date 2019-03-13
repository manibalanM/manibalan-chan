from tkinter import*
import speech
import scrap

def fun_1():
    
    t1.delete(0,'end')
    t1.insert(0,speech.speech())
    a=t1.get()
##    l.delete('1.0', END)
##    l.insert(INSERT,scrap.wiki(a))
    if 'who' in a or'when' in a:
        l.delete('1.0', END)
        l.insert(INSERT,scrap.google(a))
        speech.voice(scrap.google(a))
    elif 'about'  in a or'About' in a :
        a = a[6:]
        l.delete('1.0', END)
        l.insert(INSERT,scrap.wiki(a))
        speech.voice(scrap.wiki(a))
    elif 'what is the' in a:
        a = a[12:]
        l.delete('1.0', END)
        l.insert(INSERT,scrap.wiki(a))
        speech.voice(scrap.wiki(a))
    elif 'what is' in a:
        a = a[8:]
        l.delete('1.0', END)
        l.insert(INSERT,scrap.wiki(a))
        speech.voice(scrap.wiki(a))
        
    else:
        l.delete('1.0', END)
        l.insert(INSERT,scrap.wiki(a))
        speech.voice(scrap.wiki(a))


root = Tk()
root.title("MAX")
root.geometry('900x680')
photo = PhotoImage(file = "ai.png")
w = Label(root, image=photo)
w.pack()

S = Scrollbar(root)
S.pack(side=RIGHT, fill=Y)
b = Button(root,text="submit",command=fun_1)
b.pack()
t1 = Entry(root,font=('Gabriola','15','bold'),width=60,bd=0)
t1.pack(pady=10)
l = Text(root,font=('Gabriola','14','bold'),width=68,height=7.5,bd=0)
l.pack(pady=10)
S.config(command=l.yview)
l.config(yscrollcommand=S.set)

root.mainloop()

