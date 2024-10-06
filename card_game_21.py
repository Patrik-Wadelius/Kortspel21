import random
# Klassen "Deck" hanterar Kortleken
class Deck:
    def __init__(self) -> None:
        self.cards_list = ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] # Alla olika kort Ess-Kung
        self.card_colors = ['♦','♣','♥','♠'] # De fyra olika kortfärgerna, påverkar inte värdena 
        self.deck = [(card, category) for category in self.card_colors for card in self.cards_list] # Ger korten sin färg
    
    def shuffle(self) -> None: # Blandar kortleken
        random.shuffle(self.deck)

    def deal_card(self): # Delar ut kortet
        return self.deck.pop()

def card_value(card, current_score) -> int: #Behandlar de "klädda" kortens värden
    if card[0] == 'J':
        return 11
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'K':
        return 13
    elif card[0] == 'A': # Ess har 2 värden beroende på hur många poäng spelare/dealern har
        return 1 if current_score + 14 > 21 else 14
    else:
        return int(card[0])

game_deck = Deck() # Skapar kortleken ifrån klassen Deck
game_deck.shuffle() # Blandar kortleken

player_card = [game_deck.deal_card(), game_deck.deal_card()] # Spelarens starthand
dealer_card = [game_deck.deal_card(), game_deck.deal_card()] # Dealerns starthand

# Spelmotorn
player_score = 0 
while True: 
    player_score = 0
    for card in player_card:
        player_score += card_value(card, player_score)
    print("Player:", player_card)
    print("Player Score:", player_score)
    if player_score > 21: 
        print("Player bust:")
        break
    action: str = input("Enter [H] for another card, [S] to stop: ").lower()
    if action == "h":
        new_card = game_deck.deal_card()
        player_card.append(new_card)
    elif action == "s":
        break
    else:
        print("Invalid choice, Try Again")
        continue


if player_score > 21: # Hanterar om spelaren blir tjock
    print("Player Hand:", player_card, "Player Score:", player_score)
    print("Dealer Wins: Player Busts")

else: # Hanterar datorns hand
    dealer_score = 0
    while dealer_score < player_score:
        dealer_score = 0
        for card in dealer_card:
            dealer_score += card_value(card, dealer_score)
        if dealer_score < player_score or dealer_score < 21:
            new_card = game_deck.deal_card()
            dealer_card.append(new_card)
    print("Dealer Hand:", dealer_card, "Dealer Score:", dealer_score)


    #   Vinstmeddelanden
    if dealer_score > 21: 
        print("Player Wins: Dealer Busts")
    elif player_score > dealer_score:
        print("Player Wins")
    elif dealer_score > player_score:
        print("Dealer Wins")
    else:
        print("Same Score, Dealer Wins")