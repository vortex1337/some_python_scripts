import random
playing = True
suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J': 10, 'Q':10, 'K':10,'A':11}
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append((suit,rank))
    def __str__(self):
        return str(self.deck)
    def shuffle(self):
        return random.shuffle(self.deck)
    def deal(self):
        choice = random.choice(self.deck)
        self.deck.remove(choice)
        return choice
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card[1]]
    def adjust_for_ace(self):
        for card in self.cards:
            if 'A' in card:
                self.aces += 1
                if self.value + 11 > 21:
                    self.value -= 10
class Chip:
    def __init__(self, bet):
        self.total = 100
        self.bet = bet
    def win_bet(self, price):
        self.total += self.bet
    def lose_bet(self, price):
        self.total -= self.bet
def take_bet():
    global bet
    while True:
        try:
            bet = int(input("Enter a bet: "))
            if bet > player.total:
                raise ValueError
        except:
            print 'Bad input, try again: '
        else:
            break
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
def hit_or_stand(deck, hand):
    global playing
    while playing:
        while True:
            try:
                ask = raw_input("Hit or Stand? ")
                if ask != 'Hit' or ask != 'Stand':
                    raise TypeError
            except:
                print 'Bad input!'
                continue
            else:
                break
        if ask == 'Hit':
            hit()
        else:
            break
def show_some(player, dealer):
    print "Player's hand: {} {}".format(player.cards, player.value)
    print "Dealer's hand: NA, {}".format(dealer.cards[1:])
def show_all(player, dealer):
    print "Player's hand: {} {}".format(player.cards, player.value)
    print "Dealer's hand: {} {}".format(dealer.cards, dealer.value)

def player_busts(player, dealer):
    player.lose_bet(bet)
    if player.total > 21:
        return 'You busted!'

def player_wins(player,dealer):
    if 21 - player.total < 21 - dealer.total:
        player.win_bet(bet)
        return 'You win!'

def dealer_busts(player, dealer):
    player.win_bet(bet)
    if dealer.total > 21:
        return 'Dealer busted!'

def dealer_wins(player, dealer):
    player.lose_bet(bet)
    if 21 - dealer.total < 21 - player.total:
        return 'Dealer wins'

def push(player, dealer):
    if dealer.total == player.total:
        return 'TIE'

while True:
    bet = int(input('The game begins!\nPlease take a bet '))
    player = Hand()
    dealer = Hand()
    deck = Deck()
    deck.shuffle()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    show_some(player, dealer)
