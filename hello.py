from tkinter import *
from tkinter import messagebox
import random

# Initialize Variables
dong = 5000
game_started = False
player_turn = True
player_hand = []
dealer_hand = []

def start_game():
    global deck, dealer_hand, player_hand, dong, game_started
    if game_started:
        return
    game_started = True
    player_hand.clear()
    dealer_hand.clear()
    suits = ["diamonds", "clubs", "hearts", "spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]
    random.shuffle(deck)
    dealer_hand = [deck.pop(), deck.pop()]
    player_hand = [deck.pop(), deck.pop()]
    
    # Reset dealer's hand to "Hidden" on start
    dealer_label.config(text="Dealer: Hidden")
    
    update_ui()
    start_button.config(state=DISABLED)
    enable_buttons()

def card_value(card):
    rank = card.split()[0]
    if rank in ['Jack', 'Queen', 'King']:
        return 10
    if rank == 'Ace':
        return 11
    return int(rank)

def calculate_hand_value(hand):
    total = sum(card_value(card) for card in hand)
    aces = sum(1 for card in hand if 'Ace' in card)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def hit():
    global player_hand
    if not game_started:
        messagebox.showwarning("Warning", "Start the game first!")
        return
    player_hand.append(deck.pop())
    if calculate_hand_value(player_hand) > 21:
        update_ui()
        messagebox.showinfo("Game Over", "Bust! You Lose!")
        end_game()
    else:
        update_ui()

def stand():
    global player_turn
    player_turn = False
    dealer_turn()

def dealer_turn():
    global dealer_hand
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    reveal_dealer_hand()
    evaluate_winner()
    end_game()

def reveal_dealer_hand():
    dealer_label.config(text=f"Dealer: {', '.join(dealer_hand)} (Value: {calculate_hand_value(dealer_hand)})")

def evaluate_winner():
    dealer_value = calculate_hand_value(dealer_hand)
    player_value = calculate_hand_value(player_hand)
    if dealer_value > 21:
        messagebox.showinfo("Game Over", "Dealer busts! You Win!")
    elif dealer_value >= player_value:
        messagebox.showinfo("Game Over", "Dealer Wins!")
    else:
        messagebox.showinfo("Game Over", "You Win!")

def end_game():
    global game_started
    game_started = False
    start_button.config(state=NORMAL)
    disable_buttons()
    update_ui()

def update_ui():
    player_label.config(text=f"Player: {', '.join(player_hand)} (Value: {calculate_hand_value(player_hand)})" if game_started else '')
    if not game_started or not player_turn:
        reveal_dealer_hand()
    else:
        dealer_label.config(text="Dealer: Hidden")
    dong_label.config(text=f"Dong: {dong}")

def enable_buttons():
    hit_button.config(state=NORMAL)
    stand_button.config(state=NORMAL)

def disable_buttons():
    hit_button.config(state=DISABLED)
    stand_button.config(state=DISABLED)

def setup_ui():
    global root, player_label, dealer_label, dong_label, start_button, hit_button, stand_button
    root = Tk()
    root.title('Blackjack')
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
    hit_button = Button(root, text="Hit", font=("Times New Roman", 14), command=hit, state=DISABLED)
    hit_button.pack(pady=5)
    stand_button = Button(root, text="Stand", font=("Times New Roman", 14), command=stand, state=DISABLED)
    stand_button.pack(pady=5)
    root.mainloop()

setup_ui()
