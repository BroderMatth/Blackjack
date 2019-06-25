import random

suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
cards = {"Ace": [1, 11], "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

class Deck:

    def __init__(self):
        self.deck = []

    def __str__(self):
        return str(self.deck)

    def create_deck(self):
        for suit in suits:
            for card in cards:
                self.deck.append(card + ' of ' + suit)
        random.shuffle(self.deck)


class Cards:

    def __init__(self):
        self.playercards = []
        self.playervalues = []
        self.compcards = []
        self.compvalues = []

    def give_cards(self):
        if len(self.playercards) == 0:
            for x in range(2):
                self.playercards.append(d.deck.pop())
            print("Your cards are: " + ', '.join(self.playercards))
        else:
            while sum(self.playervalues) < 21:
                anothercard = input("Would you like another card?").lower()
                if anothercard == 'yes':
                    self.playercards.append(d.deck.pop())
                    print("Your cards are: " + ', '.join(self.playercards))
                    self.evaluate_cardvalue()
                    print(sum(self.playervalues))
                elif anothercard == 'no':
                    self.evaluate_cardvalue()
                    break
                else:
                    print("Sorry, I don't understand!")

    def evaluate_cardvalue(self):
        self.playervalues.clear()
        for x in self.playercards:
            self.playervalues.append(cards[x.split()[0]])
        if [1,11] in self.playervalues:
            self.playervalues.remove([1, 11])
            if sum(self.playervalues) > 10:
                self.playervalues.append(1)
            elif sum(self.playervalues) <= 10:
                self.playervalues.append(11)

        print(self.playervalues)

    def evaluate(self):
        if sum(self.playervalues) < 21:
            print('Less')
        elif sum(self.playervalues) == 21:
            print('Congratulations! You win!')
        else:
            print('You went over 21! You lose!')

    def give_comp_cards(self):
        if len(self.compcards) == 0:
            for n in range(2):
                self.compcards.append(d.deck.pop())
            print("Comp cards are: " + ', '.join(self.compcards))
        else:
            self.evaluate_compcardvalue()
            print(self.playervalues)

            if sum(self.compvalues) < 21 and sum(self.compvalues) < sum(self.playervalues):
                while True:
                    self.compcards.append(d.deck.pop())
                    print("Comp cards are: " + ', '.join(self.compcards))
                    self.evaluate_compcardvalue()
                    print(sum(self.compvalues))
                    print(d)

            elif sum(self.compvalues) <= 21 and sum(self.playervalues) > 21:
                print('The Computer has won!')


            elif sum(self.compvalues) > 21 and sum(self.playervalues) <= 21:
                print('You have won!')


            elif sum(self.compvalues) > 21 and sum(self.playervalues) > 21:
                print('Nobody has won')


            else:
                print(self.compvalues)
                print('here')


    def evaluate_compcardvalue(self):
        self.compvalues.clear()
        for x in self.compcards:
            self.compvalues.append(cards[x.split()[0]])
        if [1,11] in self.compvalues:
            self.compvalues.remove([1, 11])
            if sum(self.compvalues) > 10:
                self.compvalues.append(1)
            else:
                self.compvalues.append(11)

        print(self.compvalues)

    def evaluate_comp_total(self):
        if sum(self.compvalues) < 21:
            print('Less')
        elif sum(self.compvalues) == 21:
            print('Comp wins')
        else:
            print('You went over 21! You lose!')


d = Deck()
d.create_deck()
print(d)

c = Cards()
for x in range(2):
    c.give_cards()

c.evaluate()

for y in range(2):
    c.give_comp_cards()

c.evaluate_comp_total()








