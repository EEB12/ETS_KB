import copy
import sys
import queue as Q
import time
import tkinter as tk

def readMap(fileMap):
    with open(fileMap) as f:
        MAP_ROW, MAP_COL, xStart, yStart = [int(x) for x in next(f).split()] # read first line
        sourceMap = []
        countMapLine = 1
        for line in f: # read map
            countMapLine += 1
            sourceMap.append([int(x) for x in line.split()])
            if countMapLine > MAP_ROW: break

        # read managedBoard
        manaBoa = []
        for line in f: # read manaBoa
            # 2 2 4 4 4 5
            manaBoa.append([int(x) for x in line.split()])

    print("\nYOUR MAP LOOK LIKE THIS:")
    for item in sourceMap:
        print(item)
    print("Start at (",xStart, ",", yStart,")")
    print("ManaBoa:")
    for item in manaBoa:
        print(item)
    print("readMap======================================")
    return MAP_ROW, MAP_COL, xStart, yStart, sourceMap, manaBoa


class Block:
    
    def __init__(self, x, y, rot, parent, board, x1=None,y1=None, gn=0):
        self.x      = x
        self.y      = y
        self.rot    = rot  
        self.parent = parent
        self.board  = copy.deepcopy(board)
        self.x1     = x1
        self.y1     = y1
        if(parent != None):
            self.gn     = parent.gn + 1
        else:
            self.gn = gn
    
    def __lt__(self, block):
        return True
    def __gt__(self, block):
        return True

    def move_up(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board,self.gn)

        if self.rot == "STANDING":
            newBlock.y -= 2 
            newBlock.rot = "LAYING_Y"

        elif newBlock.rot == "LAYING_X":
            newBlock.y -= 1
        
        elif newBlock.rot == "LAYING_Y":
            newBlock.y -= 1
            newBlock.rot = "STANDING"
        
        return newBlock 

    def move_down(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board,self.gn)

        if newBlock.rot == "STANDING":
            newBlock.y += 1
            newBlock.rot = "LAYING_Y"

        elif newBlock.rot == "LAYING_X":
            newBlock.y += 1

        elif newBlock.rot == "LAYING_Y":
            newBlock.y += 2
            newBlock.rot = "STANDING"
        return newBlock 

    def move_right(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board,self.gn)
    
        if newBlock.rot == "STANDING":
            newBlock.x += 1
            newBlock.rot = "LAYING_X"

        elif newBlock.rot == "LAYING_X":
            newBlock.x += 2
            newBlock.rot = "STANDING"

        elif newBlock.rot == "LAYING_Y":
             newBlock.x += 1
        return newBlock

    def move_left(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board,self.gn)

        if newBlock.rot == "STANDING":
            newBlock.rot = "LAYING_X"
            newBlock.x -= 2

        elif newBlock.rot == "LAYING_X":
            newBlock.x -= 1
            newBlock.rot = "STANDING"

        elif newBlock.rot == "LAYING_Y":
            newBlock.x -= 1

        return newBlock 

    # FOR CASE SPLIT
    def split_move_up(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1,self.gn + 1)
        newBlock.y -= 1
        return newBlock 

    def split_move_down(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1,self.gn)
        newBlock.y += 1
        return newBlock 


    def split_move_left(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1,self.gn)
        newBlock.x -= 1
        return newBlock 


    def split_move_right(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1,self.gn)
        newBlock.x += 1
        return newBlock 

    def split1_move_up(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1,self.gn)
        newBlock.y1 -= 1
        return newBlock 

    def split1_move_down(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1,self.gn)
        newBlock.y1 += 1
        return newBlock 

    def split1_move_left(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1, self.gn)
        newBlock.x1 -= 1
        return newBlock 

    def split1_move_right(self):
        newBlock = Block(self.x, self.y, self.rot, self, self.board, self.x1, self.y1,self.gn)
        newBlock.x1 += 1
        return newBlock 

    def disPlayPosition(self):
        if self.rot != "SPLIT":
            print(self.rot, self.x, self.y)
        else:
            print(self.rot, self.x, self.y, self.x1, self.y1)
    
    def disPlayBoard(self):
        
        # local definition
        x   = self.x
        y   = self.y
        x1  = self.x1
        y1  = self.y1
        rot = self.rot
        board = self.board

        # let's go

        if rot != "SPLIT":
            
            for i in range(len(board)): # for ROW
                print("",end='  ')
                for j in range(len(board[i])): # for COL in a ROW

                    if (i==y and j==x and rot=="STANDING") or \
                            ((i==y and j==x) or (i==y and j==x+1) and rot=="LAYING_X") or \
                            ((i==y and j==x) or (i==y+1 and j==x) and rot=="LAYING_Y"):

                        print("x",end=' ')

                    elif(board[i][j]==0):
                        print(" ",end=' ')
                    else:
                        print(board[i][j], end=' ')
                print("")
        else: # CASE SPLIT
            for i in range(len(board)): # for ROW
                print("",end='  ')
                for j in range(len(board[i])): # for COL

                    if (i==y and j==x) or (i==y1 and j==x1):
                        print("x",end=' ')

                    elif(board[i][j]==0):
                        print(" ",end=' ')
                    else:
                        print(board[i][j], end=' ')
                print("")
            
    
