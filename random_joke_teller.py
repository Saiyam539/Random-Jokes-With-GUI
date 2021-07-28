from tkinter import *
import pyjokes


window = Tk()
window.minsize(550,500)
window.maxsize(550,500)
window.title("Random Jokes")
window.config(bg="light pink")

def random_jokes():
    jokes = pyjokes.get_joke()
    message.config(text=f"{jokes}")
    print(jokes)

heading = Label(window,text="Random Jokes",font=("bold",40),bg="light cyan")
heading.pack(fill=X)

enter_button = Button(window,text="A New Joke",font=("bold",30),fg="blue",command=lambda:random_jokes())
enter_button.place(x=200,y=100)

message = Message(window,font=("bold",35),bg="light pink",width=500)
message.place(x=0,y=200)

window.mainloop()