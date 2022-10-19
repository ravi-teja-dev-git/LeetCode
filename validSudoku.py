class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in board:
            dict1 = {}
            for j in i:
                
                if j in dict1 and j!='.':
                    return False
                else:
                    dict1[j] = 1
                
        for j in range(0,9):
            dict1 = {}
            
            for i in range(0,9):
                if board[i][j] in dict1 and board[i][j]!= '.':
                    print("hello2")
                    return False
                    
                else:
                    
                    dict1[board[i][j]] = 1
                
        #squares = [[set() for x in range(3)] for y in range(3)]       
        
        
        squares = []
        for i in range(3):
            l =[]
            for j in range(3):
                l.append(set())
            squares.append(l)
        print(squares)
        
        #squares = [[set() for x in range(3)] for y in range(3)]
        print(squares)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in squares[i//3][j//3]:
                    print("hello3")
                    return False
                squares[i//3][j//3].add(board[i][j])
                    
        return True
            
        
            
                    
                    
                
        