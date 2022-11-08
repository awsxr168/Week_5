# This file is where game logic lives. No input or output happens here. The logic in this file should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""

    winner = ""
    if board[0][0] == board[1][0] == board[2][0]:
        winner = board[0][0]
        return winner
    if board[0][1] == board[1][1] == board[2][1]:
        winner = board[0][1]
        return winner
    if board[0][2] == board[1][2] == board[2][2]:
        winner = board[0][2]
        return winner
    if board[0][0] == board[0][1] == board[0][2]:
        winner = board[0][0]
        return winner
    if board[1][1] == board[1][1] == board[1][2]:
        winner = board[1][1]
        return winner
    if board[2][0] == board[2][1] == board[2][2]:
        winner = board[2][0]
        return winner
    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
        return winner
    if board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]
        return winner
    else:
        return "It was a draw"

    return None  # FIXME


def other_player(player):

    if get_winner(board) == 'O':
        player = 'X'
        return player
    elif get_winner(board) == 'X':
        player = 'O'
        return player
    else:
        return "It was a draw"
    
    """Given the character for a player, returns the other player."""
    return "O"  # FIXME

board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]

player = ""

print(get_winner(board), "won")
print(other_player(player), "lost")