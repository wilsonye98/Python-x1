import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def find_block_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                # Temporarily place "O" to check for winning moves for "X"
                board[i][j] = "X"
                if check_winner(board) == "X":
                    board[i][j] = "O"  # Block this move
                    return (i, j)
                board[i][j] = " "  # Reset the cell
    return None


def ai_move(board):
    # First, check if the AI needs to block the player's winning move
    block_move = find_block_move(board)
    if block_move:
        return block_move

    # If no block needed, choose a random empty cell
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells) if empty_cells else None


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Player 1 is "X"

    while True:
        print_board(board)

        if current_player == "X":
            print("Player X, choose your position (row and column): ")
            while True:
                try:
                    row, col = map(int, input().split())
                    if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
                        print("Invalid position. Try again.")
                        continue
                    break
                except ValueError:
                    print("Please enter valid row and column numbers.")
                    continue
        else:
            print("Player O (AI) is making a move...")
            row, col = ai_move(board)

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()