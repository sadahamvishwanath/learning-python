
import tkinter as tk 

window = tk.Tk()
window.title("Expense Tracker")
window.geometry("800x600")

window.grid_columnconfigure(0, weight=1)


balance_label = tk.Label(
    window,
    text="Balance:$",
    font=("Arial",18,"bold"),
    bg="gray"
)
balance_label.grid(row=0, column=0, padx=20, pady=20 , sticky="w")

add_menu = tk.Menu(window,tearoff=0)
add_menu.add_command(label="Income")
add_menu.add_command(label="Expenses")

def show_menu(event):
    add_menu.post(event.x_root, event.y_root)

button = tk.Button(window,text="ADD ▼")
button.grid(row=0, column=1, padx=20, pady=20, sticky="e")
button.bind("<Button-1>", show_menu)

window.mainloop()

"""

import tkinter as tk

window = tk.Tk()
window.geometry("800x600")
menu = tk.Menu(window, tearoff=0)
menu.add_command(label="Food")
menu.add_command(label="Transport")
menu.add_command(label="Rent")

def show_menu(event):
    menu.post(event.x_root, event.y_root)

button = tk.Button(window, text="Options")
button.pack(pady=50)

button.bind("<Button-1>", show_menu)

window.mainloop()
"""