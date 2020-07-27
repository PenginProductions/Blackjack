## Robert Giglio III
## 10/18/2016
##
## Blackjack
## From 1 to 7 players compete against a dealer
## Shuffles the deck when out of cards
## NOTE: Console window safe version

import card, games

class BJ_Card(card.Card):
    """A Blackjack card."""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None

        return v

class BJ_Deck(card.Deck):
    """A Blackjack deck."""

    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))
                
class BJ_Hand(card.Hand):
    """A Blackjack hand."""

    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"

        return rep

    @property
    def total(self):
        #if a card in the hand has value of None, then total has None
        for card in self.cards:
            if not card.value:
                return None

        #add up card values, treat Ace as 1
        t = 0
        for card in self.cards:
            t += card.value

        #determin if hand contains an Ace
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        #if hand contains Ace and total is low enough, treat Ace as 11
        if contains_ace and t <= 11:
            #add only 10 since we've already added 1 for the Ace
            t += 10

        return t

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    """A Blackjack Player"""
    
    def is_hitting(self):
        response = games.ask_yes_no(self.name + ", do you want a hit? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")

    def push(self):
        print(self.name, "pushes.")

class BJ_Dealer(BJ_Hand):
    """A Blackjack Dealer"""

    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game(object):
    """A Blackjack Game."""

    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)

        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            separate("SPACE")
            if player.is_busted():
                player.bust()

    def play(self):
        #check if cards are  in the deck
        if len(self.deck.cards) < ((len(self.players) * 2) + 2):
            print("Not enough cards....")
            print("Getting new deck...")
            self.deck.populate()
            print("Shuffleing....")
            self.deck.shuffle()
            print()
            
        #deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card() #hide dealer's first card
        for player in self.players:
            print(player)
        print(self.dealer)
        separate("HALF")
        print()

        #deal additional cards to players
        for player in self.players:
            print(player)
            self.__additional_cards(player)
            separate("HALF")

        self.dealer.flip_first_card() #reveal dealers card

        if not self.still_playing:
            #since all players have busted show dealers hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                #everyone still playing wins
                for player in self.still_playing:
                    player.win()
            else:
                #compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
                        
        #remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("\t\tWelcome to Blackjack!\n")

    names = []
    numer = games.ask_number("How many players? (1-7): ", low = 1, high = 8)
    for i in range(numer):
        name = input("Enter name for player " + str(i+1) + ": ")
        names.append(name)
    separate()

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again? (Y/N): ")
        separate()

def separate(form = "FULL"):
    if(form == "FULL"):
        print("----------------------------------------------------------")
        print("__________________________________________________________")
    elif(form == "HALF"):
        print("----------------------------------------------------------")
    elif(form == "SPACE"):
        print()
    elif(form == "DSPACE"):
        print("\n")

main()
input("\n\nPress the enter key to exit.")
