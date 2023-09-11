import tkinter


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
# label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
#my_label.pack()
#my_label.place(x=0,y=0)
my_label.grid(column=1, row=1)
my_label.config(padx=50, pady=50)

# button
button = tkinter.Button(text="Click me!", command=button_clicked)
#button.pack()
#button.place(x=10,y=10)
button.grid(column=1, row=2)

# Entry
input = tkinter.Entry(width=10)
print(input.get())
#input.pack()
#input.place(x=30,y=30)
input.grid(column=1, row=3)

window.mainloop()


def add(*args):
    result = 0
    for n in args:
        result = result + n
    return result


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(2, add=2, multiply=10))


class Car:
    def __init__(self, **kw):
        self.name = kw.get("name")
        self.model = kw.get("model")
        self.seats = kw.get("seats")
        # self.name = kw["name"]
        # self.model = kw["model"]
        # self.seats = kw["seats"]

        # my_car = Car(name="Hyundai", model="GT-200")
        # File
        # "C:\100 Days coding challenge\Day27_GUI\GUI_Tkinter.py", line
        # 34, in __init__
        # self.seats = kw["seats"]
        # KeyError: 'seats'


my_car = Car(name="Hyundai", model="GT-200", seats=5)
print(my_car.seats)
