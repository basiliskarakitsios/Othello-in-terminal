#Vasilis Karakitsios A.M. 3241


import time                                                 #time will be used in the main program 

BLACK = 1
WHITE = 2



def create_board():                                         #creating the starting list wich will be used for the main board
    STARTINGBOARD = [[0 for i in range(8)]for j in range(8)]
    STARTINGBOARD[3][3] = WHITE
    STARTINGBOARD[4][4] = WHITE
    STARTINGBOARD[3][4] = BLACK
    STARTINGBOARD[4][3] = BLACK 

    return STARTINGBOARD



def print_board(board):                                     #creating the way the board will look
    firstline = '\n   0   1   2   3   4   5   6   7\n'
    secondline = '----------------------------------\n0  '
    otherline = str()
    for i in range(len(board)):
        for j in range(len(board)):
            number = (str(board[i][j])+' | ')
            otherline += number
            if len(otherline) == 32:
                otherline = otherline+'\n1  '
            elif len(otherline) == 68:
                otherline = otherline+'\n2  '
            elif len(otherline) == 104:
                otherline = otherline+'\n3  '
            elif len(otherline) == 140:
                otherline = otherline+'\n4  '
            elif len(otherline) == 176:
                otherline = otherline+'\n5  '
            elif len(otherline) == 212:
                otherline = otherline+'\n6  '
            elif len(otherline) == 248:
                otherline = otherline+'\n7  '
            else:
                continue
    newboard = firstline+secondline+otherline
    print(newboard)
    print('----------------------------------')




def up(board,i,j,colour):                               #the following functions (up...downright) are checking if there's a valid move to the corresponding direction
    uplist = []
    
    if board[i][j] != 0 or i < 0 or i > 7 or j < 0 or j > 7:
        return uplist
    
    if colour == BLACK:
        othercolour = WHITE
    else:
        othercolour = BLACK

    newi = i - 1
    if 0 <= newi <= 7 and board[newi][j] == othercolour:
        newi -= 1
        if newi < 0:
            return uplist

        while board[newi][j] == othercolour:
            newi -= 1
            if newi < 0:
                return uplist

        if board[newi][j] == colour:
            while True:
                newi += 1
                if board[newi][j] == 0:   
                    break
                uplist.append([newi,j])
    
    return uplist




def down(board,i,j,colour):
    downlist = []
    
    if board[i][j] != 0 or i < 0 or i > 7 or j < 0 or j > 7:
        return downlist
    
    if colour == BLACK:
        othercolour = WHITE
    else:
        othercolour = BLACK

    newi = i + 1
    if 0 <= newi <= 7 and board[newi][j] == othercolour:
        newi += 1
        if newi > 7:
            return downlist

        while board[newi][j] == othercolour:
            newi += 1
            if newi > 7:
                return downlist

        if board[newi][j] == colour:
            while True:
                newi -= 1
                if board[newi][j] == 0:
                    break
                downlist.append([newi,j])
    
    return downlist




def left(board,i,j,colour):
    leftlist = []
    
    if board[i][j] != 0 or i < 0 or i > 7 or j < 0 or j > 7:
        return leftlist
    
    if colour == BLACK:
        othercolour = WHITE
    else:
        othercolour = BLACK
        
    newj = j - 1
    if 0 <= newj <= 7 and board[i][newj] == othercolour:
        newj -= 1
        if newj < 0:
            return leftlist
        
        while board[i][newj] == othercolour:
            newj -= 1
            if newj < 0:
                return leftlist
            
        if board[i][newj] == colour:
            while True:
                newj += 1
                if board[i][newj] == 0:
                    break
                leftlist.append([i,newj])

    return leftlist




def right(board,i,j,colour):
    rightlist = []
    
    if board[i][j] != 0 or i < 0 or i > 7 or j < 0 or j > 7:
        return rightlist
    
    if colour == BLACK:
        othercolour = WHITE
    else:
        othercolour = BLACK
        
    newj = j + 1
    if 0 <= newj <= 7 and board[i][newj] == othercolour:
        newj += 1
        if newj > 7:
            return rightlist
        
        while board[i][newj] == othercolour:
            newj += 1
            if newj > 7:
                return rightlist
            
        if board[i][newj] == colour:
            while True:
                newj -= 1
                if board[i][newj] == 0:
                    break
                rightlist.append([i,newj])

    return rightlist




