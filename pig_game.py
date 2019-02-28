import random

class Die:
    '''Returns a random value ranging 1 to 6'''
    def __init__ (self, single_play):
        self.single_play = single_play

    def single_play (self, die):
        die = random.randint(1,6) 
        return die

class Game:
    '''Functions as the main gameloop and determines winner'''

    def __init__ (self, total_score):
        self.total_score = total_score
        
    def game_loop (self, total_score):
        '''Controls the follow of the game'''
        print('''Welcome to Pig, Player 1!

        The object of the game is to accumulate 100 total points. To acquire points you must roll the virtual die by pressing enter. You will receive points equal to the numbers displayed on the die unless it lands one 1, which will end your turn and reduce your score for that round to zero. You may roll the die as many times you desire per round.

        ''')
        players = ['Player 1', 'Player 2']
        play = input('Enter PLAY to begin!')
        if play == 'PLAY' or 'play':
            player = random.choice(players)
        if player == 'Player 1':
            print(f'{player}, it is your turn. Please press enter.')
        print(f'It is {player}\'s turn.')
        while Player.player_1.total_score < 100 and Player.player_2.total_score < 100:
            if player == 'Player 1':
                Player.player_1
                return player == 'Player 2'
            elif player == 'Player 2':
                Player.player_2
                return player == 'Player 1'
        
    # def replay():
    #     '''Prompts user to replay game'''
    #     response = input('Would you like to play again? (Y/N): ')
    #     if response == 'Y' or response == 'y':
    #         Game.game_loop
    #     else:
    #         print('Thanks for playing!')
    #         return
    #     replay()

class Player:
    '''Controls each players turn'''
    def __init__ (self, die):
        self.die = die

    def player_1(self, die):
        ''' '''
        total_score = 0
        p1_round_score = 0
        die_roll = Die.single_play
        while user_input is False:
            if die_roll == 1:
                p1_round_score = 0
                print('Player 1, your turn is over!')
                break
            elif die_roll > 1:
                p1_round_score += die_roll
                total_score += p1_round_score
                print(f'Player 1, your score for the round is now {self.p1_round_score}')
                user_input = input('Press enter to roll the die again. Otherwise, enter anything to hold.')
        print(f'Player 1, your total score is: {self.total_score}')
        if total_score >= 100:
            print(f'Player 1 has won! Total score: {self.total_score}')
    
    def player_2(self, die):
        '''Controls Player 2's decision to roll again while recording the round and total score'''
        total_score = 0
        p2_round_score = 0
        die_roll = Die.single_play
        while total_score < 100:
            if die_roll == 1:
                print('Player 2\'s turn is over!')
                break
            elif p2_round_score < 20:
                p2_round_score += die_roll
                total_score += p2_round_score
                print(f'Player 2\'s score for the round is now {self.p2_round_score}')
            elif p2_round_score >= 20:
                print(f'Player 2\'s score for the round is {self.p2_round_score}')
        print(f'Player 2\'s total score is: {self.total_score}')
        if total_score >= 100:
            print(f'Player 2 has won! Total score: {self.total_score}')
        
if __name__ == "__main__":
    pass