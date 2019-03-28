# from __future__ import print_function
from itertools import product


class Mini_Chess:

    def __init__(self):

        self.board = "ABC_E _GHIJ KLMNO PQRST UV__Y".split()
        print(self.board)

    def duplicate_characters(sequence):
        unique = set(sequence)
        return len(unique) != len(sequence)

    def knight_moves(self, pos):
        (x, y) = pos
        moves = list(product([x+1, x-1], [y+2, y-2])) + list(product([x+2, x-2], [y+1, y-1]))
        # print(moves)
        moves = [(x, y) for x, y in moves if (x >= 0 and y >= 0) and (x < len(self.board) and y < len(self.board[0]))]
        return moves

    def is_valid(sequence):  # check for string validation

        if any(letter == "_" for letter in sequence):
            return False

        # Strings shorter than 3 letters are always ok.
        if len(sequence) < 3:
            return True

        vowels = "AEIOU"   # Check for vowels
        num_vowels = len([v for v in sequence if v in vowels])

        if num_vowels > 2:    # can't contain more than two vowels
            return False
        # Check for duplicate characters.
        if knight.duplicate_characters(sequence):
            return False
        return True

    def sequences(self, pos, seq=[]):
        x, y = pos
        if x < 0 or x >= len(self.board):
            return
        if y < 0 or y >= len(self.board[0]):
            return
        letter = self.board[x][y]
        seq.append(letter)
        if not knight.is_valid(seq):
            return
        yield seq
        # Continue with all other possible moves
        moves = knight.knight_moves(pos)
        for move in moves:
            curr_seq = seq[:]
            dx, dy = move
            for s in knight.sequences(self.board, (x+dx, y+dy), curr_seq):
                se = (yield s)
                print (se)

    def Knight_Strings(self):
        result = []
        # (x, y) = (2, 3)
        # pos = (x, y)
        x = input("enter x - axis value:")
        y = input("enter y - axis value:")
        # We can start at any position on the board
        # for x in range(len(self.board)):
        #     for y in range(len(self.board[0])):  # Generate all move sequences from that position
        print("Starting position: ", x, y)
        for sequence in knight.sequences((x, y), []):
            result.append("".join(sequence))
        print(result)
        return result



# Move knight on board
# if __name__ == "__main__":

    # str_pos = (2,5)

knight = Mini_Chess()

knight.Knight_Strings()