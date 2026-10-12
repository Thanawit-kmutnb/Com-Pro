import tkinter as tk
from tkinter import messagebox #สำหรับแจ้งเตือน

def convert_temp():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"ผลลัพธ์: {fahrenheit:.2f} °F")

    except ValueError:
        messagebox.showerror("Error", "กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น!")

root = tk.Tk()
root.title("Celsius to Fahrenheit Converter")
root.geometry("350x200")

tk.Label(root, text="กรอกอุณหภูมิ (°C):", font=("Arial", 12)).pack(pady=10)
entry_celsius = tk.Entry(root, font=("Arial", 12))
entry_celsius.pack()

btn_convert = tk.Button(root, text="Convert", font=("Arial", 10), command=convert_temp)
btn_convert.pack(pady=10)

label_result = tk.Label(root, text="ผลลัพธ์: -", font=("Arial", 12))
label_result.pack(pady=10)

root.mainloop()