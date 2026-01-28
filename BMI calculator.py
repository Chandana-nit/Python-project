import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get()) / 100  # Convert cm to meters
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        
        # Determine category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        result_label.config(text=f"Your BMI: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for height and weight.")

# Create main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

# Labels and entries
tk.Label(root, text="Height (cm):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

tk.Label(root, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

# Calculate button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Times New Roman", 20))
result_label.pack(pady=10)

# Run the app
root.mainloop()