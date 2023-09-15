# CARD
# SUIT, RANK, VALUE
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # CREATE THE CARD OBJECT
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

class Player():

    def __init__(self, name):

        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # LIST OF MULTIPLE CARD OBJECTS
            self.all_cards.extend(new_cards)
        else:
            # FOR A SINGLE CARD OBJECT
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle


for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0

while game_on:
    round_num +=1
    print(f"Rounds {round_num}")

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two Wins!')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One Wins!')
        game_on = False
        break
    
    # START A NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # WHILE AT WAR

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            

            at_war = False
        else:
            print("WAR!")

            if len(player_one.all_cards) < 5:
                print("Player one unable to declare war")
                print("PLAYER TWO WINS!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player TWO unable to declare war")
                print("PLAYER ONE WINS!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())



# new_Deck = Deck()

# new_Deck.shuffle()

# mycard = new_Deck.deal_one()

# # print(mycard)
# # print(len(new_Deck.all_cards))

# new_player = Player("Jose")
# print(new_player)

# # new_player.add_cards(mycard)

# print(new_player)
# new_player.add_cards([mycard,mycard,mycard])
# print(new_player)
# new_player.remove_one()
# print(new_player)





























# new_Deck = Deck()

# new_Deck.shuffle()

# mycard = new_Deck.deal_one()

# print(mycard)
# print(len(new_Deck.all_cards))




# for card_object in new_Deck.all_cards:
#     print(card_object)





# two_hearts = Card("Hearts", "Two")
# three_of_clubs = Card("Clubs",'Three')
# print(three_of_clubs.value < two_hearts.value)




