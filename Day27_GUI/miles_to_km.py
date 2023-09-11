from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometers")
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(row=1, column=2)

miles_label = Label(text="Miles")
miles_label.grid(row=1, column=3)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=2, column=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=2, column=2)

kilometer_label = Label(text="Km")
kilometer_label.grid(row=2, column=3)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=3, column=3)

window.mainloop()
