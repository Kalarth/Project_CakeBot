import Arm_calculus as bib
import Arm as bot
import Magnet as mag
import time
import Move
import Walk
import Tool
import Fork

####MAIN
class Brain():
    """docstring for Brain."""

    def Pickup_Cake_Fork(self):
        self.Forkmode.pickup_fork(Position)
        self.Forkmode.pickup_cake(Position)
        self.Forkmode.present_cake()

    def Find_Way(self):
        self.Camscan()
        for i in range(len(way)):
            self.Walkmode.walkto_point(self.way[i])
        self.Pickup_Cake_Fork()

    def Camscan(self):
        self.way=self.Cam.getspace() #PLACEHOLDER

    def Deactivate(self):
        M0.Turn_OFF()
        M5.Turn_OFF()
        M0.destroy()

    def __init__(self):
        self.A = bot.Arm()
        self.M0 = mag.Magnet(12,25)
        self.M5 = mag.Magnet(33,25)
        self.M0.TURN_ON()
        self.Walkmode=Walk.Walk(A,M0,M5)
        self.Forkmode=.Fork.Fork(A,M0,M5)
        self.Cam=Camera.Camera(A.arm_size[2])
"""
A = bot.arm()
M0 = mag.Magnet(12,25)
M5 = mag.Magnet(33,25)
"""
