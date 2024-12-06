import random
import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk

# Define suits and ranks
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# Function to create a shuffled deck
def create_shuffled_deck():
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# Deal hands to players
def deal_hand(deck, num_players=2):
    hands = {f"Player {i+1}": [deck.pop(), deck.pop()] for i in range(num_players)}
    return hands

# Deal community cards
def deal_community_cards(deck):
    deck.pop()  # Burn one card
    flop = [deck.pop(), deck.pop(), deck.pop()]  # Three cards for the flop
    deck.pop()  # Burn another card
    turn = deck.pop()  # One card for the turn
    deck.pop()  # Burn another card
    river = deck.pop()  # One card for the river
    return {"Flop": flop, "Turn": turn, "River": river}

# Function to start a new game and display it in a new window
def open_game_window():
    # Create and shuffle a new deck
    deck = create_shuffled_deck()
    
    # Deal new hands and community cards
    hands = deal_hand(deck, 2)
    community_cards = deal_community_cards(deck)

    # Create a new window
    game_window = Toplevel()
    game_window.title("Poker Game")
    
    # Display player hands
    tk.Label(game_window, text="Player Hands:", font=("Arial", 14, "bold")).pack(pady=5)
    for player, hand in hands.items():
        tk.Label(game_window, text=f"{player}: {', '.join(hand)}", font=("Arial", 12)).pack(pady=2)

    # Display community cards
    tk.Label(game_window, text="Community Cards:", font=("Arial", 14, "bold")).pack(pady=10)
    for stage, cards in community_cards.items():
        tk.Label(game_window, text=f"{stage}: {', '.join(cards)}", font=("Arial", 12)).pack(pady=2)

    # Show a card image (just for demonstration purposes)
    card_image_path = r"C:\Users\aamar\OneDrive\Documents\GitHub\6th-period-isp-poker\assets\card.png"
    try:
        card_image = Image.open(card_image_path)
        card_image = card_image.resize((100, 150))  # Resize image for display
        card_photo = ImageTk.PhotoImage(card_image)
        tk.Label(game_window, image=card_photo).pack(pady=10)
        # Keep reference to prevent garbage collection
        game_window.image = card_photo
    except Exception as e:
        tk.Label(game_window, text=f"Error loading card image: {e}", fg="red", font=("Arial", 10)).pack(pady=10)

# Main window setup
root = tk.Tk()
root.title("Poker Game Launcher")

# Launch button
launch_button = tk.Button(root, text="Start Poker Game", font=("Arial", 14), command=open_game_window)
launch_button.pack(pady=50)

# Run the main loop
root.mainloop()
