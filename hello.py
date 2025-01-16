from tkinter import *

# Call Function
def call():
    # Define Deck
    suits = ["diamonds", "clubs", "hearts", "spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    global deck
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank}_of_{suit}')
    print(deck)

#Window
root = Tk()
root.title('Poker')
root.geometry("900x500")
root.configure(background="green")

# Main Frame
my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Card Frames
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

# Card Labels
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)

# Buttons
call_button = Button(root, text="Call", font=("Times New Roman", 14), command=call)
call_button.pack(pady=20)

raise_button = Button(root, text="Raise", font=("Times New Roman", 14))
raise_button.pack(pady=20)

fold_button = Button(root, text="Fold", font=("Times New Roman", 14))
fold_button.pack(pady=20)

#mainloop
root.mainloop()
