import tkinter as tk

def increase():
    current_val = int(label_num.cget("text"))
    label_num.config(text=str(current_val + 1))

def decrease():
    current_val = int(label_num.cget("text"))
    label_num.config(text=str(current_val - 1))

def reset():
    label_num.config(text="0")

root = tk.Tk()
root.title("Counter App")
root.geometry("300x200")

label_num = tk.Label(root, text="0", font=("Arial", 30))
label_num.pack(pady=20)

btn_increase = tk.Button(root, text="Increase", width=10, command=increase)
btn_increase.pack(pady=5)

btn_decrease = tk.Button(root, text="Decrease", width=10, command=decrease)
btn_decrease.pack(pady=5)

btn_reset = tk.Button(root, text="Reset", width=10, command=reset)
btn_reset.pack(pady=5)

root.mainloop()