# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 02:18:25 AM 2025

@author: IAN CARTER KULANI
"""


import tkinter as tk
from tkinter import messagebox

# Function to calculate the molecular weight of H2O
def calculate_molecular_weight():
    try:
        # Get the input values
        h2o_oxygens = int(entry_oxygen.get())
        h2o_hydrogens = int(entry_hydrogen.get())
        
        # Atomic masses
        oxygen_mass = 15.9994
        hydrogen_mass = 1.00794
        
        # Calculate molecular weight
        h2o_mass = (h2o_oxygens * oxygen_mass) + (h2o_hydrogens * hydrogen_mass)
        
        # Display the result
        label_result.config(text=f"Molecular weight of H2O = {h2o_mass:.4f}")
    
    except ValueError:
        # Handle invalid input
        messagebox.showerror("Invalid Input", "Please enter valid integer values.")

# Create the main window
window = tk.Tk()
window.title("Molecular Weight Calculator")
window.geometry("400x300")
window.config(bg="blue")

# Create widgets
label_oxygen = tk.Label(window, text="Enter the number of oxygen atoms:", bg="blue", fg="white")
label_oxygen.pack(pady=10)

entry_oxygen = tk.Entry(window)
entry_oxygen.pack(pady=5)

label_hydrogen = tk.Label(window, text="Enter the number of hydrogen atoms:", bg="blue", fg="white")
label_hydrogen.pack(pady=10)

entry_hydrogen = tk.Entry(window)
entry_hydrogen.pack(pady=5)

# Button to calculate molecular weight
button_calculate = tk.Button(window, text="Calculate", command=calculate_molecular_weight)
button_calculate.pack(pady=20)

# Label to display result
label_result = tk.Label(window, text="", bg="blue", fg="white")
label_result.pack(pady=10)

# Run the GUI event loop
window.mainloop()
