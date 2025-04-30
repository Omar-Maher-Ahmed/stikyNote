import tkinter as tk
from tkinter import scrolledtext, colorchooser
import os

# إعدادات حفظ الملف
FILE_PATH = "sticky_note.txt"

# فتح الملف وقراءة المحتوى
def load_content():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return file.read()
    return ""

# حفظ المحتوى في الملف
def save_content():
    with open(FILE_PATH, "w") as file:
        file.write(text_area.get("1.0", tk.END))

# تغيير اللون الخلفية
def change_background():
    color = colorchooser.askcolor()[1]
    if color:
        root.configure(bg=color)
        text_area.configure(bg=color)

# تغيير اللون النص
def change_text_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_area.configure(fg=color)

# تغيير الخط
def change_font():
    current_font = text_area.cget("font")
    new_font = ("Arial", 12, "bold")
    text_area.configure(font=new_font)

# إعداد النافذة
root = tk.Tk()
root.title("Sticky Note")
root.geometry("300x300+1000+100")  # الحجم + المكان
root.attributes("-topmost", True)  # فوق كل التطبيقات
root.resizable(True, True)  # إمكانية تغيير الحجم

# إعداد النص
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), bg="#fffec8", borderwidth=0)
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# تحميل المحتوى من الملف عند فتح التطبيق
text_area.insert(tk.END, load_content())

# زر الإغلاق
close_btn = tk.Button(root, text="X", command=root.destroy, bg="#ff5c5c", fg="white")
close_btn.place(x=270, y=5, width=20, height=20)

# زر تغيير الخلفية
bg_btn = tk.Button(root, text="Background Color", command=change_background)
bg_btn.pack(side=tk.LEFT, padx=10)

# زر تغيير لون النص
text_color_btn = tk.Button(root, text="Text Color", command=change_text_color)
text_color_btn.pack(side=tk.LEFT)

# زر تغيير الخط
font_btn = tk.Button(root, text="Font", command=change_font)
font_btn.pack(side=tk.RIGHT, padx=10)

# حفظ المحتوى تلقائيًا كل 5 ثواني
def auto_save():
    save_content()
    root.after(5000, auto_save)  # حفظ كل 5 ثواني

auto_save()

# تشغيل التطبيق
root.mainloop()