# Case 3
def isNumberThree(block,x,y):
    board = block.board

    for item in ManaBoa:

        if (x,y) ==  (item[0], item[1]):

            # TOGGLEEEE

            numToggle = item[2]   # num toggle
            index = 2   # index to check more element

            for i in range(numToggle):    # traverse toggle array
                bX = item[2*i+3]
                bY = item[2*i+4]
                if board[bX][bY] == 0:
                    board[bX][bY] = 1
                else:
                    board[bX][bY] = 0
        
            index = index + 1 + 2 * numToggle

            # CLOSEEEE

            # check if "item" has more element
            if index < len(item):   # case has more

                # read num close
                numClose = item[index]

                # traverse list close if num > 0
                for i in range(numClose):
                    bX = item[index+2*i+1]
                    bY = item[index+2*i+2]
                    board[bX][bY]=0

                index = index + 1 + 2 * numClose
            

            # OPEENNNN

            # check if "item" has more element
            if index < len(item):   # case also has more item
                # get num open
                numOpen = item[index]

                # traverse list open if num > 0
                for i in range(numOpen):
                    bX = item[index+2*i+1]
                    bY = item[index+2*i+2]
                    board[bX][bY]=1



# Case 4
def isNumberFour(block,x,y):
    board = block.board
    
    #print("(x-y) = (", x,"-", y,")")

    for item in ManaBoa:
        if (x,y) ==  (item[0], item[1]):
            num = item[2]
            for i in range(num):
                bX = item[2*i+3]
                bY = item[2*i+4]
                board[bX][bY] = 0

# Case 5: 
def isNumberFive(block,x,y):
    board = block.board

    for item in ManaBoa:
        if (x,y) ==  (item[0], item[1]):


            numToggle = item[2]     # numtoggle
            index = 2   # index to check more element

            for i in range(numToggle):
                bX = item[2*i+3]
                bY = item[2*i+4]
                if board[bX][bY] == 0:
                    board[bX][bY] = 1
                else:
                    board[bX][bY] = 0
            
            index = index + 1 + 2 * numToggle

            # CLOSEEEE

            # check if "item" has more element
            if index < len(item):   # case has more

                # read num close
                numClose = item[index]
                    
                # traverse list close if num > 0
                for i in range(numClose):
                    bX = item[index+2*i+1]
                    bY = item[index+2*i+2]
                    board[bX][bY]=0

                index = index + 1 + 2 * numClose
            

            # OPEENNNN

            # check if "item" has more element
            if index < len(item):   # case also has more item
                # get num open
                numOpen = item[index]

                # traverse list open if num > 0
                for i in range(numOpen):
                    bX = item[index+2*i+1]
                    bY = item[index+2*i+2]
                    board[bX][bY]=1


