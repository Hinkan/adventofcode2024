
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
            self.pos[0]+=1
            self.score+=1
        elif self.direction=="v":
            self.pos[0]-=1
            self.score+=1
        elif self.direction==">":
            self.pos[1]+=1
            self.score+=1
        elif self.direction=="<":
            self.pos[1]-=1
            self.score+=1
        else:
            print("something went wring")

    def turn(self, char):
        pass

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
    def find_paths():


        pass
    '''
    find 
    
    
    
    
    '''

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
    list_crossroads=[]
    list_forks=[]
    for step in path:
        forks=0
        
        if [step[0]+1,step[1] ] in path:
            forks+=1
        if [step[0]-1, step[1]] in path:
            forks+=1
        if [step[0], step[1]+1] in path:
            forks+=1
        if [step[0], step[1]-1] in path:
            forks+=1
        
        if forks>2:
            list_crossroads.append(step)
            list_forks.append(forks-1)
    
    return list_crossroads, list_forks



if __name__ == "__main__":
    filename="day16_test.txt"

    map=read_map(filename)
    start, goal, walls, path=get_cords(map)
    xroads, num, forks=find_crossroads(path)


    printmap(map)

    print(path)
    print(xroads)