def upleft(board,i,j,colour):
    upleftlist = []
        
    if board[i][j] != 0 or i < 0 or i > 7 or j < 0 or j > 7:
        return upleftlist

    if colour == BLACK:
        othercolour = WHITE
    else:
        othercolour = BLACK
        
    newi = i - 1
    newj = j - 1
    if 0 <= newj <= 7 and 0 <= newi <= 7 and board[newi][newj] == othercolour:
        newi -= 1
        newj -= 1
        if newi < 0 or newj < 0:
            return upleftlist
        
        while board[newi][newj] == othercolour:
            newi -= 1
            newj -= 1
            if newi < 0 or newj < 0:
                return upleftlist

        if board[newi][newj] == colour:
            while True:
                newi += 1
                newj += 1
                if board[newi][newj] == 0:
                    break
                upleftlist.append([newi,newj])

    return upleftlist




def upright(board,i,j,colour):
    uprightlist = []
    
    if board[i][j] != 0 or i < 0 or i > 7 or j < 0 or j > 7:
        return uprightlist
    
    if colour == BLACK:
        othercolour = WHITE
    else:
        othercolour = BLACK
        
    newi = i - 1
    newj = j + 1
    if 0 <= newj <= 7 and 0 <= newi <= 7 and board[newi][newj] == othercolour:
        newi -= 1
        newj += 1
        if newi < 0 or newj > 7:
            return uprightlist
        
        while board[newi][newj] == othercolour:
            newi -= 1
            newj += 1
            if newi < 0 or newj > 7:
                return uprightlist

        if board[newi][newj] == colour:
            while True:
                newi += 1
                newj -= 1
                if board[newi][newj] == 0:
                    break
                uprightlist.append([newi,newj])

    return uprightlist




def downleft(board,i,j,colour):
    downleftlist = []
    
    if board[i][j] != 0 or i < 0 or i > 7 or j < 0 or j > 7:
        return downleftlist
    
    if colour == BLACK:
        othercolour = WHITE
    else:
        othercolour = BLACK
        
    newi = i + 1
    newj = j - 1
    if 0 <= newj <= 7 and 0 <= newi <= 7 and board[newi][newj] == othercolour:
        newi += 1
        newj -= 1
        if newi > 7 or newj < 0:
            return downleftlist
        
        while board[newi][newj] == othercolour:
            newi += 1
            newj -= 1
            if newi > 7 or newj < 0:
                return downleftlist

        if board[newi][newj] == colour:
            while True:
                newi -= 1
                newj += 1
                if board[newi][newj] == 0:
                    break
                downleftlist.append([newi,newj])

    return downleftlist




def downright(board,i,j,colour):
    downrightlist = []
    
    if board[i][j] != 0 or i < 0 or i > 7 or j < 0 or j > 7:
        return downrightlist
    
    if colour == BLACK:
        othercolour = WHITE
    else:
        othercolour = BLACK
        
    newi = i + 1
    newj = j + 1
    if 0 <= newj <= 7 and 0 <= newi <= 7 and board[newi][newj] == othercolour:
        newi += 1
        newj += 1
        if newi > 7 or newj > 7:
            return downrightlist
        
        while board[newi][newj] == othercolour:
            newi += 1
            newj += 1
            if newi > 7 or newj > 7:
                return downrightlist
            
        if board[newi][newj] == colour:
            while True:
                newi -= 1
                newj -= 1
                if board[newi][newj] == 0:
                    break
                downrightlist.append([newi,newj])

    return downrightlist

        



def reverse_count(board,i,j,colour):                    #this function adds the number of reverses an added checker to a block will cause
    sumreverses = 0
    
    if board[i][j] != 0:
        return sumreverses

    sumreverses += len(up(board,i,j,colour))
    sumreverses += len(down(board,i,j,colour))
    sumreverses += len(left(board,i,j,colour))
    sumreverses += len(right(board,i,j,colour))
    sumreverses += len(upleft(board,i,j,colour))
    sumreverses += len(upright(board,i,j,colour))
    sumreverses += len(downleft(board,i,j,colour))
    sumreverses += len(downright(board,i,j,colour))
    return sumreverses



def compute_counts(board,colour):                       #this function returns a list with all the possible reverses that can happen
    compute_counts_list = [[0 for i in range(8)]for j in range(8)]
    for i in range(8):
        for j in range(8):
            compute_counts_list[i][j] = reverse_count(board,i,j,colour)

    return compute_counts_list




