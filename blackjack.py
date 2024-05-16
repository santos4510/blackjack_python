import random
from logo import logotipo
print(logotipo)
# Definir los palos y valores
suits = ["Hearth", "Diamonds", "Clubs", "Spades"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
initial_money = 100
# Crear la baraja de cartas
deck = [value + " de " + suit for suit in suits for value in values]
# Barajar la baraja
random.shuffle(deck)

def deal_card(deck):
    return deck.pop()

def calculate_hand_value(hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    value = 0
    aces = 0

    for card in hand:
        card_value = card.split(' ')[0]
        value += values[card_value]
        if card_value == 'A':
            aces += 1

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

def play_blackjack():
    # Barajar la baraja
    random.shuffle(deck)
    
    # Repartir cartas iniciales
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Mostrar las manos
    print(f"Your hand: {player_hand}, Value: {calculate_hand_value(player_hand)}")
    print(f"Hand of dealer: [{dealer_hand[0]}, 'Hidden card']")

    global initial_money
    wagger = bet()
    
    # Turno del jugador
    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to 'hit' (hit another card) or 'stand' (keep your hand)? ").lower()
        if action == 'hit':
            player_hand.append(deal_card(deck))
            print(f"Your hand: {player_hand}, Value: {calculate_hand_value(player_hand)}")
        else:
            break

    # Verificar si el jugador se pasa de 21
    if calculate_hand_value(player_hand) > 21:
        print("¡You went over 21! You lose.")
        check_wallet()
        return

    # Turno del dealer
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    print(f"Hand of dealer: {dealer_hand}, Value: {calculate_hand_value(dealer_hand)}")

    # Determinar el ganador
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        wallet('win', wagger)
        print("You Won!")
        check_wallet()
    elif player_value < dealer_value:
        print("You lost.")
        check_wallet()
    else:
        tie = wagger / 2
        wallet('tie', tie)
        print("Tie.")
        check_wallet()
    
    
    
def bet():
    bet_Player = int(input("How much are you going to bet?\n"))
    print(f"The dealer bet {bet_Player}€")
 
    wagger = bet_Player + bet_Player
    wallet('bet', bet_Player)
    return wagger


def wallet(moviment, value):
    global initial_money
    if moviment == "bet":
        initial_money -= value
    else:
        initial_money += value
    return initial_money

def check_wallet():
    global initial_money
    print(f"You have {initial_money}")
    action =  input("Do you want to play again?\n")
    if action == 'yes':
        play_blackjack()
    else: 
     print("Goodbye.")   

# Iniciar el juego
play_blackjack()
    