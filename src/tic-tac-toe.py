def check_win(board):
    """
    Check if somebody wins.
    Return winning symbol or None in case of a tie.
    """
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2]:
            return board[r][0]

    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

# Initialize an empty board
board = [[' ' for _ in range(3)] for _ in range(3)]

# User input for the board
for r in range(3):
    line = input("Enter row {}: ".format(r))
    board[r] = line.upper().split()

# Check for a win or tie
result = check_win(board)

if result is None:
    print("It's a Tie!")
elif result == 'X':
    print('Anjali Wins!')
elif result == 'O':
    print('Abhinav Wins!')