def add_checker(board,i,j,colour):                      #this function adds a checker to the board
    upvar = up(board,i,j,colour)
    downvar = down(board,i,j,colour)
    leftvar = left(board,i,j,colour)
    rightvar = right(board,i,j,colour)
    upleftvar = upleft(board,i,j,colour)
    uprightvar = upright(board,i,j,colour)
    downleftvar = downleft(board,i,j,colour)
    downrightvar = downright(board,i,j,colour)
    if upvar:
        for flippedi,flippedj in upvar:
            board[flippedi][flippedj] = colour
    if downvar:
        for flippedi,flippedj in downvar:
            board[flippedi][flippedj] = colour
    if leftvar:
        for flippedi,flippedj in leftvar:
            board[flippedi][flippedj] = colour
    if rightvar:
        for flippedi,flippedj in rightvar:
            board[flippedi][flippedj] = colour
    if upleftvar:
        for flippedi,flippedj in upleftvar:
            board[flippedi][flippedj] = colour
    if uprightvar:
        for flippedi,flippedj in uprightvar:
            board[flippedi][flippedj] = colour
    if downleftvar:
        for flippedi,flippedj in downleftvar:
            board[flippedi][flippedj] = colour
    if downrightvar:
        for flippedi,flippedj in downrightvar:
            board[flippedi][flippedj] = colour

    if upvar or downvar or leftvar or rightvar or upleftvar or uprightvar or downleftvar or downrightvar: 
        board[i][j] = colour

    print_board(board)




def human_play(board,colour):                       #this function checks if there's a possible move for a user and lets him play
    available_moves = 0
    available_moves_list = compute_counts(board,colour)
    for i in range(8):
        for j in range(8):
            if available_moves_list[i][j] > 0:
                available_moves = available_moves_list[i][j]
                
    if available_moves > 0:
        while True:
            try:
                mymovei = int(input('Please give row number : '))
                mymovej = int(input('Please give column number : '))
                while mymovei == '' or mymovej == ''  or mymovei < 0 or mymovei > 7 or mymovej < 0 or mymovej > 7:
                    mymovei = int(input('Please give row number : '))
                    mymovej = int(input('Please give column number : '))  
            except ValueError:
                print('Invalid Input. Please try again.')
            else:
                break
        number_of_reverses = reverse_count(board,mymovei,mymovej,colour)

        while number_of_reverses == 0 or mymovei < 0 or mymovei > 7 or mymovej < 0 or mymovej > 7:
            while True:
                try:
                    mymovei = int(input('Please give row number : '))
                    mymovej = int(input('Please give column number : '))
                    while mymovei == '' or mymovej == '' or mymovei < 0 or mymovei > 7 or mymovej < 0 or mymovej > 7:
                        mymovei = int(input('Please give row number : '))
                        mymovej = int(input('Please give column number : '))  
                except ValueError:
                    print('Invalid Input. Please try again.')
                else:
                    break
            number_of_reverses = reverse_count(board,mymovei,mymovej,colour)
        add_checker(board,mymovei,mymovej,colour)
    return available_moves




def computer_play(board):                           #this function checks if there's a possible move for the computer and lets it play
    colour = WHITE
    compute_list = compute_counts(board,colour)
    maximum = 0
    available_moves = 0
    available_moves_list = compute_counts(board,colour)
    for i in range(8):
        for j in range(8):
            if available_moves_list[i][j] > 0:
                available_moves = available_moves_list[i][j]
                
    if available_moves > 0:
        for x in range(len(compute_list)):
            for y in range(len(compute_list)):
                if compute_list[x][y] > maximum:
                    maximum = compute_list[x][y]
                    i = x
                    j = y
        print('Computer Played\nRow:', i , 'Column:', j)
        add_checker(startingboardf,i,j,WHITE)
                    
    return available_moves
        



def print_score(board):                     #this function prints the score
    blackscore = 0
    whitescore = 0
    for i in range(len(board)):
        for j in range(len(board)):
            while board[i][j] == BLACK:
                blackscore += 1
                break
            while board[i][j] == WHITE:
                whitescore += 1
                break
    print('\nBLACKS : ',blackscore, 'WHITES : ', whitescore)
    print()
    return [blackscore,whitescore]


    



