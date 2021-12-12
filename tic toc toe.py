def place_marker(gamelist,marker,position):
    gamelist[(position-1)]=marker
def replay():
    choice= 'wrong'
    while choice not in ['Y','N']:
        choice= input("Do you want to play again? Type 'Y' for yes 'N' for no: ")
        if choice not in ['Y','N']:
            print("Sorry, I couldn't understand. Type 'Y' or 'N': ")
    if choice=='Y':
        return True
    elif choice== 'N':
        return False


def display_game(board):
    for i in range(0,9):
        print(f"|{board[i]}|",end=' ')
        if (i+1)%3==0:
            print("\n-----------")



def user_input():
    choice='wrong'
    while choice not in['X','O']:
        choice=input("enter your input as X or O: ")
        if choice not in['X','O']:
            print("\n"*100)
            print("Please enter either X or O")

def win_check(board,mark):
    for i in range(0,9):
        if board[i]==mark:
            if i in[0,1,2] and board[i+3]==mark and board[i+6]==mark:
                return True
            elif i in [0,3,6] and board[i+1]==mark and board[i+2]==mark:
                return True
            elif i in [0,2]:
                if i==0 and board[4]==mark and board[9]==mark:
                    return True
                else:
                    if board[4]==mark and board[6]==mark:
                        return True
            else:
                return False
        else:
            return False

def choosefirst():
    import random
    i = random.randint(1,2)
    return i
def space_check(board,position):
    if board[position-1]==' ':
        return True
    else:
        return False

def full_board_check(board):
    temp=0
    for i in range(len(board)):
        if board[i]==' ':
            temp+=1
    if temp==0:
        return True
    else:
        return False
def player_choice(board):
    choice = 0
    while choice not in range(1,10):
        choice= int(input("choose the desired position: "))
        if choice not in range(1,10):
            print("Please enter a no. between 1 to 9")
        elif space_check(board,choice)==False:
            print("The position is filled, please enter another position")
            continue
    return choice
if __name__=='__main__':
    print('Tic Tac Toe')

    while True:
        player1_marker, player2_marker = input("entr the marker")
        play_game = input('Are you ready to play? Enter Yes or No.')

        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False
        test_board = [' ']*9
        turn = choosefirst()
        print(f"Player {1} will play first")
        while game_on:
            if turn==1:
                display_game(test_board)
                position = player_choice(test_board)
                place_marker(test_board,player1_marker,position)
                if win_check(test_board,player1_marker):
                    display_game(test_board)
                    print('Congratulation Player1 has won')
                    game_on=False
                else:
                    if full_board_check(test_board):
                        display_game(test_board)
                        print('Its a draw!!!')
                        break
                    else:
                        turn=2
            else:
                display_game(test_board)
                position = player_choice(test_board)
                place_marker(test_board,player2_marker,position)
                if win_check(test_board,player2_marker):
                        display_game(test_board)
                        print('Congratulation Player2 has won')
                        game_on=False
                elif full_board_check(test_board):
                    display_game(test_board)
                    print('Its a draw!!!')
                    break
                else:
                    turn=1
        if not replay():
            break






