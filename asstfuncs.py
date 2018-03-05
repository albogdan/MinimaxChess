class tree:
    def __init__(self,x):
        self.store = [x,[]]

    def AddSuccessor(self,x):
        self.store[1] = self.store[1] + [x]
        return True

    def Get_LevelOrder(self):
        finlist = []
        q = queue()
        q.push(self.store)
        while(q.size() != 0):
            node = q.pop()
            finlist.append(node[0])
            for i in node[1]:
                q.push(i.store)
        return finlist
    

class queue:
    def __init__(self):
        self.store = []


    def push(self, val):
        self.store = self.store + [val]
        return True

    def pop(self):
        if(len(self.store) == 0):
            return False
        rval = self.store[0]
        self.store = self.store[1:len(self.store)]
        return rval

    def size(self):
        return len(self.store)
    


def pBoard(board):
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   print(accum)


def checkPawn(board, position, player):
    legalList = []
    #check white pawn
    if(player == 2):
        if(position-8 > -1):
            if(board[position-8] == 0):
                legalList.append(position-8)
        if(position-7 > -1):
            if(board[position-7]//10 == 1):
                if(((position-7)%8) == position%8 + 1):
                    legalList.append(position-7)
        if(position-9 > -1):
            if(board[position-9]//10 == 1):
                if(((position-9)%8) == position%8-1):
                    legalList.append(position-9)
                
    #check black pawn
    if(player == 1):
        if(position+8 < 64):
            if(board[position+8] == 0):
                legalList.append(position+8)
        if(position +7 < 64):
            if(board[position+7]//10 == 2):
                if(((position+7)%8) == position%8-1):
                    legalList.append(position+7)
        if(position+9 < 64):
            if(board[position+9]//10 == 2):
                if(((position+9)%8) ==position%8+1):
                    legalList.append(position+9)
    return legalList

def checkKnight(board, position, player):
    legalList = []
    #check for white knight
    if(player == 1):
        locations = [6,10,15,17]
        for i in (locations):
            if(position+i <64):
                if((((position+i)%8) == (position%8+2)) or (((position+i)%8) == (position%8-2))):
                    if(board[position+i]//10==2 or board[position+i]==0):
                        legalList.append(position+i)
                elif((((position+i)%8) == (position%8+1)) or (((position+i)%8) == (position%8-1))):
                    if(board[position+i]//10==2 or board[position+i]==0):
                        legalList.append(position+i)
        locations = [-6,-10,-15,-17]
        for i in (locations):
            if(position+i >-1):
                if((((position+i)%8) == (position%8+2)) or (((position+i)%8) == (position%8-2))):
                    if(board[position+i]//10==2 or board[position+i]==0):
                        legalList.append(position+i)
                elif((((position+i)%8) == (position%8+1)) or (((position+i)%8) == (position%8-1))):
                    if(board[position+i]//10==2 or board[position+i]==0):
                        legalList.append(position+i)

    #check for black knight
    if(player == 2):
        locations = [6,10,15,17]
        for i in (locations):
            if(position+i <64):
                if((((position+i)%8) == (position%8+2)) or (((position+i)%8) == (position%8-2))):
                    if(board[position+i]//10==1 or board[position+i] ==0):
                        legalList.append(position+i)
                elif((((position+i)%8) == (position%8+1)) or (((position+i)%8) == (position%8-1))):
                    if(board[position+i]//10==1 or board[position+i] ==0):
                        legalList.append(position+i)
        locations = [-6,-10,-15,-17]
        for i in (locations):
            if(position+i >-1):
                if((((position+i)%8) == (position%8+2)) or (((position+i)%8) == (position%8-2))):
                    if(board[position+i]//10==1 or board[position+i] ==0):
                        legalList.append(position+i)
                elif((((position+i)%8) == (position%8+1)) or (((position+i)%8) == (position%8-1))):
                    if(board[position+i]//10==1 or board[position+i] ==0):
                        legalList.append(position+i)

    return legalList

def checkQueen(board, position, player):
    legalList = []
    #checking for white queen
    if(player == 1):
        tempBoard = list(board)
        tempBoard[position] = 12
        legalList += checkBishop(tempBoard, position, player)
        tempBoard[position] = 13
        legalList += checkRook(tempBoard, position, player)

    #checking for black queen
    if(player == 2):
        tempBoard = list(board)
        tempBoard[position] = 22
        legalList += checkBishop(tempBoard, position, player)
        tempBoard[position] = 23
        legalList += checkRook(tempBoard, position, player)

    return legalList

def checkRook(board, position, player):
    row = position//8
    column = position%8
    legalList = []
    #check white rook
    if(player == 1):
        #check horizontally
        for i in range(position-1,8*row-1,-1):
            if(board[i] == 0):
                legalList.append(i)
            elif(board[i]//10 == 2):
                legalList.append(i)
                break
            else:
                break
        for i in range(position+1, 8*(row+1)):
            if(board[i] == 0):
                legalList.append(i)
            elif(board[i]//10 == 2):
                legalList.append(i)
                break
            else:
                break

        #check vertically
        for i in range(position-8,column-8, -8):
            if(board[i] == 0):
                legalList.append(i)
            elif(board[i]//10 == 2):
                legalList.append(i)
                break
            else:
                break
        for i in range(position+8,row+57,8):
            if(board[i] == 0):
                legalList.append(i)
            elif(board[i]//10 == 2):
                legalList.append(i)
                break
            else:
                break
            
    #checking for black rook
    if(player == 2):
        #check horizontally
        for i in range(position-1,8*row-1,-1):
            if(board[i] == 0):
                legalList.append(i)
            elif(board[i]//10 == 1):
                legalList.append(i)
                break
            else:
                break
        for i in range(position+1, 8*(row+1)):
            if(board[i] == 0):
                legalList.append(i)
            elif(board[i]//10 == 1):
                legalList.append(i)
                break
            else:
                break

        #check vertically
        for i in range(position-8,column-8, -8):
            if(board[i] == 0):
                legalList.append(i)
            elif(board[i]//10 == 1):
                legalList.append(i)
                break
            else:
                break
        for i in range(position+8,row+57,8):
            if(board[i] == 0):
                legalList.append(i)
            elif(board[i]//10 == 1):
                legalList.append(i)
                break
            else:
                break

    return legalList

def checkBishop(board, position, player):
    legalList = []
    row = position//8
    column = position%8

    #check white bishop    
    if(player == 1):
        #y=-x from player down
        maxDist = min(7-column,7-row)
        for i, j in zip(range(row+1, row+maxDist+1), range(column+1, column+maxDist+1)):
            #if its an empty spot, add to the list, continue
            if(board[i*8 + j] == 0):
                legalList.append(i*8+j)
                continue
            #if its the same player, break
            elif(board[i*8+j]//10 == 1):
                break
            #if its the other player, add to the list and break
            elif(board[i*8+j]//10 == 2):
                legalList.append(i*8+j)
                break
                    

        #y=x from player down
        maxDist = min(column,7-row)
        for i,j in zip(range(row+1, row+maxDist+1), range(column-1, column-maxDist-1, -1)):
            #if its an empty spot, add to the list, continue
            if(board[i*8 + j] == 0):
                legalList.append(i*8+j)
                continue
            #if its the same player, break
            elif(board[i*8+j]//10 == 1):
                break
            #if its the other player, add to the list and break
            elif(board[i*8+j]//10 == 2):
                legalList.append(i*8+j)
                break
                
        #y=-x from player up
        maxDist = min(column,row)
        for i,j in zip(range(row-1, row-maxDist-1, -1), range(column-1, column-maxDist-1, -1)):
            #if its an empty spot, add to the list, continue
            if(board[i*8 + j] == 0):
                legalList.append(i*8+j)
                continue
            #if its the same player, break
            elif(board[i*8+j]//10 == 1):
                break
            #if its the other player, add to the list and break
            elif(board[i*8+j]//10 == 2):
                legalList.append(i*8+j)
                break
                    
        #y=x from player up
        maxDist = min(7-column, row)
        for i,j in zip(range(row-1, row-maxDist-1, -1), range(column+1, column+maxDist+1)):
            #if its an empty spot, add to the list, continue
            if(board[i*8 + j] == 0):
                legalList.append(i*8+j)
                continue
            #if its the same player, break
            elif(board[i*8+j]//10 == 1):
                break
            #if its the other player, add to the list and break
            elif(board[i*8+j]//10 == 2):
                legalList.append(i*8+j)
                break


    #check black bishop           
    if(player == 2):
        #y=-x from player down
        maxDist = min(7-column,7-row)
        for i, j in zip(range(row+1, row+maxDist+1), range(column+1, column+maxDist+1)):
            #if its an empty spot, add to the list, continue
            if(board[i*8 + j] == 0):
                legalList.append(i*8+j)
                continue
            #if its the same player, break
            elif(board[i*8+j]//10 == 2):
                break
            #if its the other player, add to the list and break
            elif(board[i*8+j]//10 == 1):
                legalList.append(i*8+j)
                break
                

        #y=x from player down
        maxDist = min(column,7-row)
        for i,j in zip(range(row+1, row+maxDist+1), range(column-1, column-maxDist-1, -1)):
            #if its an empty spot, add to the list, continue
            if(board[i*8 + j] == 0):
                legalList.append(i*8+j)
                continue
            #if its the same player, break
            elif(board[i*8+j]//10 == 2):
                break
            #if its the other player, add to the list and break
            elif(board[i*8+j]//10 == 1):
                legalList.append(i*8+j)
                break
                    
        #y=-x from player up
        maxDist = min(column,row)
        for i,j in zip(range(row-1, row-maxDist-1, -1), range(column-1, column-maxDist-1, -1)):
            #if its an empty spot, add to the list, continue
            if(board[i*8 + j] == 0):
                legalList.append(i*8+j)
                continue
            #if its the same player, break
            elif(board[i*8+j]//10 == 2):
                break
            #if its the other player, add to the list and break
            elif(board[i*8+j]//10 == 1):
                legalList.append(i*8+j)
                break
                    
        #y=x from player up
        maxDist = min(7-column, row)
        for i,j in zip(range(row-1, row-maxDist-1, -1), range(column+1, column+maxDist+1)):
            #if its an empty spot, add to the list, continue
            if(board[i*8 + j] == 0):
                legalList.append(i*8+j)
                continue
            #if its the same player, break
            elif(board[i*8+j]//10 == 2):
                break
            #if its the other player, add to the list and break
            elif(board[i*8+j]//10 == 1):
                legalList.append(i*8+j)
                break

    return legalList

def checkKing(board, position, player):
    legalList = []
    #checking for white king
    if(player == 1):
        locations = [-9,-8,-7,-1]
        for i in (locations):
            if(position+i >-1):
                if((((position+i)%8) == (position%8+1)) or (((position+i)%8) == (position%8-1)) or ((position+i)%8 == position%8)):
                    if(board[position+i]//10==2):
                        legalList.append(position+i)

        locations = [1,7,8,9]
        for i in (locations):
            if(position+i <64):
                if((((position+i)%8) == (position%8+1)) or (((position+i)%8) == (position%8-1)) or ((position+i)%8 == position%8)):
                    if(board[position+i]//10==2):
                        legalList.append(position+i)

    #checking for black king
    if(player == 2):
        locations = [-9,-8,-7,-1]
        for i in (locations):
            if(position+i >-1):
                if((((position+i)%8) == (position%8+1)) or (((position+i)%8) == (position%8-1)) or ((position+i)%8 == position%8)):
                    if(board[position+i]//10==1):
                        legalList.append(position+i)

        locations = [1,7,8,9]
        for i in (locations):
            if(position+i <64):
                if((((position+i)%8) == (position%8+1)) or (((position+i)%8) == (position%8-1)) or ((position+i)%8 == position%8)):
                    if(board[position+i]//10==1):
                        legalList.append(position+i)


    return legalList

def inCheck(board, player):
    kingVal = (player*10)+5
    kingPosition = -1
    for i in range(64):
        if(board[i] == kingVal):
            kingPosition = i
    return IsPositionUnderThreat(board, kingPosition, player*10)

def GetPieceLegalMoves2(board, position):
    pieceValue = board[position]
    legalList = []

    
    #check if there is a piece at that location
    if(pieceValue == 0):
        return False
    if(pieceValue%10 == 0):
        legalList += checkPawn(board,position, pieceValue//10)
    if(pieceValue%10 == 1):
        legalList += checkKnight(board,position, pieceValue//10)
    if(pieceValue%10 == 2):
        legalList += checkBishop(board,position, pieceValue//10)
    if(pieceValue%10 == 3):
        legalList += checkRook(board,position, pieceValue//10)
    if(pieceValue%10 == 4):
        legalList += checkQueen(board,position, pieceValue//10)
    if(pieceValue%10 == 5):
        legalList += checkKing(board,position, pieceValue//10)

    return legalList

def candidateMoves(board,player):
    accum = []
    x = []
    piecesList = GetPlayerPositions(board,player)
    for pieces in piecesList:
        for possibleMove in GetPieceLegalMoves(board, pieces):
            accum+= [(pieces,possibleMove)]
    for i in accum:
        tempB = list(board)
        movePiece(tempB, i[0], i[1])
        x = x+[i, worthEstimator(tempB, player)]
    return x

def worthEstimator(board, player):
    val = (-float((playerValue(board,player)+boardValue(board,player))/53202)*100)
    if(val!=0):
        return -val
    else:
        return boardValue(board,player)
                     
def hangingPiece(board,player):
    L = []
    currentPieces = GetPlayerPositions(board,player)
    for piece in currentPieces:
        for possibleMove in GetPieceLegalMoves(board,piece):
            if not(IsPositionUnderThreat(board, possibleMove, player%20+10)):
                L+= [(piece, possibleMove)]
    for i in L:
        if((player==10) and (board[i[1]]//10 == 2)):
            return i
        if((player==20) and (board[i[1]]//10 == 1)):
            return i
    return []

def GetPieceLegalMoves(board,position):
    pieceValue = board[position]
    legalSafeList = []
    legalList = GetPieceLegalMoves2(board,position)

    for i in legalList:
        tempBoard = list(board)
        tempBoard[i] = pieceValue
        tempBoard[position] = 0
        rVal = inCheck(tempBoard,pieceValue//10)
        if(rVal == False):
            legalSafeList.append(i)
        else:
            continue
    
    return legalList

def checkmate(board, player):
    flag = True
    for i in range(64):
        if(board[i]//10 != player and board[i] !=0):
            rList = GetPieceLegalMoves(board, i)
            if(rList != None):
                flag = False
                break
    return flag

#is in checkmate -> call get legal for all of your pieces

def IsPositionUnderThreat(board, position, player):
    enemyPlayer = player%20+10
    for i in checkPawn(board, position, player):
       if(board[i] == enemyPlayer):
           return True
    
    for i in checkKnight(board, position, player):
       if(board[i] == enemyPlayer+1):
           return True

    for i in checkBishop(board, position, player):
       if(board[i] == enemyPlayer+2):
           return True

    for i in checkRook(board, position, player):
       if(board[i] == enemyPlayer+3):
           return True

    for i in checkQueen(board, position, player):
       if(board[i] == enemyPlayer+4):
           return True
         
    for i in checkKing(board, position, player):
       if(board[i] == enemyPlayer+5):
           return True
    return False
        

def GetPlayerPositions(board, player):
    playerPos = []
    for i in range(64):
        if(player//10 == board[i]//10):
            playerPos.append(i)
    return playerPos

def printBoard(board):
    print("\n\nPRINTING BOARD")
    for i in range(7,-1,-1):
        accum = []
        for j in range(8):
            accum.append(board[8*i+j])
        print(accum)
    print("END PRINTING BOARD\n\n")

def movePiece(board, startLocation, endLocation):
    board[endLocation] = board[startLocation]
    board[startLocation] = 0

def chessPlayer(board, player):
    move = make_move(board,player)
    if(move[1] != []):
        return [True, move[0], candidateMoves(board,player), move[1].Get_LevelOrder()]
    else:
        return [True, move[0], candidateMoves(board,player), []]

def make_move(board, player):
    accum = []
   # if(hangingPiece(board,player) == []):
    locations = GetPlayerPositions(board,player)
    for i in locations:
        for j in GetPieceLegalMoves(board, i):
            accum = accum + [(i,j)]
    bestVal = -9999
    bestMove = None
    for i in accum:
        blankTree = tree([])
        tempBoard = list(board)
        movePiece(tempBoard, i[0], i[1])
        currentVal = minimax(tempBoard,player, 3, False, -10000, 10000, blankTree)
        if(currentVal >= bestVal):
            bestVal = currentVal
            bestMove = i

    return [bestMove, blankTree]
#    else:
#        print("USING HANGING PIECE")
#        return [hangingPiece(board,player),[]]

#2 kings on board
#right length
#pieces in right range
#


def minimax(board,player,depth, isMaximising, alpha, beta, treeParent):
    if(depth == 0):
        evalScore = -(boardValue(board, player) +playerValue(board,player))
        return evalScore

    if(isMaximising):
        accum = []
        locations = GetPlayerPositions(board,player)
        for i in locations:
            for j in GetPieceLegalMoves(board, i):
                accum = accum + [(i,j)]
        bestMoveVal = -9999
        for i in accum:
            tempBoard = list(board)
            movePiece(tempBoard, i[0], i[1])
            treeChild = tree(i)
            bestMoveVal = max(bestMoveVal, minimax(tempBoard, player, depth-1, not isMaximising, alpha, beta, treeChild))
            treeParent.AddSuccessor(treeChild)
            alpha = max(alpha, bestMoveVal)
            if(beta<=alpha):
                return bestMoveVal
        return bestMoveVal

    else:
        if(player == 10):
            otherPlayer = 20
        elif(player==20):
            otherPlayer = 10
        accum = []
        locations = GetPlayerPositions(board,otherPlayer)
        for i in locations:
            for j in GetPieceLegalMoves(board, i):
                accum = accum + [(i,j)]
        bestMoveVal = 9999
        for i in accum:
            tempBoard = list(board)
            movePiece(board, i[0], i[1])
            treeChild = tree(i)
            bestMoveVal = min(bestMoveVal, minimax(tempBoard, player, depth-1, not isMaximising, alpha, beta, treeChild))
            treeParent.AddSuccessor(treeChild)
            beta = min(beta, bestMoveVal)
            if(beta<=alpha):
                return bestMoveVal
        return bestMoveVal
    

def playerValue(board, player):
    enemyPlayer = player%20+10
    score =float(0)
    positions = GetPlayerPositions(board,player)
    for i in positions:
        if(board[i]%10 ==0):
            score+=10
        elif(board[i]%10 ==1):
            score+=30
        elif(board[i]%10 ==2):
            score+=30
        elif(board[i]%10 ==3):
            score+=50
        elif(board[i]%10 ==4):
            score+=90
        elif(board[i]%10 ==5):
            score+=900
    if(player==10):
        return score
    elif(player==20):
        return score
#    return score

def boardValue(board,player):
   listOfPieces = GetPlayerPositions(board, 10) + GetPlayerPositions(board,20)
   numPieces = len(listOfPieces)
   if(player==20):
        pawn = [0,  0,  0,  0,  0,  0,  0,  0, 5, 10, 10,-20,-20, 10, 10,  5, 5, -5,-10,  0,  0,-10, -5,  5, 0,  0,  0, 20, 20,  0,  0,  0, 5,  5, 10, 25, 25, 10,  5,  5,10, 10, 20, 30, 30, 20, 10, 10,50, 50, 50, 50, 50, 50, 50, 50, 0,  0,  0,  0,  0,  0,  0,  0]
        knight = [-50,-40,-30,-30,-30,-30,-40,-50, -40,-20,  0,  5,  5,  0,-20,-40, -30,  5, 10, 15, 15, 10,  5,-30, -30,  0, 15, 20, 20, 15,  0,-30, -30,  5, 15, 20, 20, 15,  5,-30, -30,  0, 10, 15, 15, 10,  0,-30, -40,-20,  0,  0,  0,  0,-20,-40, -50,-40,-30,-30,-30,-30,-40,-50]
        bishop = [-20,-10,-10,-10,-10,-10,-10,-20, -10,  5,  0,  0,  0,  0,  5,-10, -10, 10, 10, 10, 10, 10, 10,-10, -10,  0, 10, 10, 10, 10,  0,-10, -10,  5,  5, 10, 10,  5,  5,-10, -10,  0,  5, 10, 10,  5,  0,-10, -10,  0,  0,  0,  0,  0,  0,-10, -20,-10,-10,-10,-10,-10,-10,-20]
        rook = [100,  0,  0,  5,  5,  0,  0,  100, -5,  0,  0,  0,  0,  0,  0, -5, -5,  0,  0,  0,  0,  0,  0, -5, -5,  0,  0,  0,  0,  0,  0, -5, -5,  0,  0,  0,  0,  0,  0, -5, -5,  0,  0,  0,  0,  0,  0, -5,  5, 10, 10, 10, 10, 10, 10,  5,  100,  0,  0,  0,  0,  0,  0,  100]
        queen = [-20,-10,-10, -5, -5,-10,-10,-20,-10,  0,  5,  0,  0,  0,  0,-10,-10,  5,  5,  5,  5,  5,  0,-10,  0,  0,  5,  5,  5,  5,  0, -5, -5,  0,  5,  5,  5,  5,  0, -5,-10,  0,  5,  5,  5,  5,  0,-10,-10,  0,  0,  0,  0,  0,  0,-10,-20,-10,-10, -5, -5,-10,-10,-20]
        if(numPieces <=10):
            #king end game values
            king = [-50,-30,-30,-30,-30,-30,-30,-50, -30,-30,  0,  0,  0,  0,-30,-30,-30,-10, 20, 30, 30, 20,-10,-30,-30,-10, 30, 40, 40, 30,-10,-30,-30,-10, 30, 40, 40, 30,-10,-30,-30,-10, 20, 30, 30, 20,-10,-30,-30,-20,-10,  0,  0,-10,-20,-30,-50,-40,-30,-20,-20,-30,-40,-50]
        else:
            #king middle game values
            king = [ 20, 30, 10,  0,  0, 10, 30, 20, 20, 20,  0,  0,  0,  0, 20, 20,-10,-20,-20,-20,-20,-20,-20,-10,-20,-30,-30,-40,-40,-30,-30,-20,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30]


   if(player==10):
        pawn = [0,  0,  0,  0,  0,  0,  0,  0, 50, 50, 50, 50, 50, 50, 50, 50, 10, 10, 20, 30, 30, 20, 10, 10, 5,  5, 10, 25, 25, 10,  5,  5, 0,  0,  0, 20, 20,  0,  0,  0, 5, -5,-10,  0,  0,-10, -5,  5, 5, 10, 10,-20,-20, 10, 10,  5, 0,  0,  0,  0,  0,  0,  0,  0]
        knight = [-50,-40,-30,-30,-30,-30,-40,-50, -40,-20,  0,  0,  0,  0,-20,-40, -30,  0, 10, 15, 15, 10,  0,-30, -30,  5, 15, 20, 20, 15,  5,-30, -30,  0, 15, 20, 20, 15,  0,-30, -30,  5, 10, 15, 15, 10,  5,-30, -40,-20,  0,  5,  5,  0,-20,-40, -50,-40,-30,-30,-30,-30,-40,-50]
        bishop = [-20,-10,-10,-10,-10,-10,-10,-20, -10,  0,  0,  0,  0,  0,  0,-10, -10,  0,  5, 10, 10,  5,  0,-10, -10,  5,  5, 10, 10,  5,  5,-10, -10,  0, 10, 10, 10, 10,  0,-10, -10, 10, 10, 10, 10, 10, 10,-10, -10,  5,  0,  0,  0,  0,  5,-10, -20,-10,-10,-10,-10,-10,-10,-20]
        rook = [100,  0,  0,  0,  0,  0,  0,  100,  5, 10, 10, 10, 10, 10, 10,  5, -5,  0,  0,  0,  0,  0,  0, -5, -5,  0,  0,  0,  0,  0,  0, -5, -5,  0,  0,  0,  0,  0,  0, -5, -5,  0,  0,  0,  0,  0,  0, -5, -5,  0,  0,  0,  0,  0,  0, -5,  100,  0,  0,  5,  5,  0,  0,  100]
        queen = [-20,-10,-10, -5, -5,-10,-10,-20,-10,  0,  0,  0,  0,  0,  0,-10,-10,  0,  5,  5,  5,  5,  0,-10, -5,  0,  5,  5,  5,  5,  0, -5,  0,  0,  5,  5,  5,  5,  0, -5,-10,  5,  5,  5,  5,  5,  0,-10,-10,  0,  5,  0,  0,  0,  0,-10,-20,-10,-10, -5, -5,-10,-10,-20]
        if(numPieces <=10):
            #king end game values
            king = [-50,-40,-30,-20,-20,-30,-40,-50,-30,-20,-10,  0,  0,-10,-20,-30,-30,-10, 20, 30, 30, 20,-10,-30,-30,-10, 30, 40, 40, 30,-10,-30,-30,-10, 30, 40, 40, 30,-10,-30,-30,-10, 20, 30, 30, 20,-10,-30,-30,-30,  0,  0,  0,  0,-30,-30,-50,-30,-30,-30,-30,-30,-30,-50]
        else:
            #king middle game values
            king = [-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-20,-30,-30,-40,-40,-30,-30,-20,-10,-20,-20,-20,-20,-20,-20,-10, 20, 20,  0,  0,  0,  0, 20, 20, 20, 30, 10,  0,  0, 10, 30, 20]
   
   score = float(0)
   positions = GetPlayerPositions(board,player)
   for i in positions:
        if(board[i]%10 ==0):
            score+=pawn[i]
        elif(board[i]%10 ==1):
            score+=knight[i]
        elif(board[i]%10 ==2):
            score+=bishop[i]
        elif(board[i]%10 ==3):
            score+=rook[i]
        elif(board[i]%10 ==4):
            score+=queen[i]
        elif(board[i]%10 ==5):
            score+=king[i]
   if(player==10):
        return score
   elif(player==20):
        return score
#   return score


def initBoard():
    #init board array
    boardSize = 8
    board = [0 for i in range(boardSize*boardSize)]

    #place pawns
    for i in range(boardSize):
        board[8+i] = 10
        board[6*8+i] = 20


    #place rooks
    board[0] = board[7] = 13
    board[7*8] = board[7*8+7] = 23


    #place knights
    board[1] = board[6] = 11
    board[7*8+1] = board[7*8+6] = 21

    #place bishops
    board[2] = board[5] = 12
    board[7*8+2] = board[7*8+5] = 22

    #place queens
    board[4] = 14
    board[7*8+4] = 24

    #place kings
    board[3] = 15
    board[7*8+3] = 25

    return board

