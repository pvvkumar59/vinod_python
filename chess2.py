from __future__ import print_function
from itertools import product

def duplicate_characters(sequence):
    unique = set(sequence)
    return len(unique) != len(sequence)


def knight_moves(pos):
    x, y = pos
    moves = list(product([x+1, x-1], [y+2, y-2])) + list(product([x+2, x-2], [y+1, y-1]))

    # moves = [[x+2, y-1],[x+2, y+1],[x, y+2]]
    print(moves)
    # moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < len(board) and y < len(board)]
    return moves


def is_valid(sequence):
    """
    A string is not valid if the knight moves onto a blank square
    and the string cannot contain more than two vowels.
    """
    if any(letter == "_" for letter in sequence):
        return False
    # Check for vowels
    # Strings shorter than 3 letters are always ok, as they
    # can't contain more than two vowels
    if len(sequence) < 3:
        return True
    # Check longer sequences for number of vowels
    vowels="AEIUO"
    num_vowels = len([v for v in sequence if v in vowels])
    if num_vowels > 2:
        return False
    # Check for duplicate characters.
    # The original question did not say anything about
    # repeated characters, but ignoring them would lead to infinite
    # sequences, such as AMAMAMA..., where the knight makes the same sequence
    # of moves over and over again
    if duplicate_characters(sequence):
        return False
    return True


def sequences(board, pos, seq=[]):  # function to generate string sequences
    x, y = pos
    # Check for out of range errors
    if x < 0 or x >= len(board):
        return
    if y < 0 or y >= len(board[0]):
        return
    letter = board[x][y]
    seq.append(letter)
    if not is_valid(seq):
        return
    yield seq
    # Continue with all other possible moves
    moves = knight_moves(pos)
    for move in moves:
        curr_seq = seq[:]
        print(("'''''''''''''''''"))
        print(curr_seq)
        dx, dy = move
        for s in sequences(board, (x+dx, y+dy), curr_seq):
            yield s
            print(s)


def knight(board):
    result = []
    x, y = 2, 4
    # We can start at any position on the board
    # for x in range(i):
    #     for y in range(j):
    # Generate all move sequences from that position
    print("Starting position: ", x, y)
    for sequence in sequences(board, (x,y), []):
        result.append("".join(sequence))
    print(result)
    return result


# Miniature chess board where the Knight to move on
board = "ABC_E _GHIJ KLMNO PQRST UV__Y".split()
print(board)
print("+++++++++")
h = (knight(board))
