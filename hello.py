import tkinter as tk

#show test
def show_hello():
    label.config(text="test")

#show test2
def show_goodbye():
    label.config(text="test2")

#clear window
def reset_screen():
    label.config(text="")#clears

#make window
window = tk.Tk()
window.title("poker test")
window.geometry("300x200")
window.configure(bg="black")

# Create a label with no initial text
label = tk.Label(window, text="", font=("Arial", 20), fg="white", bg="black")
label.pack(pady=20)

#test button
test2_button = tk.Button(window, text="test2", command=show_goodbye, font=("Arial", 12))
test2_button.pack(side="left", padx=10, pady=20)

#test2 button
test_button = tk.Button(window, text="test", command=show_hello, font=("Arial", 12))
test_button.pack(side="right", padx=10, pady=20)

#clear button
clear_button = tk.Button(window, text="clear", command=reset_screen, font=("Arial", 12))
clear_button.pack(side="bottom", pady=20)

#run
window.mainloop()
