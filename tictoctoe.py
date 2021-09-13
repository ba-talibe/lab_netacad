from random import randrange

board = [[1, 2, 3],
         [4, "X", 6],
         [7, 8, 9]
        ]

def DisplayBoard(board):
    intercal = "|       |       |       |"
    border = ("+-------" * 3) + "+"
    for i in board:
        print(border)
        print(intercal)
        print("|   " + str(i[0]) + "   |   " + \
                (i[1]) + "   |   " + str(i[2]) \
            + "   |")
        print(intercal)

    print(border)

# the function accepts one parameter containing the board's current status

# and prints it out to the console

#

def EnterMove(board):

    move = int(input("Enter your move : "))
    while move <= 0 or move >= 10:
        move = int(input("Enter your move : "))
    if move not in MakeListOfFreeFields(board):
    	print("this move is not valid please retry")
    	EnterMove(board)
    	
    l, c = (move - 1) //3, (move - 1) % 3
    board[l][c] = 'O'
    DisplayBoard(board)
    
#

# the function accepts the board current status, asks the user about their move, 

# checks the input and updates the board according to the user's decision

#

def MakeListOfFreeFields(board):
	lst = []
	cpt = 0
	for i in board:
		for j in i:
			cpt += 1
			if j != 'X' and j != 'O':
				lst.append(cpt)
	return lst
 
#

# the function browses the board and builds a list of all the free squares; 

# the list consists of tuples, while each tuple is a pair of row and column numbers

#

def VictoryFor(board, sign):
        victory = False
        for i in range(3): #conformation vertical
                if all(j == sign for j in board[i]):
                        victory = True
                        
        for i in range(3): #conformation horizontale
                if all(j[i] == sign for j in board):
                         victory = True
        			
        if all (board[i][i] == sign for i in range(3)): #conformation diagonal seconde bissectrice
                    victory = True
                    
        if all (board[-i][i-4] == sign for i in range(1, 4)):#conformation diagonal premiere bissectrice
                    victory = True    
        return victory


#

# the function analyzes the board status in order to check if 

# the player using 'O's or 'X's has won the game

#

def DrawMove(board):

	move = randrange(1, 10)
	while move not in MakeListOfFreeFields(board):
		move = randrange(1, 10)

	l, c = (move - 1) //3, (move - 1) % 3
	board[l][c] = 'X'
	DisplayBoard(board)

#

# the function draws the computer's move and updates the board

#
"""
DisplayBoard(board)
while 1:
	EnterMove(board)
	playerSign = 'O'
	computerSign = 'X'
	if VictoryFor(board, playerSign):
		print("You won!")
		break
	DrawMove(board)
	if VictoryFor(board, computerSign):
		print("Computer Wons !")
		break
	if len(MakeListOfFreeFields(board)) == 1:
		print("DRAW !!!")
		break
"""
DisplayBoard(board)
while 1:
    EnterMove(board)
    DisplayBoard(board)

    if VictoryFor(board, playerSign):
        print("Vous avez gagnez !")
        break

    print("Ordinateur :")
    DrawMove(board)
    DisplayBoard(board)

    if VictoryFor(board, computerSign):
        print("Vous avez perdu !")
        break
        
    if len(MakeListOfFreeFields(board)) == 0:
        print("DRAW !!!")
        break

    
