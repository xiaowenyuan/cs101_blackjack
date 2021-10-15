# Blackjack
## Introduction

This is a simple Blackjack terminal program made in Python for Codecademy's CS101 course. To play, simply download and run the script in your terminal.

## Gameplay

One player can play against a computer Dealer. 

The Dealer will be dealt a single card after the player's initial choice to be hit. The next card the Dealer receives is the Hole--it is hidden from the Player. Only at the end of the game does the Dealer reveal the Hole.

The rules of this Blackjack game are very simple:
* The user/Dealer is dealt a card, and can choose to continue playing and having a card dealt to them, or stand, which holds on to the current hand.
* The value of the card follows the number on the card (ie 8 of hearts has a value of 9=8, and 5 of spades have a value of 5). Face cards (Jack, Queen, King) all have a value of 10. Ace has a value of either 1 or 11.
* If the value of the user's or Dealer's hand sums up to 21, the user or Dealer wins.
* If both players stand, the player with the bigger hand value wins.

## Logic
The logic behind the Dealer's decision to deal to itself or to stand is very simple--no card counting involved! The Dealer simply calculates if its hand is equal to or more than 18--if so, the Dealer stands.
