from tkinter import*

root = Tk()
# Title
root.title("Tkinter Review")

# This is for the window
root.geometry("300x300")

# add a label
sam = Label(root,text = "Enter your Name", font = "Georgia", fg = "pink")
# Pady
sam.pack(pady=10)

# This is an entry
sam_entry = Entry(root, text = "type here")
# pady
sam_entry.pack(pady=5)

# add a button
button = Button(root, text = "Submit")
#Pady
button.pack(pady=5)

root.mainloop()
