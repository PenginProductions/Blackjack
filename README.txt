This Python project uses methods from three class files.

	games.py => contains basic constructor and toString methods for displaying a player's name and score.
		     This class also contains methods to make prompting players more streamline.

	card.py=> contains superclass structure for basic playing card, hand, and deck objects.

        blackjack_newShuffle.py => contains subclass structure for blackjack cards, hands, players and the dealer as
			  well as a blackjack game class as well. In addition to the class features, this file 
			  contains the game loop for actually playing the game.
__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
To Run:

	1) Ensure playBlackJack.bat is in the same directory as the python files.
	
	2) Launch playBlackJack.bat

__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
Tips:

When playing, the computer determines if there is enough cards left in the deck to deal the initial cards to each 
of the players and the dealer. If there is not enough cards, the computer will reshuffle the deck.

However, in the case that there are enough cards to deal but not enough cards when hitting the game will only tell you
there are not enough cards. Fixing this functionality was intended for the next version of this game.