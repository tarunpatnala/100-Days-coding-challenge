import tkinter

window = tkinter.Tk()
window.title("Hello World!")
window.minsize(width=500, height=300)
# label
my_label = tkinter.Label(text="Who are you?", font=("Arial", 24, "italic"))
my_label.pack(side="left", expand=True)


# button
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked!")

button = tkinter.Button(text="Click me!", command=button_clicked)
button.pack()

#Entry
input = tkinter.Entry(width = 10)
input.pack()
my_label.config(text=input.get())

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
