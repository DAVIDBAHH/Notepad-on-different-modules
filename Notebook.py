from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from time import *
font_size = 11
font = "Arial"
def time_and_date():
    text_fild.insert('1.0',asctime())
def delete():
    text_fild.delete('1.0', 'end')
def new_window():
    text_fild.delete('1.0', 'end')
    notebook_root.title("Untitled--Notebook")
def chenge_theme(theme):
    text_fild["bg"] = view_colors[theme]["text_bg"]
    text_fild["fg"] = view_colors[theme]["text_fg"]
    text_fild["insertbackground"] = view_colors[theme]["cursor"]
    text_fild["selectbackground"] = view_colors[theme]["select_bg"]
def chenge_fonts(fontss):
    global font
    font = fontss
    text_fild.configure(font=fonts[fontss]["font"])
def notepad_exit():
    answer = messagebox.askokcancel("Exit", "Are you sure you want to go out?")
    if answer:
        notebook_root.destroy()
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
notebook_root = Tk()
notebook_root.title("test.txt - Notebook")
notebook_root.geometry("600x700")
main_menu = Menu(notebook_root)
# File menu
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Create",command=new_window)
file_menu.add_command(label="New window",command=new_window)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save as...", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Close", command=notepad_exit)
notebook_root.config(menu=file_menu)
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
format_menu.add_cascade(label="Theme", menu=format_menu_sub)
font_menu_sub.add_command(label="Arial", command=lambda: chenge_fonts("Arial"))
font_menu_sub.add_command(label="Comic Sans MS", command=lambda: chenge_fonts("CSMS"))
font_menu_sub.add_command(label="Times New Roman", command=lambda: chenge_fonts("TNR"))
font_menu_sub.add_command(label="Impact", command=lambda: chenge_fonts("Impact"))
font_menu_sub.add_command(label="Courier", command=lambda: chenge_fonts("Courier"))
font_menu_sub.add_command(label="Verdana", command=lambda: chenge_fonts("Verdana"))
font_menu_sub.add_command(label="Helveticar", command=lambda: chenge_fonts("Helveticar"))
font_menu_sub.add_command(label="Trebuchet MS", command=lambda: chenge_fonts("TMS"))
font_menu_sub.add_command(label="Consolas", command=lambda: chenge_fonts("Consolas"))
font_menu_sub.add_command(label="Georgia", command=lambda: chenge_fonts("Georgia"))
format_menu.add_cascade(label="Font...", menu=font_menu_sub)
notebook_root.config(menu=format_menu)
# Add menus to the main menu
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
main_menu.add_cascade(label="Format", menu=format_menu)
notebook_root.config(menu=main_menu)
f_text = Frame(notebook_root)
f_text.pack(fill=BOTH, expand=1)
view_colors = {"dark": {"text_bg": "black", "text_fg": "white", "cursor": "white", "select_bg": "white"},
               "light": {"text_bg": "white", "text_fg": "black", "cursor": "#A5A5A5", "select_bg": "#FAEEDD"}}
fonts = {"Arial": {"font": ("Arial", font_size, "bold")},
         "CSMS": {"font": ("Comic Sans MS", font_size, "bold")},
         "TNR": {"font": ("Times New Roman", font_size, "bold")},
         "Impact": {"font": ("Impact", font_size, "bold")},
         "Courier": {"font": ("Courier", font_size, "bold")},
          "Verdana": {"font": ("Verdana", font_size, "bold")},
          "Helveticar": {"font": ("Helvetica", font_size, "bold")},
          "TMS": {"font": ("Trebuchet MS", font_size, "bold")},
          "Consolas": {"font": ("Consolas", font_size, "bold")},
          "Georgia": {"font": ("Georgia", font_size, "bold")}}
text_fild = Text(f_text, bg="black", fg="white", padx=10, pady=10, wrap="word", insertbackground="white", selectbackground="white", width=30, font=fonts[font]["font"])
text_fild.pack(expand=1, fill=BOTH, side="left")
scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side="left", fill="y")
text_fild.config(yscrollcommand=scroll.set)
notebook_root.mainloop()