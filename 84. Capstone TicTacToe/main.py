# Using what you have learnt about Python programming, you will build a text-based version of the Tic Tac Toe game. The game should be playable in the command line just like the Blackjack game we created on Day 11. It should be a 2-player game, where one person is "X" and the other plays "O".

# This is a simple demonstration of how the game works:
# https://www.google.com/search?q=tic+tac+toe

# You can choose how you want your game to look. The simplest is to create a game board using "|" and "_" symbols. But the design is up to you.

# If you have more time, you can challenge yourself to build an AI player to play the game with you.

import os

class TicTacToe:
    def __init__(self) -> None:
        self.board = [i for i in range(1, 10)]
        self.available_moves = [i for i in range(1, 10)]

    def check_winner(self):
        if (self.board[0] == self.board[1] == self.board[2]):
            return self.board[0]
        if (self.board[6] == self.board[7] == self.board[8]):
            return self.board[6]
        if (self.board[0] == self.board[3] == self.board[6]):
            return self.board[0]
        if (self.board[2] == self.board[5] == self.board[8]):
            return self.board[2]
        if (self.board[0] == self.board[4] == self.board[8]):
            return self.board[0]
        if (self.board[2] == self.board[4] == self.board[6]):
            return self.board[2]
        return None

    def check_draw(self) -> bool:
        return len(self.available_moves) == 0

    def print_board(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('|'.join([str(self.board[cell]) for cell in range(0,3)]))
        print('-' * 5)
        print('|'.join([str(self.board[cell]) for cell in range(3,6)]))
        print('-' * 5)
        print('|'.join([str(self.board[cell]) for cell in range(6,9)]))
        print()

    def game_state(self):
        if self.check_winner():
            return self.check_winner()
        if self.check_draw():
            return "draw"
        return None
    
    def make_move(self, player: str, move: int) -> bool:
        if move in self.available_moves:
            self.available_moves.remove(move)
            self.board[move - 1] = player
            return True
        else:
            return False

if __name__ == "__main__":
    players = ['X', 'O']
    player_nr = 0
    ttt = TicTacToe()
    while not ttt.game_state():

        if player_nr + 1 > len(players):
            player_nr = 0 # reset player

        ttt.print_board()

        correct_field = False
        while not correct_field:
            try:
                field = int(input(f"Player {players[player_nr]} choose board field (1-9): "))
            except ValueError:
                continue

            if ttt.make_move(players[player_nr], field):
                correct_field = True
            
        player_nr += 1

    print('\n\nGAME OVER')

    match ttt.game_state():
        case 'X':
            print("Player X wins!")
        case 'O':
            print("Player O wins!")
        case 'draw':
            print("It's a DRAW!")
