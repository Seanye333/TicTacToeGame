#!/usr/bin/env python3
"""
Tic Tac Toe Game
A simple command-line Tic Tac Toe game for two players.
"""

def print_board(board):
    """Print the current game board."""
    print("\n")
    for row in range(6):
        # Print row with proper spacing for 1 or 2 digit numbers
        row_str = " | ".join(f"{board[row * 6 + col]:>2}" for col in range(6))
        print(row_str)
        if row < 5:
            print("-" * 29)
    print("\n")


def check_winner(board, player):
    """Check if the player has won (4 in a row)."""
    # Check horizontal
    for row in range(6):
        for col in range(3):  # 6 - 4 + 1 = 3
            if all(board[row * 6 + col + i] == player for i in range(4)):
                return True
    
    # Check vertical
    for row in range(3):  # 6 - 4 + 1 = 3
        for col in range(6):
            if all(board[(row + i) * 6 + col] == player for i in range(4)):
                return True
    
    # Check diagonal (top-left to bottom-right)
    for row in range(3):
        for col in range(3):
            if all(board[(row + i) * 6 + col + i] == player for i in range(4)):
                return True
    
    # Check diagonal (top-right to bottom-left)
    for row in range(3):
        for col in range(3, 6):
            if all(board[(row + i) * 6 + col - i] == player for i in range(4)):
                return True
    
    return False


def is_board_full(board):
    """Check if the board is full (draw condition)."""
    return all(cell in ['X', 'O'] for cell in board)


def get_valid_move(board, player):
    """Get a valid move from the player."""
    while True:
        try:
            move = input(f"Player {player}, enter your move (1-36): ")
            move = int(move) - 1  # Convert to 0-indexed
            
            if move < 0 or move > 35:
                print("Invalid input! Please enter a number between 1 and 36.")
                continue
            
            if board[move] in ['X', 'O']:
                print("That spot is already taken! Choose another.")
                continue
            
            return move
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 36.")
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")
            exit()


def print_positions():
    """Show the position numbers for reference."""
    print("\nPosition numbers (1-36):")
    print(" 1 |  2 |  3 |  4 |  5 |  6")
    print(" 7 |  8 |  9 | 10 | 11 | 12")
    print("13 | 14 | 15 | 16 | 17 | 18")
    print("19 | 20 | 21 | 22 | 23 | 24")
    print("25 | 26 | 27 | 28 | 29 | 30")
    print("31 | 32 | 33 | 34 | 35 | 36")
    print()


def play_game():
    """Main game loop."""
    # Initialize the board with position numbers (1-36)
    board = [str(i) for i in range(1, 37)]
    current_player = 'X'
    scores = {'X': 0, 'O': 0, 'Draw': 0}
    
    print("=" * 40)
    print("     WELCOME TO 6x6 TIC TAC TOE!")
    print("     (Get 4 in a row to win!)")
    print("=" * 40)
    print_positions()
    
    while True:
        print_board(board)
        
        # Get player move
        move = get_valid_move(board, current_player)
        board[move] = current_player
        
        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            scores[current_player] += 1
            print(f"\nScores - X: {scores['X']} | O: {scores['O']} | Draws: {scores['Draw']}")
            
            if not play_again():
                break
            board = [str(i) for i in range(1, 37)]
            current_player = 'X'
            continue
        
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("🤝 It's a draw! 🤝")
            scores['Draw'] += 1
            print(f"\nScores - X: {scores['X']} | O: {scores['O']} | Draws: {scores['Draw']}")
            
            if not play_again():
                break
            board = [str(i) for i in range(1, 37)]
            current_player = 'X'
            continue
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
    
    print("\n" + "=" * 40)
    print("     FINAL SCORES")
    print("=" * 40)
    print(f"Player X: {scores['X']}")
    print(f"Player O: {scores['O']}")
    print(f"Draws: {scores['Draw']}")
    print("\nThanks for playing! 👋")


def play_again():
    """Ask if players want to play again."""
    while True:
        response = input("\nPlay again? (y/n): ").lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'")


if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")