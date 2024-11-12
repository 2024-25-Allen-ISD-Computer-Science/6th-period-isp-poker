import tkinter as tk

#Make window
window = tk.Tk()
window.title("poker window test")
window.geometry("300x200")  #Window size

# Set the background color and font color
window.configure(bg="blue")

#Make text
label = tk.Label(window, text="window test", font=("Arial", 20), fg="red", bg="blue")
label.pack(expand=True)  #Center the label

# Run the application
window.mainloop()