board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
win = False
winner = ''


def draw_board(board):
   print("-" * 9)
   print('|', board[0][0], board[0][1], board[0][2], '|')
   print('|', board[1][0], board[1][1], board[1][2], '|')
   print('|', board[2][0], board[2][1], board[2][2], '|')
   print("-" * 9)


def move_input(player_token):
    valid = False
    while not valid:
        x, y = input("Enter the coordinates: ").split()
        if x.isdigit() and y.isdigit():
            x = int(x) - 1
            y = int(y) - 1
            if not ((x >= 0 and x<= 2) and (y >= 0 and y<= 2)):
                print("Coordinates should be from 1 to 3!")
            else:
                if board[x][y] == ' ':
                    board[x][y] = player_token
                    draw_board(board)
                    valid = True
                else:
                    print('This cell is occupied! Choose another one!')
        else:
            print('You should enter numbers!')


def check_win(board):
    for i in range(0, 3):
        if board[i][0] != ' ' and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
        elif board[0][i] != ' ' and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
        if board[0][0] != ' ' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return board[0][0]
        elif board[0][2] != ' ' and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return board[0][2]
    return False


def main(board):
    counter = 0
    win = False
    draw_board(board)
    while not win:
        if counter % 2 == 0:
           move_input("X")
        else:
           move_input("O")
        counter += 1
        if counter > 4:
           temp = check_win(board)
           if temp:
              print(temp, "wins")
              win = True
              break
        if counter == 9:
            print("Draw")
            break


main(board)