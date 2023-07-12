board=[[' ' for _ in range(3)] for _ in range(3)]

def printBoard():
    print("-------------")
    for row in board:
        print("|", end=' ')
        for cell in row:
            print(cell, end=' | ')
        print("\n-------------")

def checkWin(player):
    print("entered")
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def takeInput(player):
    r=int(input(player+" enter row: "))
    c=int(input(player+" enter col: "))

    if board[r][c]==' ':
        board[r][c]=player
    else:
        print("Spot already taken! Try again")
        takeInput(player)

def main():
    currentPlayer='X'
    nextPlayer='O'

    gameover=False
    while not gameover:
        if checkWin(currentPlayer):
            print("Player ",currentPlayer," won!")
            gameover=True
            break
        takeInput(currentPlayer)
        printBoard()
        for row in board:
            print(row.count(currentPlayer))
        temp=currentPlayer
        currentPlayer=nextPlayer
        nextPlayer=temp
        print(board)
        

        

main()


