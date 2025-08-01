#TODO pop the last cordinates from the found branching


def read_map(filename):
    f=open(filename)
    map=[]
    for line in f:
        map.append(line[:-1])
    
    return map

class walker():
    def __init__(self, start, end, path):
        self.start=start
        self.end=end

        self.pos=start
        self.direction=">"
        self.path=path
        self.score=0

        self.stepped=[]

    def step(self):
        if self.direction=="^":
            self.pos[0]-=1
            self.score+=1
        elif self.direction=="v":
            self.pos[0]+=1
            self.score+=1
        elif self.direction==">":
            self.pos[1]+=1
            self.score+=1
        elif self.direction=="<":
            self.pos[1]-=1
            self.score+=1
        else:
            print("something went wring")

    def turn(self, newdirection):
        self.direction=newdirection
        self.score+=1000

    def check_ways(self):
        forks=0
        if [self.pos[0]+1,self.pos[1] ] in self.path:
            forks+=1
        if [self.pos[0]-1, self.pos[1]] in self.path:
            forks+=1
        if [self.pos[0], self.pos[1]+1] in self.path:
            forks+=1
        if [self.pos[0], self.pos[1]-1] in self.path:
            forks+=1
        return forks
    
    def get_possible_paths(self):
        possible_paths=[]
        if [self.pos[0]+1,self.pos[1] ] in self.path:
            possible_paths.append([self.pos[0]+1,self.pos[1]])
        if [self.pos[0]-1, self.pos[1]] in self.path:
            possible_paths.append([self.pos[0]-1, self.pos[1]])
        if [self.pos[0], self.pos[1]+1] in self.path:
            possible_paths.append([self.pos[0], self.pos[1]+1])
        if [self.pos[0], self.pos[1]-1] in self.path:
            possible_paths.append([self.pos[0], self.pos[1]-1])
        return possible_paths
    
    def get_direction(self, currentpos, newpos):
        if currentpos[0]>newpos[0]:
            return "^"
        elif currentpos[0]<newpos[0]:
            return "v"
        elif currentpos[1]>newpos[1]:
            return "<"
        elif currentpos[1]<newpos[1]:
            return ">"
        else:
            return None



    def find_paths(self, cords_stepped):

        
        
        

        possible_paths=self.get_possible_paths()
        for idx,pp in enumerate(possible_paths):
            a=str(pp)
            if str(pp) in cords_stepped:
                possible_paths.pop(idx)

        if self.pos==self.end:#find the end
            print(cords_stepped, self.score)
            return True
        if len(possible_paths)==0:#dead end
            return False
        if str(self.pos) in cords_stepped:
            return False
        cords_stepped.append(str(self.pos.copy()))

        while len(possible_paths)>0:
            path=possible_paths.pop()
            newdirection=self.get_direction(self.pos, path)

            if newdirection==self.direction:
                self.step()
            else:
                self.turn(newdirection)
                self.step()
            self.find_paths(cords_stepped)
            





def printmap(map):

    for row in map:
        print(row)
def get_cords(map):
    start=None
    goal=None
    walls=[]
    path=[]
    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if col=="#":
                walls.append([row_idx, col_idx])
            elif col==".":
                path.append([row_idx, col_idx])
            elif col=="S":
                start=[row_idx, col_idx]
            elif col=="E":
                goal=[row_idx, col_idx]
            else:
                print("unknown map symbol")
    
    return start, goal, walls, path

def find_crossroads(path):
    cross=[]
    list_crossroads=[]
    
    for step in path:
        forks=0
        list_forks=[]    
        if [step[0]+1,step[1] ] in path:
            list_forks.append([step[0]+1,step[1] ])
            forks+=1
        if [step[0]-1, step[1]] in path:
            list_forks.append([step[0]-1,step[1] ])
            forks+=1
        if [step[0], step[1]+1] in path:
            list_forks.append([step[0],step[1]+1 ])
            forks+=1
        if [step[0], step[1]-1] in path:
            list_forks.append([step[0],step[1]-1 ])
            forks+=1
        
        if forks>2:
            cross.append({"cordinate":step, "forks":list_forks})
            

    
    
    return cross



if __name__ == "__main__":
    filename="day16_test.txt"

    map=read_map(filename)
    start, goal, walls, path=get_cords(map)
    list_crossroads=find_crossroads(path)

    


    printmap(map)
    

    w=walker(start, goal, path)
    cords_stepped=[]
    w.find_paths(cords_stepped)
