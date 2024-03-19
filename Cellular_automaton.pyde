GRID_W = 15
GRID_H = 15

#Size of cell
#SZ = 18
class Cell:
    def __init__(self,c,r,state=0):
        self.c = c
        self.r = r
        self.state = state
        
    def display(self):
        if self.state == 1:
            fill(0)
        else:
            fill(255)
        noStroke()
        rect(SZ*self.r,SZ*self.c,SZ,SZ)
    def checkNeighbors(self,cellList):
        if self.state == 1:return 1
        neighbs = 0 
        #check the neighbors
        for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            try:
                if cellList[self.r + dr][self.c +dc].state == 1:
                    neighbs += 1
            except IndexError:
                continue
        if neighbs in [1,4]:
            return 1
        else:
            return 0
        
def setup():
    global SZ,cellList
    size(600,600)
    SZ = width // GRID_W +1
    cellList = createCellList()

    
def draw():
    for row in cellList:
        for cell in row:
            cell.state = cell.checkNeighbors()
            cell.display()
            



       
            
            
def createCellList():
    newList=[]
    for j in range(GRID_H):
        newList.append([])
        for i in range(GRID_W):
            newList [j].append(Cell(i,j,0))
            
    newList [GRID_H//2][GRID_W//2].state = 1
    return newList
                 

        
    
    
