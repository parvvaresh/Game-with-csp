class board_game:
    def __init__(self, puzzel = 1):
        if puzzel == 1:
            self.puzzel = puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0], 
                                    [6, 0, 0, 1, 9, 5, 0, 0, 0], 
                                    [0, 9, 8, 0, 0, 0, 0, 6, 0], 
                                    [8, 0, 0, 0, 6, 0, 0, 0, 3], 
                                    [4, 0, 0, 8, 0, 3, 0, 0, 1], 
                                    [7, 0, 0, 0, 2, 0, 0, 0, 6], 
                                    [0, 6, 0, 0, 0, 0, 2, 8, 0], 
                                    [0, 0, 0, 4, 1, 9, 0, 0, 5], 
                                    [0, 0, 0, 0, 8, 0, 0, 0, 0]     
                                    ] 
        else:self.puzzel = puzzel
    
    def show_puzzel(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:    
                print("- - - - - - - - - - - ") 
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                
                print(self.puzzel[i][j], end=" ")
            print()
    
    def get_puzzel(self):
        return self.puzzel
    
    def set_puzzel(self, puzzel):
        self.puzzel = puzzel
                  
            