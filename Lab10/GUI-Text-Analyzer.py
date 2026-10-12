import tkinter as tk

def count_character():
    text = entry_text.get()
    char = entry_char.get()
    if char == "":
        label_result.config(text="กรุณากรอกตัวอักษรที่ต้องการนับ")
        return
    count = text.count(char)
    label_result.config(text=f"ตัวอักษร '{char}' มีทั้งหมด {count} ตัว")

def count_vowels():
    text = entry_text.get()
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    label_result.config(text=f"จำนวนสระทั้งหมด: {count} ตัว")

def check_palindrome():
    text = entry_text.get().replace(" ", "").lower()
    if text == "":
        label_result.config(text="กรุณากรอกข้อความก่อนตรวจสอบ")
        return
    
    if text == text[::-1]:
        label_result.config(text="ผลลัพธ์: เป็น Palindrome")
    else:
        label_result.config(text="ผลลัพธ์: ไม่เป็น Palindrome")

root = tk.Tk()
root.title("GUI Text Analyzer")
root.geometry("400x350")

tk.Label(root, text="ข้อความหลัก (Text):").pack(anchor="w", padx=20, pady=(10, 0))
entry_text = tk.Entry(root, width=35, font=("Arial", 11))
entry_text.pack(padx=20, pady=5)

tk.Label(root, text="ตัวอักษรค้นหา (Character):").pack(anchor="w", padx=20, pady=(5, 0))
entry_char = tk.Entry(root, width=10, font=("Arial", 11))
entry_char.pack(anchor="w", padx=20, pady=5)

btn_char = tk.Button(root, text="Count Character", width=20, command=count_character)
btn_char.pack(pady=3)

btn_vowels = tk.Button(root, text="Count Vowels", width=20, command=count_vowels)
btn_vowels.pack(pady=3)

btn_palindrome = tk.Button(root, text="Check Palindrome", width=20, command=check_palindrome)
btn_palindrome.pack(pady=3)

label_result = tk.Label(root, text="ผลลัพธ์: ", font=("Arial", 12), fg="blue")
label_result.pack(pady=15)

root.mainloop()