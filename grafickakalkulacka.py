import tkinter as tk

def on_button_click():
    # This function will be called when a button is clicked
    # You can add your logic here
    print("Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Simple GUI Application")

# Create and place the text fields
text_field1 = tk.Entry(root)
text_field1.pack(pady=10)

text_field2 = tk.Entry(root)
text_field2.pack(pady=10)

# Create and place the buttons
button1 = tk.Button(root, text="Button 1", command=on_button_click)
button1.pack(side=tk.LEFT, padx=5)

button2 = tk.Button(root, text="Button 2", command=on_button_click)
button2.pack(side=tk.LEFT, padx=5)

button3 = tk.Button(root, text="Button 3", command=on_button_click)
button3.pack(side=tk.LEFT, padx=5)

button4 = tk.Button(root, text="Button 4", command=on_button_click)
button4.pack(side=tk.LEFT, padx=5)

# Start the Tkinter event loop
root.mainloop()
