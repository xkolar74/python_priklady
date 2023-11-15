import tkinter as tk

def on_button_click():
    # This function will be called when a button is clicked
    # You can add your logic here
    print("Button clicked!")

# Create the main window
root = tk.Tk()
root.title("kalkulačka")

# Create and place the text fields
text_field1 = tk.Entry(root)
text_field1.pack(expand=True, fill=tk.BOTH ,pady=10)

text_field2 = tk.Entry(root)
text_field2.pack(expand=True, fill=tk.BOTH ,pady=10)

# Create and place the buttons
button1 = tk.Button(root, text="+", command=on_button_click)
button1.pack (expand=True, fill=tk.BOTH ,side=tk.LEFT, padx=5)

button2 = tk.Button(root, text="-", command=on_button_click)
button2.pack(expand=True, fill=tk.BOTH ,side=tk.LEFT, padx=5)

button3 = tk.Button(root, text="*", command=on_button_click)
button3.pack(expand=True, fill=tk.BOTH ,side=tk.LEFT, padx=5)

button4 = tk.Button(root, text="/", command=on_button_click)
button4.pack(expand=True, fill=tk.BOTH ,side=tk.LEFT, padx=5)

# Start the Tkinter event loop
root.mainloop()
