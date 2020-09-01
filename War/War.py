#random function is imported
import random 

#deck class is defined
class Deck: 
	# constructor is created & deck states initialized 
	def __init__(self):
		#deck is created, suit & rank attributes are passed to each element in the list
		self.cardList = [Card(suit, rank) for suit in Card.suit for rank in Card.rank]
		
	#shuffle method is created to shuffle the deck of cards
	def shuffle(self): 
		random.shuffle(self.cardList)

	#method is created to deal cards out to players from the deck 
	def dealOne(self, player): 
		deal = self.cardList.pop(0)
		player.hand.append(deal)

	#overrided string method that allots for printing the deck out
	def __str__(self):
		s, i = '', 0
		for card in self.cardList:
			s += ('%+4s' % (str(card)))
			i += 1
			if i == 13: 
				s += ('\n')
				i = 0
		return(s)
				

#card class is defined
class Card: 
	#class variables suit & rank are created
	suit = ('C', 'D', 'H', 'S')
	rank = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

	# constructor is created & card states initialized
	def __init__(self, suit, rank):
		#suit and rank attributes are passed to each card object
		self.suit = suit
		self.rank = rank

	#overrided string method that allots for printing card objects
	def __str__(self): 
		return(self.rank + self.suit)


#class player is defined
class Player: 
	#constructor is created & player's hand and hand total are initialized
	def __init__(self): 
		self.hand = []
		self.handTotal = 0

	#method is defined to find which player still has cards after the game. 
	#this allows us to findout who won the game
	def handNotEmpty(self): 
		return(len(self.hand) != 0)

	#overrided string method that allots for printing out the player's hand
	def __str__(self): 
		s, i = '', 0
		for card in self.hand:
			s += ('%+4s' % (str(card)))
			i += 1
			if i == 13: 
				s += ('\n')
				i = 0
		return(s)
		

#playGame function, simulates each round
def playGame(cardDeck, player1, player2): 
	#beginning format
	print('\n\nInitial hands:\nPlayer 1:')
	print(player1, '\n')
	print('Player 2:')
	print(player2, '\n\n')

	#variables initialized to be used in while loop control structure
	value = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
	i, count = 0, 0

	#iterative control structure to progress rounds of the game
	while (len(player1.hand) != 0) and (len(player2.hand) != 0):
		#formatting 
		print('ROUND %d:' % (i + 1))
		print('Player 1 plays: ', player1.hand[0])
		print('Player 2 plays: ', player2.hand[0])
		print()
		
		#Standard Case, player1 wins 
		if value.index(player1.hand[0].rank) > value.index(player2.hand[0].rank):
			print('Player 1 wins round', i+1, ': ', player1.hand[0], '>', player2.hand[0], '\n')
			reward1, reward2 = player1.hand.pop(0), player2.hand.pop(0)
			player1.hand.extend([reward1, reward2])

		#Standard Case, player2 wins
		elif value.index(player2.hand[0].rank) > value.index(player1.hand[0].rank):
			print('Player 2 wins round', i+1, ': ', player2.hand[0], '>', player1.hand[0], '\n')
			reward1, reward2 = player1.hand.pop(0), player2.hand.pop(0)
			player2.hand.extend([reward1, reward2])

		#case of War!, recursive function is called
		else: 
			print('War starts: ', player1.hand[0], '= ', player2.hand[0])
			war(player1, player2, count, value, i)
			print()
			

		#displaying players hand at the end of each round
		print('Player 1 now has', len(player1.hand), 'card(s) in hand:')
		print(player1)

		print('Player 2 now has', len(player2.hand), 'card(s) in hand:')
		print(player2)
		print('\n')
		i += 1

#recursive function designed for the case of War, remedies consecutive wars as well
def war(player1, player2, count, value, i):
	#base case 1: player 1 wins war
	if value.index(player1.hand[count].rank) > value.index(player2.hand[count].rank):
		print('\nPlayer 1 wins round', i+1, ': ', player1.hand[count], '>', player2.hand[count])
		player1.hand.extend(player1.hand[:count + 1])
		player1.hand.extend(player2.hand[:count + 1])
		player1.hand, player2.hand = player1.hand[count+1:], player2.hand[count+1:]
		return (player1, player2, count)

	#base case 2: player 2 wins war
	if value.index(player2.hand[count].rank) > value.index(player1.hand[count].rank): 
		print('\nPlayer 2 wins round', i+1, ': ', player2.hand[count], '>', player1.hand[count])
		player2.hand.extend(player1.hand[:count + 1])
		player2.hand.extend(player2.hand[:count + 1])
		player1.hand, player2.hand = player1.hand[count+1:], player2.hand[count+1:]
		return (player1, player2, count) 

	#case of war, 3 cards are burned 4th card is placed face up
	if value.index(player1.hand[count].rank) == value.index(player2.hand[count].rank):
		for j in range(1+count, 5+count): 
			if j == 4+count: 
				print('Player 1 puts %+4s face up' % (player1.hand[j]))
				print('Player 2 puts %+4s face up' % (player2.hand[j]))
			else: 	
				print('Player 1 puts %+4s face down' % (player1.hand[j]))
				print('Player 2 puts %+4s face down' % (player2.hand[j]))
	
		j = 0
		count += 4 

		#recursively calls the function
		return(war(player1, player2, count, value, i))


#main program
def main():

	cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
	print("Initial deck:")
	print(cardDeck)                 # print the deck so we can see that you built it correctly
			
	random.seed(15)                # leave this in for grading purposes
	cardDeck.shuffle()              # shuffle the deck
	print("Shuffled deck:")
	print(cardDeck)                 # print the deck so we can see that your shuffle worked

	player1 = Player()              # create a player
	player2 = Player()              # create another player

	for i in range(26):             # deal 26 cards to each player, one at 
		cardDeck.dealOne(player1)    #   a time, alternating between players
		cardDeck.dealOne(player2)

	playGame(cardDeck,player1,player2)

	if player1.handNotEmpty():
		print("Game over.  Player 1 wins!")
	else:
		print("\n\nGame over.  Player 2 wins!")

	print ("\n\nFinal hands:")    
	print ("Player 1:   ")
	print (player1)                 # printing a player object should print that player's hand
	print ("\nPlayer 2:")
	print (player2)                 # one of these players will have all of the cards, the other none

main()