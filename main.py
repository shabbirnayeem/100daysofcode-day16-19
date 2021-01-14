############### Blackjack Project #####################
import random
#from replit import clear
import art

def deal_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(cards)

def calculate_score(cards):

	if sum(cards) == 21 and len(cards) == 2:
		return 0
	if 11 in cards and sum(cards) > 21:
		cards.remove(11)
		cards.append(1)
	return sum(cards)

#Create a function called compare() and pass in the user_score and computer_score. 
def compare(player_score, dealer_score):
	if player_score > 21 and dealer_score > 21:
		return "You went over. You lose."

	if player_score == dealer_score:
		return "Its a Draw."
	elif dealer_score == 0:
		return "Dealer wins with Blackjack"
	elif player_score == 0:
		return "You win with Blackjack"
	elif player_score > 21:
		return "You went over. you lose"
	elif dealer_score > 21:
		return "Dealer went over you win"
	elif player_score > dealer_score:
		return "You Win."
	elif dealer_score > player_score:
		return "Dealer Win."




def play_game():

	print(art.logo)

 #Deal the user and computer 2 cards each using deal_card() and append().
	user_cards = []
	computer_cards = []
	is_game_over = False

	for _ in range(2):
		user_cards.append(deal_card())
		computer_cards.append(deal_card())


#The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
	while not is_game_over:

		#Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
		user_score = calculate_score(user_cards)
		computer_score = calculate_score(computer_cards)
		print(f"Your cards: {user_cards}, current_score: {user_score}")
		print(f"Computer's first card: {computer_cards[0]}")

		if user_score == 0 or computer_score == 0 or user_score > 21:
			is_game_over = True
		else:
			#If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
			another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
			if another_card == 'y':
				user_cards.append(deal_card())
			else:
				is_game_over = True

	#Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
	# computer play
	while computer_score != 0 and  computer_score < 17:
		computer_cards.append(deal_card())
		computer_score = calculate_score(computer_cards)

	print(f"		Your final hand: {user_cards}, final score: {user_score}")
	print(f"		Dealer's final hand: {computer_cards}, final score: {computer_score}")
	print(compare(player_score=user_score, dealer_score=computer_score))

#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want want to game of Blackjack? Type 'y' or 'n': ") == 'y':
	#clear()
	play_game()