print()
print()
print()
print('*********************************************************************************************')
print('*   OOOOOOO    TTTTTTTTTTT  HHH     HHH  EEEEEEEEEEE  LLL          LLL            OOOOOOO   *')
print('*  OOOOOOOOO   TTTTTTTTTTT  HHH     HHH  EEEEEEEEEEE  LLL          LLL           OOOOOOOOO  *')
print('* OOO     OOO      TTT      HHH     HHH  EEE          LLL          LLL          OOO     OOO *')
print('* OOO     OOO      TTT      HHHHHHHHHHH  EEEEEE       LLL          LLL          OOO     OOO *')
print('* OOO     OOO      TTT      HHHHHHHHHHH  EEEEEE       LLL          LLL          OOO     OOO *')
print('* OOO     OOO      TTT      HHH     HHH  EEE          LLL          LLL          OOO     OOO *')
print('*  OOOOOOOOO       TTT      HHH     HHH  EEEEEEEEEEE  LLLLLLLLLLL  LLLLLLLLLLL   OOOOOOOOO  *')
print('*   OOOOOOO        TTT      HHH     HHH  EEEEEEEEEEE  LLLLLLLLLLL  LLLLLLLLLLL    OOOOOOO   *')
print('*********************************************************************************************')
print()
print()
print()

    
startingboardf = create_board()



while True:
    try:
        game_mode = int(input('Type 1 for singleplayer mode or 2 for multiplayer mode : '))
        while game_mode > 2 or game_mode < 1:
            game_mode = int(input('Type 1 for singleplayer mode or 2 for multiplayer mode : '))
    except ValueError:
        print('Invalid input. Please try again.')
    else:
        break

    
if game_mode == 1:
    print_board(startingboardf)
    scores_list = print_score(startingboardf)
    print()
    print('Black checkers = \'1\', White checkers = \'2\'')
    print()
    print('Player 1 (black checkers) turn ')
    print()
    while True:
        try:
            human_available_moves_player_1 = human_play(startingboardf,BLACK)
            scores_list = print_score(startingboardf)
            print()
                
                
        except ValueError and IndexError:
            print('Invalid input. Please try again')
        else:
            break
    print('Computer\'s (white checkers) turn ')
    print()
    time.sleep(1)                       #time is used to simulate the thought of the computer before it makes a move
    computer_available_moves = computer_play(startingboardf)
    scores_list = print_score(startingboardf)
    print()
    while True:
        if human_available_moves_player_1 > 0: 
            try:
                print('Player 1 (black checkers) turn ')
                print()
                human_available_moves_player_1 = human_play(startingboardf,BLACK)
                scores_list = print_score(startingboardf)
                print()
            except ValueError and IndexError:
                print('Invalid input. Please try again.')
        if computer_available_moves > 0:
                print('Computer\'s (white checkers) turn ')
                print()
                time.sleep(1)
                computer_available_moves = computer_play(startingboardf)
                scores_list = print_score(startingboardf)
                print()
        if human_available_moves_player_1 == 0 and computer_available_moves == 0:
            if scores_list[0] > scores_list[1]:
                print('Player 1 (black checkers) wins!')
            elif scores_list[0] < scores_list[1]:
                print('Computer (white checkers) wins!')
            elif scores_list[0] == scores_list[1]:
                print('It\'s a draw!')
            print('GAME OVER')
            break
            
    



elif game_mode == 2:
    print_board(startingboardf)
    scores_list = print_score(startingboardf)
    print()
    print('Black checkers = \'1\', White checkers = \'2\'')
    print()
    print('Player 1 (black checkers) turn ')
    print()
    while True:
        try:
            human_available_moves_player_1 = human_play(startingboardf,BLACK)
            scores_list = print_score(startingboardf)
            print()
        except ValueError and IndexError:
            print('Invalid input. Please try again')
        else:
            break
    print()
    print('Player 2 (white checkers) turn ')
    print()
    while True:
        try:
            human_available_moves_player_2 = human_play(startingboardf,WHITE)
            scores_list = print_score(startingboardf)
            print()
        except ValueError and IndexError:
            print('Invalid input. Please try again')
        else:
            break
    print()
    while True:
        if human_available_moves_player_1 > 0: 
            try:
                print('Player 1 (black checkers) turn ')
                print()
                human_available_moves_player_1 = human_play(startingboardf,BLACK)
                scores_list = print_score(startingboardf)
                print()
            except ValueError and IndexError:
                print('Invalid input. Please try again.')


        if human_available_moves_player_2 > 0: 
            try:
                print('Player 2 (white checkers) turn ')
                print()
                human_available_moves_player_2 = human_play(startingboardf,WHITE)
                scores_list = print_score(startingboardf)
                print()
            except ValueError and IndexError:
                print('Invalid input. Please try again.')

        elif human_available_moves_player_1 == 0 and human_available_moves_player_2 == 0:
            if scores_list[0] > scores_list[1]:
                print('Player 1 (black checkers) wins!')
            elif scores_list[0] < scores_list[1]:
                print('Player 2 (white checkers) wins!')
            elif scores_list[0] == scores_list[1]:
                print('It\'s a draw!')
            print('GAME OVER')
            break
