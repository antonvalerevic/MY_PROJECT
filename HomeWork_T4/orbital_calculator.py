from math import pi
import tkinter as tk


def calculate():
    radius_1 = float(entry_radius1.get())
    velocity_1 = float(entry_velocity1.get())

    radius_2 = float(entry_radius2.get())
    velocity_2 = float(entry_velocity2.get())

    year_length_1 = 2 * pi * radius_1 / velocity_1
    year_length_2 = 2 * pi * radius_2 / velocity_2

    planet_1 = "Планета 1" if year_length_1 > year_length_2 else "Планета 2"

    label_length1.config(text=f"Длина года на планете 1: {year_length_1:.2f}")
    label_length2.config(text=f"Длина года на планете 2: {year_length_2:.2f}")
    label_comparison.config(text=f"На {planet_1} год длиннее")


root = tk.Tk()
root.geometry("500x500+500+300")
root.title("Космический калькулятор")

label_radius1 = tk.Label(root, text="Радиус орбиты планеты 1:")
label_radius1.pack()

entry_radius1 = tk.Entry(root)
entry_radius1.pack()

label_velocity1 = tk.Label(root, text="Орбитальная скорость планеты 1:")
label_velocity1.pack()

entry_velocity1 = tk.Entry(root)
entry_velocity1.pack()

label_radius2 = tk.Label(root, text="Радиус орбиты планеты 2:")
label_radius2.pack()

entry_radius2 = tk.Entry(root)
entry_radius2.pack()

label_velocity2 = tk.Label(root, text="Орбитальная скорость планеты 2:")
label_velocity2.pack()

entry_velocity2 = tk.Entry(root)
entry_velocity2.pack()

button_calculate = tk.Button(root, text="Вычислить", command=calculate)
button_calculate.pack()

label_length1 = tk.Label(root, text="")
label_length1.pack()

label_length2 = tk.Label(root, text="")
label_length2.pack()

label_comparison = tk.Label(root, text="")
label_comparison.pack()

root.mainloop()