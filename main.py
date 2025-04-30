import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500,height=300)

def button_clicked():
    user_input = input_entry.get()
    my_label["text"] = user_input
    print(user_input)

my_label = tkinter.Label(text="I am a label :P",font=("Arial",24,"bold"))
my_label.pack()
my_label["text"] = "I am NOT a label :/"

input_entry = tkinter.Entry(width=50)
input_entry.pack()

button = tkinter.Button(text="Click me :3",command=button_clicked)
button.pack()


window.mainloop()