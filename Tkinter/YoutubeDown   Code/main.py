from tkinter import *
from tkinter import filedialog
import pytube1
import tkinter as tk
import pytube


def show(url):
    num = 1
    r1 = ''
    r2 = []
    yt = pytube.YouTube(f'{url}')
    print(yt.title)
    r2.append(str(yt.title))

    yt = yt.streams.filter(progressive='True')

    for m in yt:
        r1 += (f'{num}. Sifat:  ')
        for i in str(m)[46:55]:
            if i.isdigit():
                r1 += str(i)
        r2.append(r1)
        r1 = ''
        num += 1
    return r2


def dow1(url, index, fileas):
    yt = pytube.YouTube(f'{url}')
    yt = list(yt.streams.filter(progressive='True'))[int(index)-1]
    yt.download(output_path=fileas)


oyna = Tk(className=" YouTubeDownloader")
oyna.geometry('400x500')
oyna.minsize(width=400, height=500)
oyna.maxsize(400, 500)
oyna['bg'] = 'cyan'
oyna.tk.call('wm', 'iconphoto', oyna._w, tk.PhotoImage(file='youtube-512.png'))
lab1 = Label(text='Link: ', bg='cyan', fg='red', font=('Elephant', 15))
lab1.place(x=10, y=10, width=70, height=20)
ent1 = Entry(text='Link')
ent1.place(x=90, y=10, width=250, height=20)
####################################


def down():
    
    joy = 40
    for i in show(str(ent1.get())):
        tugma = Label(text=i, font=('Stencil'),
                      fg='yellow', bg='blue')
        tugma.place(x=90, y=joy, width=250)
        joy += 20
    tugma1.place(height=0, x=1000000)	
    lab3 = Label(text='Index: ', bg='cyan',
                 fg='red', font=('Elephant', 15))
    lab3.place(x=10, y=200, width=70, height=20)
    ent2 = Entry()
    ent2.place(x=90, y=200, width=250, height=20)
    lab4 = Label(text='Papka: ', bg='cyan',
                 fg='red', font=('Elephant', 15))
    lab4.place(x=10, y=250, width=70, height=20)
    ent3 = Label(text='Downloads/', bg='yellow', font=('Elephant', 15))
    ent3.place(x=90, y=250, width=250, height=20)
	
    def fileas():
        folder = filedialog.askdirectory()
        if len(str(folder)) < 20:
            pass
        else:
            folder = folder[20:40]
        ent3.config(text=folder,  bg='yellow', font=('Elephant', 15))
        print(ent3['text'])
        return folder

    tugma3 = Button(text='...', bg='blue',
                    fg='red', font=('Elephant', 15), command=fileas)
    tugma3.place(x=345, y=250, width=50, height=20)

    def download():
        dow1(ent1.get(), ent2.get(), ent3['text'])
    tugma2 = Button(text='Download:))', font=('Elephant'),
                    fg='yellow', bg='blue',  command=download)
    tugma2.place(x=120, y=350, width=150)


tugma1 = Button(text='Tekshirish', font=('Elephant'),
                fg='yellow', bg='blue', command=down)
tugma1.place(x=150, y=40, width=100)


#####################
muallif = Label(fg='red', text='Muallif: Diyorbek Ismoilov',
                font=('SimSun', 10))
muallif.place(x=200, y=475)

oyna.mainloop()
