N = 9

board = [
    [0,0,0,0,0,0,5,6,0],
    [0,0,0,0,8,0,0,4,0],
    [0,0,3,2,0,0,0,0,7],
    [0,0,0,1,0,0,0,0,0],
    [0,6,4,0,0,0,2,1,0],
    [0,0,0,0,7,0,0,8,0],
    [0,7,0,0,0,5,0,0,0],
    [0,0,0,0,2,6,8,0,0],
    [0,5,0,0,0,0,4,0,3]
]

def solve(board, row, col):

    if (row == N - 1 and col == N):
        return True

    if col == N:
        row += 1
        col = 0

    if board[row][col] > 0:
        return solve(board, row, col + 1)
    for num in range(1, N + 1, 1):

        if valid(board, num, row, col):
            board[row][col] = num

            if solve(board, row, col + 1):
                return True

        board[row][col] = 0

    return False    


def valid(board, number, row, col):
    # check row
    for i in range(len(board[0])):
        if board[row][i] == number:
            return False

    # check column
    for i in range(len(board)):
        if board[i][col] == number:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == number:
                return False

    # check box
    ''' box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_x * 3 + 3):
        for j in range(box_x * 3, box_y * 3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False '''

    return True


def print_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('------------------------')

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, column

    return None


if __name__ == '__main__':
    print_board(board)
    solve(board, 0, 0)
    print('\n')
    print('\n')
    print_board(board)
                