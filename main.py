############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo

def blackjack():
  def deal():
    card = random.choice(cards)
    return card
  
  def deal_first_hand():
    hand = random.sample(cards, 2)
    return hand

  def show_hands():
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Computer's first card: {dealer_hand[0]}") 

  def show_final_hands():
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}") 
  
  def check_blackjack():
  
    if len(dealer_hand) == 2 and dealer_score == 21:
      dealer_blackjack = True
    
    if len(player_hand) == 2 and player_score == 21:
      player_blackjack = True

  player_blackjack = False
  dealer_blackjack = False
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
  
  keep_playing = True
  
  dealer_hand = deal_first_hand()
  player_hand = deal_first_hand()
  dealer_score = sum(dealer_hand)
  player_score = sum(player_hand)
  
  check_blackjack()
  
  if player_blackjack == True or dealer_blackjack:
    keep_playing = False
  else:
    show_hands()
    
  
  while keep_playing == True:
    cont = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if cont == 'n':
      keep_playing = False
  
    if cont == 'y':  
      player_hand.append(deal())
      player_score = sum(player_hand)
  
    if player_score > 21 and '11' in player_hand:
      i = player_score.index('11')
      player_hand[i] = "1"
      player_score = sum(player_hand)
    
    if player_score > 21:
      keep_playing = False
  
    show_hands()
    
  if keep_playing == False:
  
    if player_blackjack == True and dealer_blackjack == False:
      show_final_hands()
      print("You got a BlackJack, you win!")
      
    elif player_blackjack == True and dealer_blackjack == False:
      show_final_hands()
      print("You got a BlackJack, you win!")  
  
    elif player_blackjack == True and dealer_blackjack == True:
      show_final_hands()
      print("You both got a BlackJack!! It's a draw!") 
  
    else:
      
      while dealer_score < 21:
        dealer_hand.append(deal())
        dealer_score = sum(dealer_hand)
        show_final_hands()
    
      if player_score > dealer_score and player_score <= 21:
        print("You WIN!")
      elif player_score < 21 and dealer_score > 21:
        print("You WIN!")
      elif player_score > 21:
        print("You LOSE!")
      elif player_score < 21  and player_score < dealer_score and dealer_score < 21:
        print("You LOSE!")
      elif player_score == dealer_score and player_score <= 21:
        print("Draw!")

  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if play == 'y':
    blackjack()
  
print(logo)
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if play == 'y':
  blackjack()

