import random
class Card:
    def __init__(self, id, name, suit, value, visibility = True):
        self.id = id
        self.name = name + " " + suit.title()
        self.suit = suit.title()
        self.value = value
        self.visibility = visibility
        if self.id == 11:
            self.name = "Jack of " + self.suit 
            self.value = 10
        if self.id == 12:
            self.name = "Queen of " + self.suit
            self.value = 10
        if self.id == 13:
            self.name = "King of " + self.suit
            self.value = 10
        if self.id == 1:
            self.name = "Ace of " + self.suit
            self.value = 11
    
    def __repr__(self):
        if self.visibility == False:
            return "Hidden"
        else:  
            return self.name

def generate_cards(suit): 
    cards = []
    for i in range(1, 14):
        card_i = Card(i, str(i), suit, i)
        cards.append(card_i)
    return cards

list_of_suits = ["diamonds", "clubs", "spades", "hearts"]

all_cards = [] 

for suit in list_of_suits:
    all_cards.extend(generate_cards(suit))

def shuffle_cards():
    deck = random.sample(all_cards, k = len(all_cards))
    return deck

current_deck = shuffle_cards()

user_hand = []

ai_hand = []

def deal_card(hand, deck):
    dealt_card = deck.pop(0)
    hand.append(dealt_card)

def card_count(hand):
    count_card_list = []
    for card in hand:
        count_card_list.append(card.value)
    count_card_sum = sum(count_card_list)
    while 11 in count_card_list:
        if count_card_sum > 21:
            for i in range(len(count_card_list)):
                if count_card_list[i] == 11:
                    count_card_list[i] = 1
                    count_card_sum = sum(count_card_list)
                    break
        else:
            break
    return count_card_sum

def ai_decision(hand, deck):
    if len(hand) == 1:
        deal_card(hand,deck)
        hand[1].visibility = False
    elif card_count(hand) < 17:
        deal_card(hand, deck)
    else:
        print("The House stands.")

def reveal_hole(hand):
    for card in hand:
        if card.visibility == False:
            card.visibility = True
    string_to_return = "The House reveals its hand: " + str(hand)
    return string_to_return

game_running = True

print("Welcome to Blackjack!")

while game_running:
    if user_hand == []:
        user_input = input("Type \'Hit me\' to be dealt a card.")
    else:
        user_input = input("Type \'Hit me\' to be dealt a card or \'Stand\' to stand.")
    if user_input.lower() == "hit me":
        deal_card(user_hand, current_deck)
        print("You have:", user_hand)
        ai_decision(ai_hand, current_deck)
        print("The House has:", ai_hand)
        current_hand_sum = card_count(user_hand)
        ai_hand_sum = card_count(ai_hand)
        if ai_hand_sum > 21 and current_hand_sum > 21:
            print(reveal_hole(ai_hand))
            print("Everyone lost!")
            game_running = False
        if ai_hand_sum == 21 and current_hand_sum == 21:
            print(reveal_hole(ai_hand))
            print("Blackjack! Everyone wins!")
            game_running = False
        if current_hand_sum == 21:
            print("Blackjack!")
            print("You win! Thank you for playing. Goodbye.")
            game_running = False
        if current_hand_sum > 21:
            print(reveal_hole(ai_hand))
            print("Busted! The House wins.")
            print("Thank you for playing. Goodbye.")
            game_running = False
        if ai_hand_sum == 21:
            print(reveal_hole(ai_hand))
            print("The House has Blackjack. Thank you for playing. Goodbye.")
            game_running = False
        if ai_hand_sum > 21 and current_hand_sum < 21:
            print(reveal_hole(ai_hand))
            print("The House loses. Thank you for playing. Goodbye.")
            game_running = False
        if ai_hand_sum > 21 and current_hand_sum > 21:
            print(reveal_hole(ai_hand))
            print("Everyone lost!")
            game_running = False
    if user_input.lower() == "stand":
        print("You have: ", user_hand)
        ai_decision(ai_hand, current_deck)
        if ai_hand_sum < 21 and ai_hand_sum > current_hand_sum:
            print(reveal_hole(ai_hand))
            print("The House wins. Thank you for playing. Goodbye.")
            game_running = False
        if ai_hand_sum < 21 and ai_hand_sum < current_hand_sum:
            print(reveal_hole(ai_hand))
            print("You win. Thank you for playing. Goodbye.")
            game_running = False
        if ai_hand_sum == current_hand_sum:
            print(reveal_hole(ai_hand))
            print("It's a draw. Everyone wins!") 
            game_running = False
        