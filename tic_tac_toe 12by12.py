#!/usr/bin/env python3
"""
Tic Tac Toe Game
A simple command-line Tic Tac Toe game for two players.
"""

def print_board(board):
    """Print the current game board."""
    print("\n")
    for row in range(12):
        # Print row with proper spacing for 1, 2, or 3 digit numbers
        row_str = " | ".join(f"{board[row * 12 + col]:>3}" for col in range(12))
        print(row_str)
        if row < 11:
            print("-" * 59)
    print("\n")


def check_winner(board, player):
    """Check if the player has won (5 in a row)."""
    # Check horizontal
    for row in range(12):
        for col in range(8):  # 12 - 5 + 1 = 8
            if all(board[row * 12 + col + i] == player for i in range(5)):
                return True
    
    # Check vertical
    for row in range(8):  # 12 - 5 + 1 = 8
        for col in range(12):255


def is_board_full(board):
    """Check if the board is full (draw condition)."""
    return all(cell in ['X', 'O'] for cell in board)


def get_valid_move(board, player):
    """Get a valid move from the player."""
    while True:
        try:
            move = input(f"Player {player}, enter your move (1-144): ")
            move = int(move) - 1  # Convert to 0-indexed
            
            if move < 0 or move > 143:
                print("Invalid input! Please enter a number between 1 and 144.")
                continue
            
            if board[move] in ['X', 'O']:
                print("That spot is already taken! Choose another.")
                continue
            
            return move
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 144.")
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")
            exit()


def print_positions():
    """Show the position numbers for reference."""
    print("\nPosition numbers (1-144):")
    print("Top-left corner is 1, top-right is 12")
    print("Bottom-left is 133, bottom-right is 144")
    print("Example positions:")
    print("  1 |  2 |  3 | ... | 10 | 11 | 12")
    print(" 13 | 14 | 15 | ... | 22 | 23 | 24")
    print("...")
    print("133|134|135 | ... |142|143|144")
    print()


def play_game():
    """Main game loop."""
    # Initialize the board with position numbers (1-144)
    board = [str(i) for i in range(1, 145)]
    current_player = 'X'
    scores = {'X': 0, 'O': 0, 'Draw': 0}
    
    print("=" * 60)
    print("     WELCOME TO 12x12 TIC TAC TOE!")
    print("     (Get 5 in a row to win!)")
    print("=" * 60)
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
            board = [str(i) for i in range(1, 145)]
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
            board = [str(i) for i in range(1, 145)]
            current_player = 'X'
            continue
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
    
    print("\n" + "=" * 60)
    print("     FINAL SCORES")
    print("=" * 60)
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