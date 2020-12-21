
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.geometry("700x500")
root.resizable(width=0, height=0)
root.title("moodle logger")
root.configure(background="black")

username = tk.Entry(root)
username.place(rely=0.5)
username.insert(0, "MOODLE_USERNAME")

password = tk.Entry(root)
password.place(rely=0.55)
password.insert(0, "MOODLE_PASSWORT")

interval  = tk.Entry(root)
interval.place(rely=0.6)
interval.insert(0, "INTERVAL EINFÜGEN")

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    show_chrdriver = tk.Label(root, text=str(filename))
    show_chrdriver.place(rely=0.75)

button = tk.Button(root, text='OPEN CHROMEDRIVER', command=UploadAction)
button.place(rely=0.65)

audiofiles = tk.Listbox(root, width=50, height=25, bg="black", fg="white")
audiofiles.place(relx=0.5, rely=0.1)

start = tk.Button(root, text="START", width=10)
start.place(relx=0.3, rely=0.853)

root.mainloop()