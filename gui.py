import tkinter as tk

def show_message():
    name = entry.get()
    result_label.config(text="Hello " + name)

app = tk.Tk()
app.title("Student Result System")

label = tk.Label(app, text="Enter Name")
label.pack()

entry = tk.Entry(app)
entry.pack()

btn = tk.Button(app, text="Submit", command=show_message)
btn.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()