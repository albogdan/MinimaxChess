from asstfuncs import initBoard, checkmate, minimax, make_move, pBoard, GetPlayerPositions, IsPositionUnderThreat, GetPieceLegalMoves, printBoard, movePiece, chessPlayer, tree, queue
import time,timeit

board = initBoard()
done = False
while not(done):
    #white player - sentient
    pBoard(board)
    #black player - AI
    start = time.time()

    #blackMove = chessPlayer(board, 20)
    blackMove = chessPlayer(board,20)
    print("THE BLACK MOVE", blackMove[2])
    end = time.time()
    #print("TIME:", (end-start))
    #movePiece(board, blackMove[0], blackMove[1])
    
    movePiece(board, blackMove[1][0], blackMove[1][1])
    #print("LENLVL", len(blackMove[3]))
    check = checkmate(board,10)
    if(check):
        break


    pBoard(board)
    start = time.time()
    whiteMove = chessPlayer(board,10)#make_move(board, 10)#, 3, True)
 #   print("THE WHITE MOVE", whiteMove[2])
    #whiteMove = chessPlayer(board,10)
    end = time.time()
    #print("TIME:", (end-start))
    
    #print("THE MINI MOVE", whiteMove)
    #movePiece(board, whiteMove[0], whiteMove[1])
    movePiece(board, whiteMove[1][0], whiteMove[1][1])

    #print("LENLVL", len(whiteMove[3]))

    checkmate(board,20)
    if(check):
        break

"""    currentLocation = int(raw_input("Enter white piece to move: "))
    whiteLocations = GetPlayerPositions(board,10)
    while(currentLocation not in whiteLocations):
        currentLocation = int(raw_input("No white piece at that location, try again: "))

    moveToLocation = int(raw_input("Enter location to move to: "))
    whitePossibleLocations = GetPieceLegalMoves(board, currentLocation)
    while(moveToLocation not in whitePossibleLocations):
        moveToLocation = int(raw_input("Cannot move there: "))

    movePiece(board,currentLocation, moveToLocation)
"""



print("\n\n\n")
#print(GetPlayerPositions(board, 10))

#print(GetPieceLegalMoves(board, 48))

print(IsPositionUnderThreat(board, 33, 10))



