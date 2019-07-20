import random
import os
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
        if card[1] == 'A' and self.value + values[card[1]] > 21 and self.value + 1 <= 21:
            self.value +=1
        else:
            self.value += values[card[1]]
class Chip:
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self, price):
        self.total += price
    def lose_bet(self, price):
        self.total -= price
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
def hit_or_stand(deck, hand):
    global playing
    while True:
        try:
            ask = raw_input("Hit or Stand? (h/s) ")
            if ask != 'h':
                if ask != 's':
                    raise TypeError
        except:
            print 'Bad input!'
            continue
        else:
            break
    if ask == 'h':
        hit(deck, hand)
        return 'h'
    else:
        return 's'

def show_some(player, dealer):
    print "Player's hand: "
    for card in player.cards:
        print '{} of {}'.format(card[1], card[0])
    print "{} points".format(player.value)
    print "\nDealer's hand: "
    for card in dealer.cards[1:]:
        print '{} of {}'.format(card[1], card[0])

def show_all(player, dealer):
    print "Player's hand: "
    for card in player.cards:
        print '{} of {}'.format(card[1], card[0])
    print "{} points".format(player.value)
    print "\nDealer's hand: "
    for card in dealer.cards:
        print '{} of {}'.format(card[1], card[0])
    print "{} points".format(dealer.value)

def player_busts(balance, bet):
    balance.lose_bet(bet)
    print 'You busted!'

def player_wins(balance):
    balance.win_bet(bet)
    print 'You win!'

def dealer_busts(balance):
    balance.win_bet(bet)
    print 'Dealer busted!'

def dealer_wins(balance):
    balance.lose_bet(bet)
    print 'Dealer wins'

def push():
    print 'TIE'
def clear():
    os.system('clear')
def replay():
    while True:
        try:
            ask = raw_input('Your balance is {}$\nPlay again? y/n: '.format(balance.total))
            if ask != 'y':
                if ask != 'n':
                    raise TypeError
            if ask == 'y':
                return 'y'
            elif ask == 'n':
                return 'n'

        except:
            clear()
            print 'Bad input!'
            continue
        else:
            break
def new_game():
    while True:
        try:
            ask = raw_input('Play a new game? y/n ')
            if ask != 'y':
                if ask != 'n':
                    raise TypeError
            if ask == 'y':
                return 'y'
            else:
                return 'n'
        except:
            print 'Bad input!'
            continue
        else:
            break
while True:
    balance = Chip()
    while True:
        clear()
        print 'Your balance is {}$'.format(balance.total)
        while True:
            try:
                bet = int(input('The game begins!\nPlease take a bet '))
                if bet > balance.total or bet < 0:
                    raise ValueError
            except:
                print 'Bad betting, try again: '
                continue
            else:
                break

        clear()
        player = Hand()
        dealer = Hand()
        deck = Deck()
        deck.shuffle()
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())
        player.add_card(deck.deal())
        player.add_card(deck.deal())
        show_some(player, dealer)
        while playing:
            print '\n'
            res = hit_or_stand(deck,player)
            if res == 'h':
                clear()
                show_some(player, dealer)
            if player.value > 21:
                print "\n"
                player_busts(balance, bet)
                break
            if res == 's':
                while dealer.value < 17:
                    hit(deck, dealer)
                clear()
                show_all(player, dealer)
                print "\n"
                if 21 - player.value < 21 - dealer.value:
                    player_wins(balance)
                    break
                elif dealer.value > 21:
                    dealer_busts(balance)
                    break
                elif 21 - dealer.value < 21 - player.value:
                    dealer_wins(balance)
                    break
                elif dealer.value == player.value:
                    push()
                    break
        if balance.total <= 0:
            break
        repl = replay()
        if repl == 'y':
            continue
        else:
            break
    print 'You are out of money'
    new = new_game()
    if new == 'y':
        continue
    else:
        break
