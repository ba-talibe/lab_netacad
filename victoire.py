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

