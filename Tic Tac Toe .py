import random
from colorama import init, Fore

init(autoreset=True)

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 10   
        self.current_player = "X"
        self.ai_enabled = False

    def display_board(self):
        print(Fore.CYAN + "\n")
        print(Fore.YELLOW + " {} | {} | {} ".format(
            self.colored(7), self.colored(8), self.colored(9)))
        print(Fore.WHITE + "---+---+---")
        print(Fore.YELLOW + " {} | {} | {} ".format(
            self.colored(4), self.colored(5), self.colored(6)))
        print(Fore.WHITE + "---+---+---")
        print(Fore.YELLOW + " {} | {} | {} ".format(
            self.colored(1), self.colored(2), self.colored(3)))
        print()

    def colored(self, i):
        if self.board[i] == 'X':
            return Fore.GREEN + 'X'
        elif self.board[i] == 'O':
            return Fore.RED + 'O'
        else:
            return Fore.WHITE + str(i)

    def check_winner(self):
        combos = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]
        for c in combos:
            if self.board[c[0]] == self.board[c[1]] == self.board[c[2]] != ' ':
                return self.board[c[0]]
        return None

    def is_draw(self):
        return all(space != ' ' for space in self.board[1:])

    def player_move(self):
        while True:
            try:
                move = int(input(f"Player {self.current_player}, enter your move (1–9): "))
                if 1 <= move <= 9 and self.board[move] == ' ':
                    self.board[move] = self.current_player
                    break
                else:
                    print(Fore.RED + "Invalid move! Try again.")
            except ValueError:
                print(Fore.RED + "Please enter a number between 1 and 9.")

    def ai_move(self):
        move = random.choice([i for i in range(1, 10) if self.board[i] == ' '])
        print(Fore.MAGENTA + f"AI ({self.current_player}) chose {move}")
        self.board[move] = self.current_player

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        print(Fore.BLUE + "Welcome to Numbered Tic Tac Toe!")
        mode = input("Do you want to play against AI? (yes/no): ").strip().lower()
        self.ai_enabled = mode == 'yes'

        while True:
            self.display_board()
            if self.ai_enabled and self.current_player == 'O':
                self.ai_move()
            else:
                self.player_move()

            winner = self.check_winner()
            if winner:
                self.display_board()
                print(Fore.GREEN + f"Player {winner} wins!")
                break
            elif self.is_draw():
                self.display_board()
                print(Fore.CYAN + "It's a draw!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
