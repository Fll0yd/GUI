from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def greet_user(event):
    username = input_box.get()
    greet['text'] = 'Welcome ' + username

def show_message():
    messagebox.showinfo('PythonX - Learn Python', 'Welcome')

window = Tk()

name = Label(window, text='PythonX - Learn Python', bg='white', fg='Blue', font=('Serif', 16))
image = Label(window, image=ImageTk.PhotoImage(Image.open('F:/Code/Python/Learning/python.png')))

frame = Frame(window)
username_lbl = Label(frame, text='Username', font=('Serif', 12))
input_box = Entry(frame)

button = Button(window, text="Let's Start")
button.bind('<Button-1>', greet_user)

greet = Label(window)

frame.pack()
username_lbl.pack(side=LEFT)
input_box.pack(side=RIGHT)
button.pack()
greet.pack()

frame_lang = Frame(window)
lbl_lang = Label(frame_lang, text='Choose your favorite programming languages:')
python = Checkbutton(frame_lang, text='Python')
java = Checkbutton(frame_lang, text="Java")
js = Checkbutton(frame_lang, text='Javascript')
cpp = Checkbutton(frame_lang, text='C++')

frame_gender = Frame(window)
lbl_gender = Label(frame_gender, text="Gender:")
var = StringVar()
male = Radiobutton(frame_gender, text='Male', variable=var, value='M')
female = Radiobutton(frame_gender, text='Female', variable=var, value='F')

name.pack()
image.pack()
frame_lang.pack()
lbl_lang.pack()
python.pack()
java.pack()
js.pack()
cpp.pack()
frame_gender.pack()
lbl_gender.pack()
male.pack()
female.pack()

window.mainloop()
