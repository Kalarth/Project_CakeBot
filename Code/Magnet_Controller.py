import bib
import bot
import Magnet
import time

"""
Space management functions
"""


"""
Adaptative move functions
"""

def checkmagnets(M0,M5):
    LowerStatus = M0.PowerStatus
    HigherStatus = M5.PowerStatus
    if LowerStatus ==0 and HigherStatus==0 :
        return 0 #Both Magnets are turned off SHOULDN'T HAPPEN

    if LowerStatus ==1 and HigherStatus==0 :
        return 1 #The lower magnet is turned on

    if LowerStatus ==0 and HigherStatus==1 :
        return 2 #The higher magnet is turned on, which means the arm is in inverted mode

    if LowerStatus ==1 and HigherStatus==1 :
        return 3 #Both magnets are turned on, should only happen when using the tool.


def walkto_point(A,M0,M5,Position):
    """
    Position should be 3D coordinate in the form of a list [x,y,z]
    """
    orientation=checkmagnets(M0,M5)
    if orientation == 1:
        A.update(Position,[0,0,1],[0,1,0],A.arm_size)
        time.sleep(8)
        M5.Turn_ON()
        M0.Turn_OFF()


    if orientation == 2: #NOT FINISHED, NEED TO FIX THE DIRECTION TODO
        Direction = bib.normalize(bib.vec(Position))
        #A.update(Position,[0,0,1],[0,1,0],A.arm_size)
        A.update(Position,[0,0,1],Direction,A.arm_size) #NEED TO TEST
        time.sleep(8)
        M5.Turn_ON()
        M0.Turn_OFF()

    A.update([0,0,sum(A.arm_size)],[0,0,-1],[0,1,0],A.arm_size) #ARM PUTS ITSELF UPRIGHT
    time.sleep(8)

def pickup fork(A,M0,M5,Position):
    orientation=checkmagnets(M0,M5)
    #TODO
    if orientation == 1:

    if orientation == 2:

"""
Hardcoded Move functions
"""
def move_x(A,M0,M5):
    A.update([A.arm_size[2],0,0],[0,0,1],[0,1,0],A.arm_size) #MOUVEMENT EN X
    time.sleep(8)
    M5.Turn_ON()
    M0.Turn_OFF()
    A.update([0,0,sum(A.arm_size)],[0,0,-1],[0,1,0],A.arm_size) #REDRESSEMENT
    time.sleep(8)

def move_y(A,M0,M5):
    A.update([0,A.arm_size[2],0],[0,0,1],[0,1,0],A.arm_size) #MOUVEMENT EN Y
    time.sleep(8)
    M5.Turn_ON()
    M0.Turn_OFF()
    A.update([0,0,sum(A.arm_size)],[0,0,-1],[0,1,0],A.arm_size) #REDRESSEMENT
    time.sleep(8)

def move_minus_y(A,M0,M5):
    A.update([0,-A.arm_size[2],0],[0,0,1],[0,1,0],A.arm_size) #MOUVEMENT EN Y
    time.sleep(8)
    M5.Turn_ON()
    M0.Turn_OFF()
    A.update([0,0,sum(A.arm_size)],[0,0,-1],[0,1,0],A.arm_size) #REDRESSEMENT
    time.sleep(8)

def inv_move_x(A,M0,M5):
    A.update([(A.arm_size[2]),0,0],[0,0,1],[1,0,0],A.arm_size) #MOUVEMENT INVERSE EN X ATTENTION DIRECTION
    time.sleep(8)
    M0.Turn_ON()
    M5.Turn_OFF()
    A.update([0,0,sum(A.arm_size)],[0,0,-1],[0,1,0],A.arm_size) #REDRESSEMENT
    time.sleep(8)

def inv_move_y(A,M0,M5):
    A.update([0,(A.arm_size[2]),0],[0,0,1],[0,-1,0],A.arm_size) #MOUVEMENT INVERSE EN -Y ATTENTION DIRECTION
    time.sleep(10)
    M0.Turn_ON()
    M5.Turn_OFF()
    A.update([0,0,sum(A.arm_size)],[0,0,-1],[0,1,0],A.arm_size) #REDRESSEMENT
    time.sleep(10)

####MAIN
A = bot.arm()
M0 = Magnet.Magnet(12,25)
M5 = Magnet.Magnet(33,25)