# Case 6: 
def isNumberSix(block,x,y):
    board = block.board

    for item in ManaBoa:
        if (x,y) ==  (item[0], item[1]):
            num = item[2]
            for i in range(num):
                bX = item[2*i+3]
                bY = item[2*i+4]
                board[bX][bY] = 1

# Case 7: 
def isNumberSeven(block,x,y):  
    board = block.board
    array = []    
    for item in ManaBoa:
        if (x,y) ==  (item[0], item[1]):
            num = item[2]
            # format x7 y7 2 x y x1 y1
            for i in range(num):
                bX = item[2*i+3]
                bY = item[2*i+4]
                array.append([bX,bY])

    (block.y,block.x,block.y1,block.x1) = \
            (array[0][0],array[0][1],array[1][0], array[1][1])

    block.rot = "SPLIT"

# Case 8: 
def isNumberEight(block,x,y):
    board = block.board

    for item in ManaBoa:
        if (x,y) ==  (item[0], item[1]):

            num = item[2]
            for i in range(num):
                bX = item[2*i+3]
                bY = item[2*i+4]
                board[bX][bY] = 1




# isValidBLock
def isValidBlock(block):
    
    if isFloor(block):
        
        # local definition
        x     = block.x
        y     = block.y
        x1    = block.x1
        y1    = block.y1
        rot   = block.rot
        board = block.board
        gn    = block.gn
        
        
        # Case 2
        if rot == "STANDING" and board[y][x] == 2:
            return False 

        # Case 3
        if rot == "STANDING" and board[y][x] == 3:
            isNumberThree(block,x,y)
        
        # Case 4
        if board[y][x] == 4:
            isNumberFour(block,x,y)
        if rot == "LAYING_X" and board[y][x+1] == 4:
            isNumberFour(block,x+1,y)
        if rot == "LAYING_Y" and board[y+1][x] == 4:
            isNumberFour(block,x,y+1)
        if rot == "SPLIT" and board[y1][x1] == 4:
            isNumberFour(block,x1,y1)


        # Case 5
        if board[y][x] == 5:
            isNumberFive(block,x,y)
        if rot == "LAYING_X" and board[y][x+1] == 5:
            isNumberFive(block,x+1,y)
        if rot == "LAYING_Y" and board[y+1][x] == 5:
            isNumberFive(block,x,y+1)
        if rot == "SPLIT" and board[y1][x1] == 5:
            isNumberFive(block,x1,y1)

        # Case 6
        if board[y][x] == 6:
            isNumberSix(block,x,y)
        if rot == "LAYING_X" and board[y][x+1] == 6:
            isNumberSix(block,x+1,y)
        if rot == "LAYING_Y" and board[y+1][x] == 6:
            isNumberSix(block,x,y+1)
        if rot == "SPLIT" and board[y1][x1] == 6:
            isNumberSix(block,x1,y1)

        # Case 7
        if rot == "STANDING" and board[y][x] == 7:
            isNumberSeven(block,x,y)
        # Case7_1: MERGE BLOCK
        if rot == "SPLIT": # check IS_MERGE
            # case LAYING_X: x first
            if y == y1 and x == x1 -1:
                block.rot = "LAYING_X"

            # case LAYING_X: x1 first
            if y == y1 and x == x1 + 1:
                block.rot = "LAYING_X"
                block.x   = x1

            # case LAYING_Y: y first
            if x == x1 and y == y1 - 1:
                block.rot = "LAYING_Y"
            
            # case LAYING_Y: y1 first
            if x == x1 and y == y1 + 1:
                block.rot = "LAYING_Y"
                block.y   = y1

        # Case 8
        if rot == "STANDING" and board[y][x] == 8:
            isNumberEight(block,x,y)
            
        return True
    else:
        return False


