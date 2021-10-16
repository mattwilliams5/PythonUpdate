import random


class TicTacToe:
    """
        Get your TicTacToe on
    """

    def __init__(self):
        self.board = []

    def create_board(self):
        """
            Creating the board
        """
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def player_one(self):
        """
            First player
        """
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        """
            Getting the game started
        """
        self.board[row][col] = player

    def setup_win(self, player):
        """
            Game on!
        """
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def filled_board(self):
        """
            Board
        """
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_turn(self, player):
        """
            Swap turn
        """
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        """
            Actual board setup
        """
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        """
            Game on
        """
        self.create_board()

        player = 'X' if self.player_one() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.setup_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.filled_board():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
