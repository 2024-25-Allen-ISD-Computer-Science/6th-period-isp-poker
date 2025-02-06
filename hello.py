from tkinter import *
from tkinter import simpledialog, messagebox  
import random

# Call Function
def call():
    # Define Deck
    suits = ["diamonds", "clubs", "hearts", "spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    global deck, dealer_hand, player_hand
    deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]
    random.shuffle(deck)
    
    # Dealer and Player Hands
    dealer_hand = [deck.pop(), deck.pop()]
    player_hand = [deck.pop(), deck.pop()]
    
    print(f"Dealer's hand (hidden): {dealer_hand}")
    player_label.config(text=f"Player's hand: {player_hand[0]}, {player_hand[1]}")

# Reveal Dealer Hand Function
def reveal_dealer():
    dealer_label.config(text=f"Dealer's hand: {dealer_hand[0]}, {dealer_hand[1]}")

# Raise Function
def raise_bet():
    response = messagebox.askyesno("Raise", "Do you want to raise?")
    if response:
        amount = simpledialog.askinteger("Raise", "Enter your raise amount:", minvalue=1, parent=root)
        if amount is not None:
            action_label.config(text=f"Player raises by {amount} dong.")

# Fold Function
def fold():
    messagebox.showinfo("Fold", "Player has folded! Game Over.")
    call_button.config(state=DISABLED)
    raise_button.config(state=DISABLED)
    fold_button.config(state=DISABLED)
    action_label.config(text="Player has folded. Game Over.")
    reveal_dealer()

# Window Setup
root = Tk()
root.title('Poker')
root.geometry("900x500")
root.configure(background="green")

# Main Frame
my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Dealer Frame
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)
dealer_label = Label(dealer_frame, text='Dealer Cards (Hidden)')
dealer_label.pack(pady=20)

# Player Frame
player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)
player_label = Label(player_frame, text='')
player_label.pack(pady=20)

# Output Labels
action_label = Label(root, text="", bg="green", fg="yellow", font=("Arial", 14))
action_label.pack(pady=10)

# Buttons
call_button = Button(root, text="Call", font=("Times New Roman", 14), command=call)
call_button.pack(pady=10)

raise_button = Button(root, text="Raise", font=("Times New Roman", 14), command=raise_bet)
raise_button.pack(pady=10)

fold_button = Button(root, text="Fold", font=("Times New Roman", 14), command=fold)
fold_button.pack(pady=10)

# Main Loop
root.mainloop()
