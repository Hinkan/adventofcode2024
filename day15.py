
class Robot():
    def __init__(self, row, col, map):
        self.row=row
        self.col=col
        self.map=map
    
    def move(self, char):
        self.map[int(self.row)][int(self.col)]="."
        if char=="^":
            self.row=self.row-1
        elif char=="<":
            self.col=self.col-1
        elif char=="v":
            self.row+=1
        elif char==">":
            self.col+=1
        else:
            print("invalid movement")
        map[int(self.row)][int(self.col)]="@"
    
    def next_tile(self, row, col, direction):
        if direction=="^":
            row=row-1
        elif direction=="<":
            col=col-1
        elif direction=="v":
            row+=1
        elif direction==">":
            col+=1
        else:
            print("invalid movement")
        return row, col


    def check_next(self, row, col, direction):
        if map[row][col]=="O":
            row, col= self.next_tile(row, col, direction)
            returnvalue=self.check_next(row, col, direction)
            if returnvalue==True:
                map[row][col]="O"
                return True
        elif map[row][col]=="[" or map[row][col]=="]":
            row, col= self.next_tile(row, col, direction)
            returnvalue=self.check_next(row, col, direction)
            if returnvalue==True:
                map[row][col]="O"
                return True
        elif map[row][col]=="#":
            return False
        elif map[row][col]==".":
            return True
        else:
            print("unknown mapitem")




class Box():
    def __init__(self,map, row, col1, col2):
        self.map=map
        self.row=row
        self.col1=col1
        self.col2=col2

    def get(self):
        return self.row, self.col1, self.col2
    
    def move_row(self, direction):
        self.row=row+direction*1
    
    def move_col(self, direction):
        self.col1=self.col1+direction*1
        self.col2=self.col2+direction*1
    
    def move(self, char):
        self.map[int(self.row)][int(self.col)]="."
        if char=="^":
            self.row=self.row-1
        elif char=="<":
            self.col=self.col-1
        elif char=="v":
            self.row+=1
        elif char==">":
            self.col+=1
        else:
            print("invalid movement")
        map[int(self.row)][int(self.col)]="@"


    def check_next(self, char, list_movables):
        if map[row][col]=="[" or map[row][col]=="]":
            row, col= self.next_tile(row, col, char)
            returnvalue=self.check_next(row, col, char)
            if returnvalue==True:
                list_movables.append(self)
                return True
        elif map[row][col]=="#":
            return False
        elif map[row][col]==".":
            return True
        else:
            print("unknown mapitem")





def read_map(filename):
    f=open(filename)
    map=[]
    instructions=""
    mapdone=False
    for line in f:
        if mapdone==False:
            map.append([x for x in line[:-1]])
        else:
            instructions+=line
        if len(line)==1:
            mapdone=True
    return map, instructions
    


def find_cords(map):
    boxes=[]
    walls=[]
    robot=[]
    for row, line in enumerate(map):
        for col, value in enumerate(line):
            if value=="#":
                walls.append([row, col])
            elif value=="O":
                boxes.append([row, col])
            elif value=="[":
                boxes.append([[row, col],[row, col+1]])
            elif value=="@":
                robot=[row, col]
    return boxes,walls,  robot

def print_map(map):
    for line in map:
        print(line)

def boxat(list_boxes, row_target, col_target):
    for box in list_boxes:

        row, col1, col2=box.get()
        if row_target==row:
            if col_target==col1 or col_target==col2:
                return box
    return None
        


if __name__ == "__main__":
    filename="day15_test2.txt"
    map, instructions=read_map(filename)
    boxes_cords,walls, robotcords= find_cords(map)
    
    
    robot=Robot(robotcords[0], robotcords[1], map)

    list_boxes=[]
    for cords in boxes_cords:
        cord1=cords[0]
        cord2=cords[1]
        if cord1[0]==cord2[1]:
            list_boxes.append(Box(map, cord1[0], cord1[1], cord2[1] ))
        else:
            print("row mismatch")
    
    for instruction in instructions:
        print(instruction)
        row, col=robot.next_tile(robot.row, robot.col, instruction)
        #returnvalue=robot.check_next(row, col, instruction)
        list_movables=[]
        if map[row][col]==".":
            robot.move(instruction)
        
        
        elif map[row][col]=="[" or map[row][col]=="]":
            box=boxat(list_boxes, row, col)
            if box!=None:
                box.check_next(instruction, list_movables)

            


        
        
        
        #print_map(map)

    boxes,walls, robotcords= find_cords(map)
    gps_value=0
    for box in boxes:
        gps_value+=box[0]*100+box[1]
    print(gps_value)