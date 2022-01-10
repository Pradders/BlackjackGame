#Import packages
from random import randint

#Define a deck of cards
def deck():
    #Set face value cards
    card_number = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    card_suit = ['Clubs','Spades','Diamonds','Hearts']
    #Set up deck of cards
    deck = []
    for i in card_suit:
        for j in card_number:
            deck.append(j + ' ' + i)
    return deck

#Define card values
def card_vals(card):
    if card[0:4] in ['Jack', 'King']:
        return int(10)
    elif card[0:5] in ['Queen']:
        return int(10)
    elif card[0:1] in ['2','3','4','5','6','7','8','9']:
        return int(card[:1])
    elif card[0:2] in ['10']:
        return int(card[:2])
    elif card[0:3] == 'Ace':
        ace_num = input("Is this Ace valued as 1 or 11? ")
        while ace_num != '1' or ace_num != '11':
            if ace_num == '1':
                return(int(ace_num))
                break
            elif ace_num == '11':
                return(int(ace_num))
                break
            else:
                ace_num = input("Is this Ace valued as 1 or 11? ")

#Draw a new card into hand
def draw_card(deck):
    return deck[randint(0,len(deck)-1)]

#Remove a card from the deck
def remove_card_from_deck(deck,card):
    return deck.remove(card)

#Start with new deck
print("START BLACKJACK GAME\n")
new_deck = deck()

#Card counting
player_card_count = 0
dealer_card_count = 0

#Draw first card, start with dealer, then player
dealer_first_card = draw_card(new_deck)
remove_card_from_deck(new_deck,dealer_first_card)
dealer_card_count += 1
player_first_card = draw_card(new_deck)
remove_card_from_deck(new_deck,player_first_card)
print("Player's face-down card is " + player_first_card + "\n")
player_card_count += 1

#Draw second card, start with dealer, then player
dealer_second_card = draw_card(new_deck)
remove_card_from_deck(new_deck,dealer_second_card)
print("Dealer's face-up card is " + dealer_second_card)
dealer_card_count += 1
player_second_card = draw_card(new_deck)
remove_card_from_deck(new_deck,player_second_card)
print("Player's face-up card is " + player_second_card + "\n")
player_card_count += 1

#Check total sum of player's cards
current_player_total = card_vals(player_first_card) + card_vals(player_second_card)
print("Player's current total is " + str(current_player_total))

#Check if player has reached Blackjack or if they want to draw more cards or end the round
if current_player_total == 21:
    print("Blackjack!")
elif current_player_total < 21:
    round = input('Would you like to hit or stand? ')
    while current_player_total < 21:
        #Hit
        if round.lower() == 'hit':
            player_extra_card = draw_card(new_deck)
            remove_card_from_deck(new_deck,player_extra_card)
            print("\nPlayer's extra card is " + player_extra_card)
            player_card_count += 1
            added_card_value = card_vals(player_extra_card)
            current_player_total += added_card_value
            print("Player's current total is " + str(current_player_total))
            #Check if player reached Blackjack
            if current_player_total == 21:
                print("Blackjack!")
                break
            elif current_player_total > 21:
                print("BUST!")
                break
            else:
                round = input('Would you like to hit or stand? ')
                continue
        elif round.lower() == 'stand':
            break
        elif round.lower() != ('hit' or 'stand'):
            round = input('Would you like to hit or stand? ')

#Reveal dealer's hidden card and check score
print("\nDealer's face-down card is " + dealer_first_card)
current_dealer_total = card_vals(dealer_first_card) + card_vals(dealer_second_card)
print("Dealer's current total is " + str(current_dealer_total))

#Check if deaker has reached Blackjack or if they want to draw more cards or end the round
if current_dealer_total == 21:
    print("Blackjack!")
elif current_dealer_total < 21:
    round = input('Would the dealer like to hit or stand? ')
    while current_dealer_total < 21:
        #Hit
        if round.lower() == 'hit':
            dealer_extra_card = draw_card(new_deck)
            remove_card_from_deck(new_deck,dealer_extra_card)
            print("\nDealer's extra card is " + dealer_extra_card)
            dealer_card_count += 1
            dealer_added_card_value = card_vals(dealer_extra_card)
            current_dealer_total += dealer_added_card_value
            print("Dealer's current total is " + str(current_dealer_total))
            #Check if dealer reached Blackjack
            if current_dealer_total == 21:
                print("Blackjack!")
                break
            elif current_dealer_total > 21:
                print("BUST!")
                break
            else:
                round = input('Would the dealer like to hit or stand? ')
                continue
        elif round.lower() == 'stand':
            break
        elif round.lower() != ('hit' or 'stand'):
            round = input('Would the dealer like to hit or stand? ')

#Check who wins
print("\nPlayer's current total is " + str(current_player_total) + " with " + str(player_card_count) + " cards")
print("Dealer's current total is " + str(current_dealer_total) + " with " + str(dealer_card_count) + " cards")
if current_player_total <= 21 and current_dealer_total <= 21:
    if current_dealer_total >= current_player_total:
        print("Dealer wins!")
    else:
        print("Player wins!")
elif current_player_total > 21 and current_dealer_total > 21:
    print("Both players BUST!")
elif current_player_total > 21 and current_dealer_total <= 21:
    print("Dealer wins!")
else:
    print("Player wins!")

print("\nEND BLACKJACK GAME")