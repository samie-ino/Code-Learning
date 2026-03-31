from tkinter import*

root = Tk()
# Title
root.title("Miles Converter")

# This is for the window
root.geometry("300x300")

# Change background color
root.configure(bg="lightblue")

# This is the side margins
root['padx'] = 50 # Horizontal padding
root['pady'] = 20 # Vertical padding

def calculation():
    miley = float(miles_entry.get())
    formula = miley * 1.6
    formula2 = miley * 1.6 * 1000
    times_label1.config(text = formula)
    times_label2.config(text=formula2)


# Entry box
miles_entry = Entry(root,text= "Type Miles here")
# grid for entry
miles_entry.grid(row = 0, column = 1)
# add a label
miles_label = Label(root, text = "Miles")
# grid for label
miles_label.grid(row = 0, column = 2)

# label for equal to (1)
equal_label1 = Label(root, text="is equal to")
# grid for the label
equal_label1.grid(row = 1, column = 0)

# label for equal to (2)
equal_label2 = Label(root, text="is equal to")
# grid for the label
equal_label2.grid(row = 2, column = 0)

# label for times (1)
times_label1 = Label(root, text="   X")
# grid for the label
times_label1.grid(row = 1, column = 1)

# label for times (2)
times_label2 = Label(root, text="   X")
# grid for the label
times_label2.grid(row = 2, column = 1)


# label for kilometers
kilo_label = Label(root, text="Km")
# grid for the label
kilo_label.grid(row = 1, column = 2)

# label for meters
meters_label = Label(root, text="M")
# grid for the label
meters_label.grid(row = 2, column = 2)

# add the button
button = Button(root, text = "Calculate", command = calculation)
# grid for the button
button.grid(row = 3, column = 1)



'''
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

'''

root.mainloop()