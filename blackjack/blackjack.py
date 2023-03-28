import random
def generate_deck(_suits,_cards):
    random.seed(0)
    n=0
    deck = [(i,j) for i in _suits for j in _cards]
    random.shuffle(deck)
    while True:
        yield deck[n]
        n += 1
        if n== 52:
            random.shuffle(deck)
            n=0

suits = ["Spades", "Heart", "Clubs", "Diamonds"]
cards =["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
shuffled_deck = generate_deck(suits,cards)
def get_next_card():
    return next(shuffled_deck)

def card_value(card):
    if card[1] in ['A','J','Q']:
        return 10
    elif card[1] in ['K']:
        if card[0] in ['Hearts', 'Diamonds']:
            return 1
        else:
            return 11
    else:
        return int(card[1])
    
def total_value(cards):
    total = 0
    i = 0
    while i < len(cards):
        total += card_value(cards[i])
        i += 1
    return total

sages_money = int(input("Sage's money: "))
num_games = int(input("Number of games: "))

for game in range(1, num_games + 1):
    print("Game: " + str(game))

    sages_cards = [get_next_card(), get_next_card()]
    kings_cards = [get_next_card(), get_next_card()]
  
    
    print("King's cards: (*)" + str(kings_cards[1]))
    print("Total value:", card_value(kings_cards[1]))
    print("Sage's cards:", sages_cards)
    print("Total value:", total_value(sages_cards))
    
    while True:
        if total_value(sages_cards) == 21:
            sages_money += 50
            print("It is Blackking! You won!")
            break
        elif total_value(sages_cards) > 21:
            sages_money -= 50
            print("You busted! You lost!")
            break
        else:
            decision = input("Do you want to hit or stand? [H/S] ")
            if decision == 'H':
                sages_cards.append(get_next_card())
                print("Sage's cards:", sages_cards)
                print("Total value:", total_value(sages_cards))
            elif decision == 'S':
                break

    if total_value(sages_cards) < 21:
        print("King's cards:", kings_cards)
        print("Total value:", total_value(kings_cards))

        while total_value(kings_cards) < 17:
            kings_cards.append(get_next_card())
            print("King's cards:", kings_cards)
            print("Total value:", total_value(kings_cards))

        if total_value(kings_cards) > 21:
            sages_money += 50
            print("King busted! You won!")
        elif total_value(kings_cards) > total_value(sages_cards):
            sages_money -= 50
            print("King has higher value. You lost!")
        elif total_value(kings_cards) == total_value(sages_cards):   
            print("It is a tie!")
        else:
            sages_money += 50
            print("You have higher value. You won!")

print("Final money is", sages_money)