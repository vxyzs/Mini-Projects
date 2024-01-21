import tkinter as tk

class TicTacToeSingle:
    def __init__(self, master):
        self.master = master
        self.master.title("Single player - Tic Tac Toe")
        self.master.config(bg='#f1fdff')
        self.board = [" " for _ in range(9)]
        self.move_history = []
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text=" ",bg='#dcfffc',fg='black', font=('calibri', 16, 'bold'), command=lambda row=i, col=j: self.handle_click(row, col),width=6)
                button.grid(row=i, column=j, padx=1, pady=1, ipadx=20, ipady=20)
                self.buttons.append(button)

        self.status_label = tk.Label(self.master, text="Current Status: ", font=('calibri', 14, 'bold'),bg='#f1fdff')
        self.status_label.grid(row=3, columnspan=3, pady=10)

        self.play_again_button = tk.Button(self.master, text="Play Again", command=self.play_again, state=tk.NORMAL, width=10,bg='#dcfffc')
        self.play_again_button.grid(row=4, column=0, pady=10)

        self.undo_button = tk.Button(self.master, text="Undo", command=self.undo_move, state=tk.DISABLED, width=10,bg='#dcfffc')
        self.undo_button.grid(row=4, column=1, pady=10)

        self.exit_button = tk.Button(self.master, text="EXIT", command=self.master.destroy, width=10,bg='#ff4343')
        self.exit_button.grid(row=4, column=2, pady=10)


    def handle_click(self, row, col):
       if self.board[row * 3 + col] == " ":
           self.board[row * 3 + col] = "X"
           self.move_history.append((row * 3 + col, "X"))
           self.update_gui()


           if self.check_win("X"):
               self.game_over("Hurray!!\nYou Won ")
           else:
               computer_move = self.get_computer_move()
               if computer_move is not None:
                   self.board[computer_move] = "O"
                   self.move_history.append((computer_move, "O"))
                   self.update_gui()


                   if self.check_win("O"):
                       self.game_over("\nComputer Won")
               if self.check_draw():
                   self.game_over("It's a draw")


       if not self.move_history:
           self.undo_button.config(state=tk.DISABLED)
       else:
           self.undo_button.config(state=tk.NORMAL)


       if self.check_win("X") or self.check_win("O") or self.check_draw():
           self.undo_button.config(state=tk.DISABLED)
       else:
           self.undo_button.config(state=tk.NORMAL)


    def get_computer_move(self):
       empty_cells = [i for i, cell in enumerate(self.board) if cell == " "]
       if empty_cells:
           return self.minimax(self.board, "O")  # Use Minimax for the computer's move
       return None


    def minimax(self, board, player):
       available_moves = [i for i, cell in enumerate(board) if cell == " "]


       if self.check_win("X"):
           return -1
       elif self.check_win("O"):
           return 1
       elif self.check_draw():
           return 0


       moves = []
       for move in available_moves:
           new_board = board.copy()
           new_board[move] = player


           if player == "O":
               result = self.minimax(new_board, "X")
               moves.append((result, move))
           elif player == "X":
               result = self.minimax(new_board, "O")
               moves.append((result, move))


       if not moves:  # No available moves
           return 0


       if player == "O":
           return max(moves)[1]
       elif player == "X":
           return min(moves)[1]


    def check_win(self, player):
       for i in range(0, 9, 3):
           if self.board[i] == self.board[i+1] == self.board[i+2] == player:
               self.play_again_button.config(state=tk.NORMAL)
               return True


       for i in range(3):
           if self.board[i] == self.board[i+3] == self.board[i+6] == player:
               self.play_again_button.config(state=tk.NORMAL)
               return True


       if self.board[0] == self.board[4] == self.board[8] == player or self.board[2] == self.board[4] == self.board[6] == player:
           self.play_again_button.config(state=tk.NORMAL)
           return True


       return False


    def check_draw(self):
       if " " not in self.board:
           self.play_again_button.config(state=tk.NORMAL)
           return True
       return False


    def undo_move(self):
       if self.move_history:
           last_move = self.move_history.pop()
           self.board[last_move[0]] = " "
           last_move = self.move_history.pop()
           self.board[last_move[0]] = " "
           self.update_gui()
           self.toggle_undo_button()


    def toggle_undo_button(self):
       if not self.move_history:
           self.undo_button.config(state=tk.DISABLED)
       else:
           self.undo_button.config(state=tk.NORMAL)


    def game_over(self, message):
       self.status_label.config(text=f"Current Status: {message}")
       self.play_again_button.config(state=tk.NORMAL)
       self.undo_button.config(state=tk.DISABLED)
       for button in self.buttons:
           button.config(state=tk.DISABLED)


    def update_gui(self):
       for button, value in zip(self.buttons, self.board):
           button.config(text=value)


    def play_again(self):
       self.board = [" " for _ in range(9)]
       self.move_history = []
       self.update_gui()
       self.play_again_button.config(state=tk.NORMAL)
       self.undo_button.config(state=tk.DISABLED)
       self.status_label.config(text="Current Status: ")
       for button in self.buttons:
           button.config(text=" ", state=tk.NORMAL)


