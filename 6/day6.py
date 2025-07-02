class guard():
    def __init__(self,map, row, col, dir):
        self.map=map
        self.row=row
        self.col=col
        self.dir=dir
        self.unique_spaces=0
        self.path=[]
    
    def move(self):
        new_row=self.row
        new_col=self.col
        if self.dir=="^":
            new_row=self.row-1
        elif self.dir=="v":
            new_row=self.row+1
        elif self.dir=="<":
            new_col=self.col-1
        elif self.dir==">":
            new_col=self.col+1
        if self.check_collision(new_row, new_col):
            if self.dir=="^":
               self.dir=">"
            elif self.dir=="v":
                self.dir="<"
            elif self.dir=="<":
                self.dir="^"
            elif self.dir==">":
                self.dir="v"
            new_col=self.col
            new_row=self.row
            self.unique_spaces+=1
            self.map[self.row][self.col]="+"
        else:
            #if self.map[self.row][self.col]!="X"  :
            #    self.unique_spaces+=1
            #    self.map[self.row][self.col]="X"
            
            if self.dir=="^" or self.dir=="v":
                if self.map[self.row][self.col]=="-" or self.map[self.row][self.col]=="+":
                    self.map[self.row][self.col]="+"
                else:
                    self.map[self.row][self.col]="|"
                    self.unique_spaces+=1
            if self.dir=="<" or self.dir==">":
                if self.map[self.row][self.col]=="|"or self.map[self.row][self.col]=="+":
                    self.map[self.row][self.col]="+"
                else:
                    self.map[self.row][self.col]="-"
                    self.unique_spaces+=1
            self.path.append([self.row, self.col, self.dir ])
            self.row=new_row
            self.col=new_col
           
        if self.check_edge(self.row, self.col):
            self.unique_spaces+=1
            if self.dir=="^" or self.dir=="v":
                self.map[self.row][self.col]="|"
            if self.dir=="<" or self.dir==">":
                self.map[self.row][self.col]="-"
            
            self.path.append([self.row, self.col])
            return True
        return False

    def check_edge(self, new_row, new_col):
        if new_row==0 or new_row==len(self.map)-1:
            return True
        if new_col==0 or new_col==len(self.map[0])-1:
            return True
        
        return False
        
    def check_collision(self, new_row, new_col):
        if self.map[new_row][new_col]=="#" or self.map[new_row][new_col]=="O":
            return True
        
        return False
    def check_repath(self):
        #if (self.dir=="^" or self.dir=="v") and self.map[self.row][self.col]=="|":
        #    return True
        #elif(self.dir=="<" or self.dir==">") and self.map[self.row][self.col]=="-":
        #    return True
        #return False
        if [self.row, self.col, self.dir] in self.path:
            return True
        return False
    
    def add_obsticle(self, row, col):
        self.map[row][col]="O"


def read_map(filename):
    f=open(filename)
    map=[]
    for line in f:
        map.append([x for x in line[:-1]])
    return map


def find_guard(map):
    for line_idx, line in enumerate(map):
        if "^" in line:
            return line_idx, line.index("^"), "^"
        if "<" in line:
            return line_idx, line.index("<"), "<"
        if "v" in line:
            return line_idx, line.index("v"), "v"
        if ">" in line:
            return line_idx, line.index(">"), ">"

        
import copy
if __name__ == "__main__":
    map=read_map("day6.txt")
    map_copy=copy.deepcopy(map)
    
    current_row, current_col, current_dir=find_guard(map)
    g=guard(map_copy, current_row, current_col, current_dir)
    at_edge=False
    while not at_edge:
        at_edge=g.move()
    print(g.map)
    print(g.unique_spaces)
    print(g.path)
    path=g.path.copy()
    num_blocked=0
    list_obsticles=[]
    for step in path:
        if [step[0],step[1]] in list_obsticles:
            continue
        map_copy=copy.deepcopy(map)
        g=guard(map_copy, current_row, current_col, current_dir)
        g.add_obsticle(step[0], step[1])
        at_edge=False
        blocked=False
        while not at_edge and not blocked:
            if g.check_repath():
                print(f"obsticle at {step[0]},{step[1]}")
                list_obsticles.append([step[0],step[1]])
                blocked=True
                num_blocked+=1
            at_edge=g.move()
        
            
    print(num_blocked)
    
    #obstacle must be placed somewhere on the path
    #use the -|+ to find if the place and direction has been trecked before, if it has loop is found


    #test_obsticles=[
    #    6,3
    #    7,6
    #    7,7
    #    8,1
    #    8,3
    #    9,7
    #]



    
