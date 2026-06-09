import math
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Two real roots: x1={x1}, x2={x2}"

    elif delta == 0:
        x = -b / (2*a)
        return f"One repeated root: x={x}"

    else:
        return "No real roots"


def plot_parabola(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c

    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.plot(x, y, label=f"{a}x^2 + {b}x + {c}")
    plt.legend()
    plt.title("Quadratic Function")
    plt.show()


def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            messagebox.showerror("Error", "a cannot be zero")
            return

        result = solve_quadratic(a, b, c)
        messagebox.showinfo("Result", result)

    except:
        messagebox.showerror("Error", "Invalid input")


def draw():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            messagebox.showerror("Error", "a cannot be zero")
            return

        plot_parabola(a, b, c)

    except:
        messagebox.showerror("Error", "Invalid input")


app = tk.Tk()
app.title("Quadratic Solver")
app.geometry("300x250")

tk.Label(app, text="a").pack()
entry_a = tk.Entry(app)
entry_a.pack()

tk.Label(app, text="b").pack()
entry_b = tk.Entry(app)
entry_b.pack()

tk.Label(app, text="c").pack()
entry_c = tk.Entry(app)
entry_c.pack()

tk.Button(app, text="Solve", command=calculate).pack(pady=5)
tk.Button(app, text="Plot", command=draw).pack(pady=5)

app.mainloop()