class TicTacToeDouble:
    def __init__(self, master):
        self.master = master
        self.master.title("Double Player")
        self.master.config(bg='#f1fdff')
        self.board = [" " for _ in range(9)]
        self.current_turn = "X"
        self.move_history = []
        self.game_over = False
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text=" ",bg='#dcfffc', font=('normal', 16), command=lambda row=i, col=j: self.handle_click(row, col),width=6)
                button.grid(row=i, column=j, padx=1, pady=1, ipadx=20, ipady=20)
                self.buttons.append(button)

        self.turn_label = tk.Label(self.master, text="", font=('calibri', 14, 'bold'),bg='#f1fdff')
        self.turn_label.grid(row=3, columnspan=3, pady=10)

        self.play_again_button = tk.Button(self.master, text="Play Again", command=self.reset_game, state=tk.NORMAL, width=10,bg='#dcfffc')
        self.play_again_button.grid(row=4, column=0, pady=10)

        self.undo_button = tk.Button(self.master, text="Undo", command=self.undo_move, state=tk.DISABLED, width=10,bg='#dcfffc')
        self.undo_button.grid(row=4, column=1, pady=10)

        self.exit_button = tk.Button(self.master, text="EXIT", command=self.master.destroy, width=10,bg='#ff4343')
        self.exit_button.grid(row=4, column=2, pady=10)


    def handle_click(self, row, col):
       if self.board[row * 3 + col] == " " and not self.game_over:
           move = 3 * row + col
           self.receive_move(move)
          
       if not self.move_history:
           self.undo_button.config(state=tk.DISABLED)
       else:
           self.undo_button.config(state=tk.NORMAL)
          
       if self.game_over:
           self.undo_button.config(state=tk.DISABLED)
       else:
           self.undo_button.config(state=tk.NORMAL) 


    def receive_move(self, move):
       if self.board[move] == " ":
           self.board[move] = self.current_turn
           self.check_win()
           self.move_history.append((move, self.current_turn))
           self.update_gui()
           if self.game_over != True:
               self.switch_turn()
              
    def undo_move(self):
       if self.move_history:
           last_move = self.move_history.pop()
           self.board[last_move[0]] = " "
           self.update_gui()
           self.switch_turn()
           self.toggle_undo_button()


    def toggle_undo_button(self):
       if not self.move_history:
           self.undo_button.config(state=tk.DISABLED)
       else:
           self.undo_button.config(state=tk.NORMAL)


    def check_win(self):
       for i in range(0, 9, 3):
           if self.board[i] == self.board[i + 1] == self.board[i + 2] != " ":
               self.game_over = True
               self.turn_label.config(text=f"Game Over! {self.current_turn} wins!")
               return


       for i in range(3):
           if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
               self.game_over = True
               self.turn_label.config(text=f"Game Over! {self.current_turn} wins!")
               return


       if self.board[0] == self.board[4] == self.board[8] != " " or self.board[2] == self.board[4] == self.board[6] != " ":
           self.game_over = True
           self.turn_label.config(text=f"Game Over! {self.current_turn} wins!")
           return


       if " " not in self.board:
           self.game_over = True
           self.turn_label.config(text="Game Over! It's a draw!")


       self.play_again_button.config(state=tk.NORMAL)


    def switch_turn(self):
       self.current_turn = "O" if self.current_turn == "X" else "X"
       self.turn_label.config(text=f"Current Turn: {self.current_turn}")


    def update_gui(self):
       for button, value in zip(self.buttons, self.board):
           button.config(text=value)


    def reset_game(self):
       self.board = [" " for _ in range(9)]
       self.move_history = []
       self.current_turn = "X"
       self.game_over = False
       self.turn_label.config(text="")
       self.undo_button.config(state=tk.DISABLED)
       for button in self.buttons:
           button.config(text=" ", state=tk.NORMAL)
       self.play_again_button.config(state=tk.NORMAL)


def single():
    root = tk.Tk()
    client = TicTacToeSingle(root)
    root.mainloop()


def double():
    root = tk.Tk()
    client = TicTacToeDouble(root)
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic-Tac-Toe Game")
    root.config(bg='#fffec7')

    window_width = 300
    window_height = 200
    root.geometry(f"{window_width}x{window_height}")

    single_button = tk.Button(root, text="Player vs Computer", command=lambda: single(), font=('normal', 16), width=24,bg='#fffd96')
    single_button.grid(row=0, pady=10, columnspan=5)

    double_button = tk.Button(root, text="Player vs Player", command=lambda: double(), font=('normal', 16), width=24,bg='#fffd96')
    double_button.grid(row=1, pady=10, columnspan=5)

    exit_button = tk.Button(root, text="Exit", command=root.quit, font=('normal', 16), width=24,bg='#e62929')
    exit_button.grid(row=2, column=0, pady=10)

    root.mainloop()
