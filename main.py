import tkinter as tk
from tkinter import messagebox

import constant

window = tk.Tk()

window.title(constant.TITLE)
window.geometry(constant.GEOMETRY)


#เริ่มต้น - กำหนดตัวแปรที่จะนำมาคำนวน
gender = tk.StringVar()

current_year = tk.IntVar()
current_year.set(2024)

birth_year = tk.IntVar()
birth_year.set(0)
#จบ - กำหนดตัวแปรที่จะนำมาคำนวน

def show_age():
    messagebox.showinfo(
        title="อายุของคุณตอนนี้ !",
        message=f"อายุของคุณคือ {current_year.get() - birth_year.get()}"
    )


def show_privileges():
    user_age = current_year.get() - birth_year.get()
    if gender.get() == "Female":
        if user_age >= 20:
            messagebox.showinfo(
                title="สิทธิพิเศษของคุณ !",
                message="ขนม"
            )
        else:
            messagebox.showinfo(
                title="สิทธิพิเศษของคุณ !",
                message="ลูกอม"
            )
    elif gender.get() == "Male":
        if user_age >= 20:
            messagebox.showinfo(
                title="สิทธิพิเศษของคุณ !",
                message="พิซซ่า"
            )
        else:
            messagebox.showinfo(
                title="สิทธิพิเศษของคุณ !",
                message="ดินสอ"
            )
    else:
        messagebox.showerror(
            title="กรุณาเลือกเพศของคุณ",
            message="กรุณาเบือกเพศของคุณเพื่อตรวจสอบสิทธิพิเศษ"
        )


tk.Label(text="กรุณากรอกปีปัจจุบัน").pack()
tk.Entry(window, width=15, textvariable=current_year, ).pack()

tk.Label(text="กรุณากรอกปีเกิด").pack()
tk.Entry(window, width=15, textvariable=birth_year).pack()

tk.Button(text="คำนวนอายุ", command=show_age).pack()

tk.Checkbutton(window, text="ผู้ชาย", variable=gender, onvalue="Male").pack()
tk.Checkbutton(window, text="ผู้หญิง", variable=gender, onvalue="Female").pack()

tk.Button(text="คำนวนสิทธิพิเศษ", command=show_privileges).pack()

window.mainloop()
