'''tic-tac-toe game'''

class Player:
    '''Define player and their piece'''
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece


class Move:
    '''Set who made the move and their position'''
    def __init__(self, author, position):
        self.author = author
        self.position = position


class Board:
    '''Contains all moves on the board'''
    # [-,-,x]
    # [-,-,-]
    # [-,-,-]

    def __init__(self, moves=[["-" for _ in range(3)] for _ in range(3)]):
        self.moves = moves
    
    
    def display(self):
        '''Prints out the board for users to see'''

        print(self.moves[0])
        print(self.moves[1])
        print(self.moves[2])


    def add_move(self, move):
        '''Adds move to the board'''
        self.moves[int(move.position[0])][int(move.position[1])] = move.author.piece


class Game:
    ''''''
    def __init__(self, board, player1, player2, started_at=None, finished_at=None):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.started_at = started_at
        self.finished_at = finished_at

def set_players():
    player1 = Player(input('Player 1 name: '), input('Player 1 piece: '))
    player2 = Player(input('Player 2 name: '), input('Player 2 piece: '))
    
    return [player1, player2]


[player1, player2] = set_players()
my_board = Board()
my_game = Game(my_board, player1, player2)

def play_game():
    first_move = Move(player1, input(f"Choose your move {player1.piece}: ").split())
    my_board.add_move(first_move)
    my_board.display()

    second_move = Move(player2, input(f"Choose your move {player2.piece}: ").split())
    my_board.add_move(second_move)
    my_board.display()

    play_game()

play_game()