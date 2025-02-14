
# Connect 4 Project

import random

#Initializes the board
def initialize_board(m,n):
    board = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(0) 
        board.append(row)
    return board

#prints the board 
def render(board):
    m,n = size(board)
    for i in range(m):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
#checks up for win
def horizontal_check(board,i,k, player):
    row = get_row(board, i)
    h_win = connectk(row, k, player)
    return h_win
#checks across for win
def vertical_check(board,j,k,player):
    col = get_col(board, j)
    v_win = connectk(col, k, player)
    return v_win
#starts to put the disc in the board
def play_disc(board,j,player):
    for row in reversed(board):
        if row[j] == 0:
            row[j] = player
            return True
    return False
#grabs the coloumn
def get_col(board,j):
    lst = []
    m, n = size(board)
    for i in range(m):
        lst.append(board[i][j])
    return lst
#grabs the rows
def get_row(board,i):
    return board[i]
#gets the diagonals from the right
def get_negative_diagonal(board,y,x):
    lst = []
    m, n = size(board)
    for i in range(m):
        for j in range(n):
            if i - j == y - x:
                lst.append(board[i][j])
    return lst
#gets the diagonals from the left
def get_positive_diagonal(board, y, x):
    lst = []
    m, n = size(board)
    for i in range(m):
        for j in range(n):
            if i + j == y + x:
                lst.append(board[i][j])
    return lst

def size(board):
    m, n = len(board), len(board[0])
    return m, n
#checks if there are enough in a row for a win
def connectk(lst,k,player):
    total = 0
    for item in lst:
        if item == player:
            total += 1
            if total == k:
                return True
        else:
            total = 0
    return False
#rules for the game
def legal_move(board):
    moves = []
    m, n = size(board)
    for j in range(n):
        for i in range(m-1, -1, -1):
            if board[i][j] == 0:
                moves.append((i, j))
                break
    return moves

def user_turn(board, player):
    j=int(input("Pick a column 1-7: "))
    if not legal_move:
        print("Move is not legal")
    else:
        play_disc(board,j,player)

def diagonal_win(board,i,j,k,player):
    right_diagonal = get_negative_diagonal(board,i,j)
    left_diagonal = get_positive_diagonal(board,i,j)
    return connectk(right_diagonal,k,player) or connectk(left_diagonal,k,player)

def computer_turn(board,player):
    moves = legal_move(board)
    move = random.choice(moves)
    i, j = move
    play_disc(board, j, player)
    print(f"Computer picks column ")

#arguments for a win
def check_win(board, player, k):
    return any(horizontal_check(board, i, k, player) or vertical_check(board, j, k, player) or diagonal_win(board, i, j, k, player) for i in range(len(board)) for j in range(len(board[0])))

def main():
    board = initialize_board(6, 7)
    k = 4

    while True:
        I_rule = "F"
        render(board)
        user_turn(board, I_rule)
        if check_win(board, I_rule, k):
            render(board)
            print("You win!")
            break
        

        computer_lame = "X"
        computer_turn(board, computer_lame)
        if check_win(board, computer_lame, k):
            render(board)
            print("Computer wins!")
            break
        

if __name__ == '__main__':
    main()