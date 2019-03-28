# from __future__ import print_function
from itertools import product
from flask_restful import Resource, Api, reqparse
from flask import Flask, json, request

app = Flask(__name__)
api = Api(app)


class Mini_Chess(Resource):

    def __init__(self):

        self.board = "ABC_E _GHIJ KLMNO PQRST UV__Y".split()
        print(self.board)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', location=['headers', 'values'])
        parser.add_argument('x', type=str, required=False)
        parser.add_argument('y', type=str, required=False)
        parser.add_argument('Authorization', location='headers', type=str)

        if "Authorization" in request.headers:
            args = parser.parse_args()
            x = args['x']
            y = args['y']
            result = Mini_Chess.knight_strings(self, x, y)
            return {"Sucess": "knight strings are:{}".format(json.dumps(result))}

    def duplicate_characters(self, sequence):
        unique = set(sequence)
        return len(unique) != len(sequence)

    def Game_moves(self, pos):
        (x, y) = pos
        moves = list(product([x+1, x-1], [y+2, y-2])) + list(product([x+2, x-2], [y+1, y-1]))
        # print(moves)
        # moves = [(x, y) for x, y in moves if (x >= 0 and y >= 0) and (x < len(self.board) and y < len(self.board[0]))]
        return moves

    def is_valid(self, sequence):  # check for string validation

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
        if duplicate_characters(sequence):
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
        if not self.is_valid(seq):
            return
        yield seq
        # Continue with all other possible moves
        moves = Game_moves(pos)
        for move in moves:
            curr_seq = seq[:]
            dx, dy = move
            for s in self.sequences((x+dx, y+dy), curr_seq):
                yield s
                # print (s)

    def knight_strings(self, x, y):
        result = []
        # if x == None and Y == None:
        #     x, y = 0, 0
        # else:

            # x = int(raw_input("enter x - axis value:") or '0')
            # y = int(raw_input("enter y - axis value:") or '0')


        # We can start at any position on the board
        # for x in range(len(self.board)):p
        #     for y in range(len(self.board[0])):  # Generate all move sequences from that position
        print("Starting position:", (x, y))
        for sequence in Mini_Chess.sequences(self, (x, y), []):
            result.append("".join(sequence))
        print(result)
        return result


api.add_resource(Mini_Chess, "/result")


if __name__ == "__main__":

    app.run(debug=True)

    print(result)
