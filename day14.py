
class Robot():
    def __init__(self, pos, speed, map):
        self.row=pos[0]
        self.col=pos[1]
        self.rowspeed=speed[0]
        self.colspeed=speed[1]
        self.maxrow=map[0]
        self.maxcol=map[1]

    
    def move(self):
        self.row=(self.row+self.rowspeed+self.maxrow)%self.maxrow
        self.col=(self.col+self.colspeed+self.maxcol)%self.maxcol
    def get_quadrant(self):
        if self.row<self.maxrow/2 and self.col<self.maxcol/2:
            return 1
        elif self.row<self.maxrow/2 and self.col>self.maxcol/2:
            return 2
        elif self.row>self.maxrow/2 and self.col<self.maxcol/2:
            return 3
        elif self.row>self.maxrow/2 and self.col>self.maxcol/2:
            return 4
        else:
            return None
        
        

import re
def read_robots(filename):

    f=open(filename)
    robot_cords=[]
    for line in f:
        location=re.findall('\d', line)
        row=int(location[0])
        col=int(location[1])
        row_v=int(location[2])
        col_v=int(location[3])
        pos=[row, col]
        speed=[row_v, col_v]
        robot_cords.append([pos, speed])
    return robot_cords


if __name__=='__main__':
    filename="day14_test.txt"
    map_dimensions=[7,11]
    secs=100
    robot_cords=read_robots(filename)
    
    robots=[]
    for cords in (robot_cords):
        robot=Robot(cords[0], cords[1], map_dimensions)
        robots.append(robot)
    print(f'num robots:{len(robots)}')
    for sec in range(secs):
        for robot in robots:
            robot.move()
    
    quadcount=[0,0,0,0]
    middle=0
    for robot in robots:
        quad=robot.get_quadrant()
        if quad==1:
            quadcount[0]+=1
        if quad==2:
            quadcount[1]+=1
        if quad==3:
            quadcount[2]+=1
        if quad==4:
            quadcount[3]+=1
        if quad==None:
            middle+=1
    print(f'quadcount:{quadcount}')
    print(f'middle:{middle}')

    safety=1
    for quad in quadcount:
        safety*=quad
    print(safety)
        