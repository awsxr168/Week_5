# This file contains the Command Line Interface (CLI) for the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    while winner == None:
        
        # TODO: Show the board to the user.
        
        """The board:"""
        print(board[0])
        print(board[1])
        print(board[2])
        
        # TODO: Input a move from the player.
        """The player:"""
        def move(board):
            while board[0][0] == board[1][0] == board[2][0] or board[0][1] == board[1][1] == board[2][1] or board[0][2] == board[1][2] == board[2][2] or board[0][0] == board[0][1] == board[0][2] or board[1][1] == board[1][1] == board[1][2] or board[2][0] == board[2][1] == board[2][2] or board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0] is not True:
                row = int(input("Input the row:"))
                col = int(input("Input the col:"))
                player = str(input("Input 'X' or 'O'):"))
                # TODO: Update the board.
                """The updated board:"""
                board[row][col] = player
                print(board[0])
                print(board[1])
                print(board[2])
                # TODO: Update who's turn it is.
                print("TODO: take a turn!")
                """The other player:"""
                move(board)
                if board[0][0] == board[1][0] == board[2][0] or board[0][1] == board[1][1] == board[2][1] or board[0][2] == board[1][2] == board[2][2] or board[0][0] == board[0][1] == board[0][2] or board[1][1] == board[1][1] == board[1][2] or board[2][0] == board[2][1] == board[2][2] or board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
                    break
        
        move(board)
        winner = 'X'  # FIXME