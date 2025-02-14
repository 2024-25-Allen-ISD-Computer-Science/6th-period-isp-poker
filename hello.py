from tkinter import *
from tkinter import simpledialog, messagebox
import random

# Initialize Variables
dong = 5000
call_made = False
game_started = False

def start_game():
    global deck, dealer_hand, player_hand, dong, call_made, game_started
    if game_started:
        return
    game_started = True
    call_made = False
    suits = ["diamonds", "clubs", "hearts", "spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]
    random.shuffle(deck)
    dealer_hand, player_hand = [deck.pop(), deck.pop()], [deck.pop(), deck.pop()]
    update_ui()
    start_button.config(state=DISABLED)
    enable_buttons()

def call():
    global call_made
    if not game_started:
        messagebox.showwarning("Warning", "Start the game first!")
        return
    if call_made:
        messagebox.showwarning("Warning", "You can only call once per round!")
        return
    player_hand.append(deck.pop())
    call_made = True
    update_ui()

def raise_bet():
    global dong, call_made
    if not game_started:
        messagebox.showwarning("Warning", "Start the game first!")
        return
    amount = simpledialog.askinteger("Raise", "Enter raise amount:", minvalue=1, parent=root)
    if amount is None:
        return
    if amount > dong:
        messagebox.showwarning("Warning", "You do not have enough Dong!")
        return
    if amount and amount <= dong:
        dong -= amount
        call_made = False
        update_ui()

def fold():
    global dong, game_started
    if not game_started:
        messagebox.showwarning("Warning", "Start the game first!")
        return
    messagebox.showinfo("Fold", "Player has folded! Game Over.")
    dong = 1000
    game_started = False
    start_button.config(state=NORMAL)
    disable_buttons()
    update_ui()

def update_ui():
    player_label.config(text=f"Player: {', '.join(player_hand) if game_started else ''}")
    dealer_label.config(text="Dealer: Hidden")
    dong_label.config(text=f"Dong: {dong}")

def enable_buttons():
    call_button.config(state=NORMAL)
    raise_button.config(state=NORMAL)
    fold_button.config(state=NORMAL)

def disable_buttons():
    call_button.config(state=DISABLED)
    raise_button.config(state=DISABLED)
    fold_button.config(state=DISABLED)

def setup_ui():
    global root, player_label, dealer_label, dong_label, start_button, call_button, raise_button, fold_button
    root = Tk()
    root.title('Poker')
    root.geometry("900x500")
    root.configure(background="green")
    dong_label = Label(root, text=f"Dong: {dong}", font=("Arial", 14), bg="green", fg="white")
    dong_label.pack(anchor="ne", padx=20, pady=10)
    dealer_label = Label(root, text="Dealer: Hidden", font=("Arial", 14), bg="green", fg="white")
    dealer_label.pack(pady=10)
    player_label = Label(root, text="", font=("Arial", 14), bg="green", fg="white")
    player_label.pack(pady=10)
    start_button = Button(root, text="Start Game", font=("Times New Roman", 14), command=start_game)
    start_button.pack(pady=5)
    call_button = Button(root, text="Call", font=("Times New Roman", 14), command=call, state=DISABLED)
    call_button.pack(pady=5)
    raise_button = Button(root, text="Raise", font=("Times New Roman", 14), command=raise_bet, state=DISABLED)
    raise_button.pack(pady=5)
    fold_button = Button(root, text="Fold", font=("Times New Roman", 14), command=fold, state=DISABLED)
    fold_button.pack(pady=5)
    root.mainloop()

setup_ui()
