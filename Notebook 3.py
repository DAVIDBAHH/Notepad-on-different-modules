from tkinter import Menu
from tkinter.font import families
from tkinter import Menu
from customtkinter import *
from tkinter import messagebox
from tkinter import filedialog
from time import *
font_size = 16
font = "Arial"
def time_and_date():
    text_fild.insert('1.0',asctime())
def delete():
    text_fild.delete('1.0', 'end')
def new_window():
    text_fild.delete('1.0', 'end')
    root.title("Untitled--Notebook")
def chenge_theme(theme):
    text_fild["bg"] = view_colors[theme]["text_bg"]
    text_fild["fg"] = view_colors[theme]["text_fg"]
    text_fild["insertbackground"] = view_colors[theme]["cursor"]
    text_fild["selectbackground"] = view_colors[theme]["select_bg"]
    if theme == "dark":
        set_appearance_mode("Dark")
    else:
        set_appearance_mode("Light")
def chenge_fonts(index):
    global font
    font = families()[index]
    text_fild.configure(font=(font, font_size))
def notepad_exit():
    answer = messagebox.askokcancel("Exit", "Are you sure you want to go out?")
    if answer:
        root.destroy()
def open_file():
    file_path = filedialog.askopenfilename(title="File selection", filetypes=(("Text documents (*.txt)", "*.txt"), ("All files", "*.*")))
    if file_path:
        text_fild.delete("1.0", "end")
        text_fild.insert("1.0", open(file_path, encoding="utf-8").read())
def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(("Text documents (*.txt)", "*.txt"), ("All files", "*.*")))
    if file_path:
        f = open(file_path, "w", encoding="utf-8")
        text = text_fild.get("1.0", "end")
        f.write(text)
        f.close()
root = CTk()
a = families()
root.title("test.txt - Notebook")
root.geometry("600x700")
main_menu = Menu(root)
# File menu
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Create",command=new_window)
file_menu.add_command(label="New window",command=new_window)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save as...", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Close", command=notepad_exit)
root.config(menu=file_menu)
# Edit menu
edit_menu = Menu(main_menu, tearoff=0)
edit_menu.add_command(label="Delete",command=delete)
edit_menu.add_separator()
edit_menu.add_command(label="Time and date",command=time_and_date)
# Format menu
format_menu = Menu(main_menu, tearoff=0)
format_menu_sub = Menu(format_menu, tearoff=0)
font_menu_sub = Menu(format_menu, tearoff=0)
format_menu_sub.add_command(label="Dark", command=lambda: chenge_theme("dark"))
format_menu_sub.add_command(label="Light", command=lambda: chenge_theme("light"))
format_menu.add_cascade(label="Theme...", menu=format_menu_sub)
for i in range(len(families())):
    font_menu_sub.add_command(label=families()[i], command=lambda i=i: chenge_fonts(i))
format_menu.add_cascade(label="Font...", menu=font_menu_sub)
root.config(menu=format_menu)
# Add menus to the main menu
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
main_menu.add_cascade(label="Format", menu=format_menu)
root.config(menu=main_menu)
f_text = CTkFrame(root)
f_text.pack(fill=BOTH, expand=1)
view_colors = {"dark": {"text_bg": "black", "text_fg": "white", "cursor": "white", "select_bg": "white"},
               "light": {"text_bg": "white", "text_fg": "black", "cursor": "#A5A5A5", "select_bg": "#FAEEDD"}}
#f_text, bg_color="black", fg_color="white", padx=10, pady=10, wrap="word", insertbackground="white", selectbackground="white"
text_fild = CTkTextbox(master=f_text, width=30, font=(font, font_size, "normal"))
text_fild.pack(expand=1, fill=BOTH)
root.mainloop()