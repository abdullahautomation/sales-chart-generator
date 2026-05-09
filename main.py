import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, filedialog
window = tk.Tk()
window.title("Sales Chart")
window.geometry("600x400")
def generate_chart():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        plt.bar(df["Month"], df["Sales"], color="green")
        plt.title("Monthly Sales Chart")
        plt.xlabel("Months")
        plt.ylabel("Sales")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        messagebox.showerror("Cancelled", "No File Selected")
tk.Label(window, text="Sales Chart Generator", font=("Arial", 14, "bold")).pack(pady=20)
tk.Button(window, text="Generate Report", command=generate_chart).pack(pady=10)
window.mainloop()