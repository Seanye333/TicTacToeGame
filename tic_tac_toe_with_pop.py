#!/usr/bin/env python3
"""
Tic Tac Toe GUI Game
A graphical 6x6 Tic Tac Toe game with pop-up window interface.
"""

import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("6x6 Tic Tac Toe")
        self.root.resizable(False, False)
        
        # Game state
        self.board = ['' for _ in range(36)]
        self.current_player = 'X'
        self.scores = {'X': 0, 'O': 0, 'Draw': 0}
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg='#2c3e50')
        title_frame.pack(fill='x', pady=10)
        
        title = tk.Label(title_frame, text="6x6 TIC TAC TOE", 
                        font=('Arial', 24, 'bold'), 
                        bg='#2c3e50', fg='white')
        title.pack()
        
        subtitle = tk.Label(title_frame, text="Get 4 in a row to win!", 
                           font=('Arial', 12), 
                           bg='#2c3e50', fg='#ecf0f1')
        subtitle.pack()
        
        # Score board
        score_frame = tk.Frame(self.root, bg='#ecf0f1')
        score_frame.pack(fill='x', pady=10)
        
        self.score_label = tk.Label(score_frame, 
                                    text=f"Player X: {self.scores['X']}  |  Draws: {self.scores['Draw']}  |  Player O: {self.scores['O']}", 
                                    font=('Arial', 14),
                                    bg='#ecf0f1', fg='#2c3e50')
        self.score_label.pack()
        
        # Current player indicator
        self.player_label = tk.Label(self.root, 
                                     text=f"Current Turn: Player X", 
                                     font=('Arial', 16, 'bold'),
                                     fg='#3498db')
        self.player_label.pack(pady=10)
        
        # Game board
        board_frame = tk.Frame(self.root, bg='#34495e')
        board_frame.pack(padx=30, pady=20)
        
        self.buttons = []
        for i in range(6):
            for j in range(6):
                index = i * 6 + j
                btn = tk.Button(board_frame, text='', 
                              font=('Arial', 20, 'bold'),
                              width=4, height=2,
                              bg='#ecf0f1',
                              activebackground='#bdc3c7',
                              command=lambda idx=index: self.make_move(idx))
                btn.grid(row=i, column=j, padx=2, pady=2)
                self.buttons.append(btn)
        
        # Control buttons
        control_frame = tk.Frame(self.root, bg='white')
        control_frame.pack(pady=10, padx=20, side='bottom')
        
        new_game_btn = tk.Button(control_frame, text='New Game', 
                                 font=('Arial', 12, 'bold'),
                                 bg='#3498db', fg='white',
                                 padx=20, pady=10,
                                 command=self.reset_game)
        new_game_btn.pack(side='left', padx=5)
        
        reset_scores_btn = tk.Button(control_frame, text='Reset Scores', 
                                     font=('Arial', 12, 'bold'),
                                     bg='#95a5a6', fg='white',
                                     padx=20, pady=10,
                                     command=self.reset_scores)
        reset_scores_btn.pack(side='left', padx=5)
        
    def make_move(self, index):
        if self.board[index] == '':
            self.board[index] = self.current_player
            
            # Update button
            color = '#3498db' if self.current_player == 'X' else '#e74c3c'
            self.buttons[index].config(text=self.current_player, 
                                      fg=color,
                                      state='disabled',
                                      disabledforeground=color)
            
            # Check for winner
            if self.check_winner(self.current_player):
                self.scores[self.current_player] += 1
                self.update_score_display()
                messagebox.showinfo("Game Over", f"🎉 Player {self.current_player} wins! 🎉")
                self.reset_game()
                return
            
            # Check for draw
            if '' not in self.board:
                self.scores['Draw'] += 1
                self.update_score_display()
                messagebox.showinfo("Game Over", "🤝 It's a draw! 🤝")
                self.reset_game()
                return
            
            # Switch player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            color = '#3498db' if self.current_player == 'X' else '#e74c3c'
            self.player_label.config(text=f"Current Turn: Player {self.current_player}",
                                    fg=color)
    
    def check_winner(self, player):
        # Check horizontal
        for row in range(6):
            for col in range(3):
                if all(self.board[row * 6 + col + i] == player for i in range(4)):
                    self.highlight_winning_line([(row * 6 + col + i) for i in range(4)])
                    return True
        
        # Check vertical
        for row in range(3):
            for col in range(6):
                if all(self.board[(row + i) * 6 + col] == player for i in range(4)):
                    self.highlight_winning_line([((row + i) * 6 + col) for i in range(4)])
                    return True
        
        # Check diagonal (top-left to bottom-right)
        for row in range(3):
            for col in range(3):
                if all(self.board[(row + i) * 6 + col + i] == player for i in range(4)):
                    self.highlight_winning_line([((row + i) * 6 + col + i) for i in range(4)])
                    return True
        
        # Check diagonal (top-right to bottom-left)
        for row in range(3):
            for col in range(3, 6):
                if all(self.board[(row + i) * 6 + col - i] == player for i in range(4)):
                    self.highlight_winning_line([((row + i) * 6 + col - i) for i in range(4)])
                    return True
        
        return False
    
    def highlight_winning_line(self, indices):
        for idx in indices:
            self.buttons[idx].config(bg='#2ecc71')
    
    def reset_game(self):
        self.board = ['' for _ in range(36)]
        self.current_player = 'X'
        
        for btn in self.buttons:
            btn.config(text='', state='normal', bg='#ecf0f1')
        
        self.player_label.config(text="Current Turn: Player X", fg='#3498db')
    
    def reset_scores(self):
        self.scores = {'X': 0, 'O': 0, 'Draw': 0}
        self.update_score_display()
        self.reset_game()
    
    def update_score_display(self):
        self.score_label.config(
            text=f"Player X: {self.scores['X']}  |  Draws: {self.scores['Draw']}  |  Player O: {self.scores['O']}"
        )

def main():
    root = tk.Tk()
    
    # Center the window on screen
    window_width = 580
    window_height = 850
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    app = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()