def isFloor(block):
    x = block.x
    y = block.y
    rot = block.rot
    board = block.board
    
    if x >= 0 and y >= 0 and \
            y < MAP_ROW and x < MAP_COL and \
            board[y][x] != 0:

        if rot == "STANDING":
            return True
        elif rot == "LAYING_Y":
            if y+1 < MAP_ROW and board[y+1][x] != 0 :
                return True
        elif rot == "LAYING_X":
            if x+1 < MAP_COL and board[y][x+1] != 0 :
                return True
        else: # case SPLIT
            x1 = block.x1
            y1 = block.y1

            if x1 >= 0 and y1 >= 0 and \
                y1 < MAP_ROW and x1 < MAP_COL and \
                board[y1][x1] != 0:
                    return True

    else:
        return False


def isGoal(block):
    x = block.x
    y = block.y
    rot = block.rot
    board = block.board

    if rot == "STANDING" and  \
        board[y][x] == 9:
        return True
    else:
        return False


def isVisited(block):
    if block.rot != "SPLIT":

        for item in passState:
            if item.x == block.x     and item.y == block.y and \
                item.rot == block.rot and item.board == block.board:
                return True

    else: # case SPLIT
        for item in passState:
            if item.x  == block.x     and item.y  == block.y and \
               item.x1 == block.x1    and item.y1 == block.y1 and \
                item.rot == block.rot and item.board == block.board:
                return True

    return False

  

def printSuccessRoad(block):
    
    print("\nTHIS IS SUCCESS ROAD")
    print("================================")
    
    successRoad = [block]
    temp = block.parent
    
    while temp != None:
        
        if temp.rot != "SPLIT":
            newBlock = Block(temp.x, temp.y, \
                    temp.rot, temp.parent, temp.board)
        else: # case SPLIT
            newBlock = Block(temp.x, temp.y, \
                    temp.rot, temp.parent, temp.board, temp.x1, temp.y1)

        successRoad = [newBlock] + successRoad
        
        temp = temp.parent
    
    step = -1
    for item in successRoad:
        step += 1
        time.sleep(0.6)
        # print("\nStep:", step, end=' >>>   ')
        item.disPlayPosition()
        # print("=============================")
        item.disPlayBoard()

    print("COMSUME",step,"STEP!!!!")
    
    return item
    
def evalFunction(block):

    #  local definition
    x   = block.x
    y   = block.y
    x1  = block.x1
    y1  = block.y1
    rot = block.rot
    board = block.board

    # get goal
    (xGoal, yGoal) = (0, 0)
    for yG in range(len(board)):
        for xG in range(len(board[0])):
            if board[yG][xG] == 9:
                (xGoal, yGoal) = (xG, yG)
            # print("board:", board[yG][xG])

    # print("goal:", xGoal, ",", yGoal)
    # print("current", x, ",", y)
    # calc distance pos-goal
    distance = 0

    # Heuristic Function with chebyshev
    if rot == "SPLIT":

        distance1 = max(abs(x-xGoal),abs(y-yGoal))
        distance2 = max(abs(x1-xGoal),abs(y1-yGoal))
        distance = (distance1+distance2)/2

    else:
        # (x1 - x2)^2 + (y1 - y2) ^ 2
        distance = max(abs(x-xGoal),abs(y-yGoal))

    return int(distance)

def moveAStar(AStarQueue, block, flag):
    
    if isValidBlock(block):
        if isVisited(block):            
            return False
        
        EvalCur = evalFunction(block)
        block.gn += 1
        # print("block.gn + EvalCur:", block.gn + EvalCur, block.gn, EvalCur)
        AStarQueue.put((block.gn + EvalCur, block))
        passState.append(block)

        return True
    return False
        
