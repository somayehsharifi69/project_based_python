"""Author: Somayeh Sharifi
   Date: 29.11.2023
   Description: Rock Paper Scissors Game
"""

import random
from typing import List


class RockPaperScissors:
    """ Main class for Rock Paper Scissors play """
    def __init__(self, name: str):
        self.choices: List(str) = ['rock', 'paper', 'scissors']
        self.user_name = name

    def get_user_choice(self):
        user_choice = input(f'Enter your choice ({self.choices}):')
        if user_choice.lower() in self.choices:
           return user_choice.lower()
        
        print(f'Invalid choice, please choose in ({self.choices}):')
        return self.get_user_choice()
    
    def get_computer_choice(self):
        """ Get computer choice randomly from choices Rock, paper, and scissors. """
        return random.choice(self.choices)
    
    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """Decide the winner of the game based on the user and computer choices.

        Args:
            user_choice: The choice of the user.
            computer_choice: The choice of the computer.
        Returns:
            The result of the game.
        """
        if user_choice == computer_choice:
            return "It is a Tie."
        
        win_combinations = [('rock', 'paper'), ('paper', 'scissors'), ('scissor', 'paper')]
        for win_comb in win_combinations:
            if (user_choice == win_comb[0]) & (computer_choice == win_comb[1]):
                return "Congratulation, you won..."
            
        return "Oh, the computer won..."


    def play(self):
        """Play the game.
           _ Get the uer choice.
           _ Get the computer choice.
           _ Decide the winner.
           _ Print the result.
        """
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(self.decide_winner(user_choice, computer_choice))
        print(f'Your choice: {user_choice}')
        print(f'Computer choice: {computer_choice}')

if __name__ == '__main__':
    game = RockPaperScissors('Ali')

while True:
    game.play()
    continue_game = input('Do you want to play again? (Enter any key to play or enter Q/q to exit.) ')
    if continue_game.lower() == 'q':
        break
