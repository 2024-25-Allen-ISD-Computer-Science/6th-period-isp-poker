from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Initialize Variables
dong = 5000
game_started = False
player_turn = True
player_hand = []
dealer_hand = []

def load_card_image(card_name):
    try:
        img = Image.open(f"assets/{card_name}.png").resize((100, 150))
        return ImageTk.PhotoImage(img)
    except FileNotFoundError:
        return None

def start_game():
    global deck, dealer_hand, player_hand, dong, game_started
    if game_started:
        return
    game_started = True
    player_hand.clear()
    dealer_hand.clear()
    suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "Ace"]
    deck = [f'{rank}_{suit}' for suit in suits for rank in ranks]
    random.shuffle(deck)
    dealer_hand = [deck.pop(), deck.pop()]
    player_hand = [deck.pop(), deck.pop()]
    
    update_ui()
    start_button.config(state=DISABLED)
    enable_buttons()

def card_value(card):
    rank = card.split("_")[0]
    return 10 if rank in ['J', 'Q', 'K'] else 11 if rank == 'Ace' else int(rank)

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
    update_ui()
    if calculate_hand_value(player_hand) > 21:
        messagebox.showinfo("Game Over", "Bust! You Lose!")
        end_game()

def stand():
    global player_turn
    player_turn = False
    dealer_turn()

def dealer_turn():
    global dealer_hand
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    update_ui(show_dealer_cards=True)
    evaluate_winner()
    end_game()

def evaluate_winner():
    global dong
    dealer_value = calculate_hand_value(dealer_hand)
    player_value = calculate_hand_value(player_hand)
    if dealer_value > 21 or player_value > dealer_value:
        messagebox.showinfo("Game Over", "You Win!")
        dong += 1000
    elif player_value < dealer_value:
        messagebox.showinfo("Game Over", "Dealer Wins!")
        dong -= 1000
    else:
        messagebox.showinfo("Game Over", "It's a Tie!")

def end_game():
    global game_started
    game_started = False
    start_button.config(state=NORMAL)
    disable_buttons()
    update_ui(show_dealer_cards=True)

def enable_buttons():
    hit_button.config(state=NORMAL)
    stand_button.config(state=NORMAL)

def disable_buttons():
    hit_button.config(state=DISABLED)
    stand_button.config(state=DISABLED)

def update_ui(show_dealer_cards=False):
    for i, label in enumerate(player_card_labels):
        if i < len(player_hand):
            img = load_card_image(player_hand[i])
            label.img = img
            label.config(image=img if img else '', text=player_hand[i] if not img else '')
        else:
            label.config(image='', text='Empty')
    
    for i, label in enumerate(dealer_card_labels):
        if i < len(dealer_hand):
            if i == 0 and not show_dealer_cards:
                label.config(image='', text='[Hidden]')
            else:
                img = load_card_image(dealer_hand[i])
                label.img = img
                label.config(image=img if img else '', text=dealer_hand[i] if not img else '')
        else:
            label.config(image='', text='Empty')
    
    dong_label.config(text=f"Dong: {dong}")

def show_help():
    help_text = (
        "How to Play Blackjack:\n"
        "1. Press 'Start Game' to begin.\n"
        "2. Press 'Hit' to draw a card.\n"
        "3. Press 'Stand' to end your turn.\n"
        "4. Dealer will draw cards until reaching 17 or higher.\n"
        "5. Closest to 21 without going over wins!\n"
        "6. Aces count as 1 or 11, depending on the best outcome."
    )
    messagebox.showinfo("Help", help_text)

def setup_ui():
    global root, dong_label, start_button, hit_button, stand_button, player_card_labels, dealer_card_labels, help_button
    root = Tk()
    root.title('Blackjack')
    root.geometry("900x500")
    root.configure(background="green")
    
    dong_label = Label(root, text=f"Dong: {dong}", font=("Arial", 14), bg="green", fg="white")
    dong_label.pack(anchor="ne", padx=20, pady=10)
    
    dealer_frame = Frame(root, bg="green")
    dealer_frame.pack()
    dealer_card_labels = [Label(dealer_frame, bg="green") for _ in range(5)]
    for lbl in dealer_card_labels:
        lbl.pack(side=LEFT, padx=5)
    
    player_frame = Frame(root, bg="green")
    player_frame.pack()
    player_card_labels = [Label(player_frame, bg="green") for _ in range(5)]
    for lbl in player_card_labels:
        lbl.pack(side=LEFT, padx=5)
    
    start_button = Button(root, text="Start Game", font=("Times New Roman", 14), command=start_game)
    start_button.pack(pady=5)
    hit_button = Button(root, text="Hit", font=("Times New Roman", 14), command=hit, state=DISABLED)
    hit_button.pack(pady=5)
    stand_button = Button(root, text="Stand", font=("Times New Roman", 14), command=stand, state=DISABLED)
    stand_button.pack(pady=5)
    reset_button = Button(root, text="Reset Game", font=("Times New Roman", 12), command=start_game)
    reset_button.pack(pady=5)
    help_button = Button(root, text="Help", font=("Times New Roman", 12), command=show_help)
    help_button.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-20)
    
    root.mainloop()

setup_ui()