#!/usr/bin/env python

# Tic tac toe 2 player game
# CLI based script

def drawBoard(board):
    # This function prints out the board that it was passed
    i = 1
    op = ''
    for u in range(1, N):
        op = op + '      |'
    print(op)
    for x in range(1, N+1):
        start = 1
        st = ''
        while start <= N:
              val = board[i]
              if val == None:
                 val = i
              st = st + str(val)
              if start != N:
                 sp = 5
                 if len(str(val)) > 1:
                    sp = sp - len(str(val)) + 1
                 for u in range(1, sp+1):
                     st = st + ' '
                 st = st + '|'
              i = i + 1
              start  = start + 1
        print(st)
        if x != N:
           print(op)
           op1 = ''
           for u in range(1, (N*N) + (14-N)):
               op1 = op1 + '-'
           print(op1)
    print(op)
    print(op)

def getPlayerMove(player, board):
    # Let the player type in their move
    move = ' '
    while move not in range(1, (N * N)+ 1) or not isSpaceFree(board, int(move)):
         print(playName[player]+', choose a box to put '+playLetter[player]+' into:')
         move = raw_input()
         try:
             move = int(move)
         except:
                pass
    return move

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board
    return board[move] == None

def makeMove(board, letter, move):
    board[move] = letter

def isBoardFull(board):
    # Return True if every space on the board has been taken, Otherwise return False
    for i in range(1, (N * N)+ 1):
        if isSpaceFree(board, i):
            return False
    return True

def isWinner(board, letter):
    # Given a board and a player's letter, this function returns True if that player has won
    if checkAcross(board, letter) is True:
       return True
    elif checkDown(board, letter) is True:
         return True
    elif checkLeftDiagonal(board, letter) is True:
         return True
    elif checkRightDiagonal(board, letter) is True:
         return True
    return False

def checkAcross(board, letter):
    # check all rows for win
    z = 1
    for x in range(1, N+1):
        start = 1
        found = 0
        while start <= N:
              if board[z] == letter:
                 found = found + 1
              else:
                   found = 0
              z = z + 1
              start = start + 1
              if found == Win:
                 return True
    return False

def checkDown(board, letter):
    # check all colums for win
    for x in range(1, N+1):
        start = 1
        z = x
        found = 0
        while start <= N:
              if board[z] == letter:
                 found = found + 1
              else:
                   found = 0
              z = z + N
              start = start + 1
              if found == Win:
                 return True
    return False    

def checkLeftDiagonal(board, letter):
    # check all left side diagonals for win
    z = 1
    d = (N - 2) * 2
    row = 1
    it = 0
    for t in range(1, d+1):
        start = 1
        found = 0
        while start <= N:
              try:
                  board[z]
              except:
                     break
              if board[z] == letter:
                 found = found + 1
              else:
                   found = 0
              z = z + (N + 1)
              start = start + 1
              if found == Win:
                 return True
        z = z + 1
        it = it + 1
        if it == (N - 2):
           row = row + 1
           it = 0
           z = (N * (row-1)) + 1
    return False

def checkRightDiagonal(board, letter):
    # check all right side diagonals for win
    z = N
    d = (N - 2) * 2
    row = 1
    it = 0
    for t in range(1, d+1):
        start = 1
        found = 0
        while start <= N:
              try:
                  board[z]
              except:
                     break
              if board[z] == letter:
                 found = found + 1
              else:
                   found = 0
              z = z + (N - 1)
              start = start + 1
              if found == Win:
                 return True
        z = z - 1
        it = it + 1
        if it == (N - 2):
           row = row + 1
           it = 0
           z = (N * row)
    return False


if __name__ == '__main__':        
   print('Welcome to Tic Tac Toe!')
   N = ''
   while not (type(N) == int) or N <= 2:
        print('Please enter N for game dimention NXN greater than 2')
        N = raw_input()
        try:
            N = int(N)
        except:
               pass

   board = [None] * (N * N + 1)
   Win = 3
   player1 = ''
   while player1 is '':
         print('Enter name for player 1:')
         player1 = raw_input()

   player2 = ''
   while player2 is '' or player2 == player1:
         print('Enter name for player 2:')
         player2 = raw_input()

   playName = [player1, player2]
   playLetter = ['X', 'O']
   turn = 0
   while True:
        drawBoard(board)
        move = getPlayerMove(turn, board)
        makeMove(board, playLetter[turn], move)
        if isWinner(board, playLetter[turn]):
           drawBoard(board)
           print('Congratulations '+playName[turn] +'! You have won')
           break
        elif isBoardFull(board):
             drawBoard(board)
             print('The game is a tie!')
             break
        else:
             turn = 1 if turn == 0 else 0
