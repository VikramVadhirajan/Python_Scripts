import tkinter as tk
from tkinter import ttk

# Conversion factors to meters
to_meters = {
    'mm': 0.001,
    'cm': 0.01,
    'm': 1,
    'km': 1000,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34
}

# List of units for dropdown
units = list(to_meters.keys())

def convert_length():
    try:
        value = float(entry.get())
        from_unit = unit_var.get()
        # Convert input to meters
        meters = value * to_meters[from_unit]
        # Convert meters to all units
        result = {unit: meters / factor for unit, factor in to_meters.items()}
        result_text = (
            f"{value} {from_unit} = "
            f"{result['mm']:.2f} mm, "
            f"{result['cm']:.2f} cm, "
            f"{result['m']:.2f} m, "
            f"{result['km']:.4f} km, "
            f"{result['inch']:.2f} inch, "
            f"{result['foot']:.2f} foot, "
            f"{result['yard']:.2f} yard, "
            f"{result['mile']:.4f} mile"
        )
        result_label.config(text=result_text)
    except ValueError:
        result_label.config(text="Please enter a valid number")

root = tk.Tk()
root.title("Length Converter")
root.geometry("500x250")

tk.Label(root, text="Enter length:").pack(pady=(10, 5))

entry = tk.Entry(root)
entry.pack(pady=5)

unit_var = tk.StringVar(value='m')
ttk.Label(root, text="Select unit:").pack()
unit_menu = ttk.Combobox(root, textvariable=unit_var, values=units, state='readonly')
unit_menu.pack(pady=5)

tk.Button(root, text="Convert", command=convert_length).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()