def AStar(block):
    
    # create priority queue
    AStarQueue = Q.PriorityQueue()
    # print(sizepq(AStarQueue))

    startEval = evalFunction(block)
    # block.gn+=1
    # insert start node
    AStarQueue.put((startEval, block))
    passState.append(block)
    
    virtualStep = 0

    AStarq = 0
    # until priority queue is empty
    while AStarQueue.not_empty:
        temp = AStarQueue
        AStarq += 1
        item   = AStarQueue.get()  # item = (distance, block)
        iDista = item[0]
        iBlock = item[1]
        # print("while:", AStarq, iDista)

        # if goal
        if isGoal(iBlock):

            lastPath = printSuccessRoad(iBlock)
            print("SUCCESS")
            print("COMSUME", virtualStep, "VIRTUAL STEP")
            
            lastPath.disPlayPosition()
            lastPath.disPlayBoard()

            while not AStarQueue.empty():
                try:
                    AStarQueue.get(False)
                except Empty:
                    continue
                AStarQueue.task_done()
            handler(iBlock)

            return True

        # put all new operator to queue
        if iBlock.rot != "SPLIT":
            
            virtualStep += 4

            # try up
            moveAStar(AStarQueue, iBlock.move_up(), "up") 
            moveAStar(AStarQueue, iBlock.move_down(), "down") 
            moveAStar(AStarQueue, iBlock.move_right(), "right") 
            moveAStar(AStarQueue, iBlock.move_left(), "left") 
        else: 
           
            virtualStep += 8

            moveAStar(AStarQueue, iBlock.split_move_left(), "left0")
            moveAStar(AStarQueue, iBlock.split_move_right(), "right0")
            moveAStar(AStarQueue, iBlock.split_move_up(), "up0")
            moveAStar(AStarQueue, iBlock.split_move_down(), "down0")
            
            moveAStar(AStarQueue, iBlock.split1_move_left(), "left1")
            moveAStar(AStarQueue, iBlock.split1_move_right(), "right1")
            moveAStar(AStarQueue, iBlock.split1_move_up(), "up1")
            moveAStar(AStarQueue, iBlock.split1_move_down(), "down1")
        # time.sleep(0.6)
        # iBlock.disPlayBoard()

def key(event, arg):
    arg = passHandler[-1]
    """shows key or tk code for the key"""
    # while(True):
    if event.keysym == 'space':
        root.quit()
    if event.keysym == 'Escape':
        root.destroy()
    if event.keysym == 'Left':
        arg = arg.move_left()
    if event.keysym == 'Right':
        arg = arg.move_right()
    if event.keysym == 'Down':
        arg = arg.move_down()
    if event.keysym == 'Up':
        arg = arg.move_up()
  
    
    passHandler.append(arg)
    passHandler[-1].disPlayBoard()
    
    if isFloor(arg) != True:
        print("\n----------------------- GAME OVER -----------------------")
        sys.exit()
        root.destroy()
        

def handler(blocks):   
    print( "\nPress arrow (up/down/right/left) to move" )
    print( "Press Space Bar to find solution" )
    print( "Press Esc to exit" )
    passHandler.append(blocks)
    root.bind_all('<Key>', lambda event, arg=blocks: key(event,arg) )

    try:
        # don't show the tk window
        root.withdraw() 
        root.mainloop()

        if sys.argv[1:][1] == "AStar":
            
            print("Solve AStar")
            passState.clear()
            print('passState:', passState)
            passHandler[-1].parent = None
            passHandler[-1].gn = 0
            passHandler[-1].disPlayBoard()
            AStar(passHandler[-1])

        else:
            print("Wrong algorithms argument!")
    except:
        print("\n-=-=-=-=-=- Game Selesai -=-=-=-=-=-")

# START PROGRAM HERE
passState = []
passHandler = []

MAP_ROW, MAP_COL, xStart, yStart, sourceMap, ManaBoa \
                        = readMap('map/map'+sys.argv[1:][0]+'.txt')

global block
block = Block(xStart, yStart, "STANDING", None, sourceMap)

root = tk.Tk()

if sys.argv[1:][1] == "AStar":
    print("Solve AStar")
    AStar(block)

else:
    print("Wrong algorithms argument!")