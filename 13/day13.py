import re


def read_instruction(filename):
    f=open(filename)
    instructions=[]
    machine=[]
    for line in f:
        if line=="\n":
            instructions.append(machine)
            machine=[]
        else:
            machine.append(line)
    instructions.append(machine)
    return instructions

def extract_values(isntruction):
    ButtonA=isntruction[0]
    ButtonB=instruction[1]
    Prize=instruction[2]
    A=re.findall('\d+', ButtonA)
    B=re.findall('\d+', ButtonB)
    P=re.findall('\d+', Prize)
    return A,B,P
    

def find_combinations(value1, value2, target):
    combination_list=[]
    a=0
    while a<100:
        b=0
        while b<100 and value1*a+value2*b<target:
            b+=1
        
            if value1*a+value2*b==target:
                combination_list.append([a,b])
        a+=1
    return combination_list

def find_minimum(AB_presses, A_prize=3, B_prize=1, max_press=100):
    minimum=(A_prize+B_prize)*max_press
    minimum_press=[]
    for ab in AB_presses:
        cost=ab[0]*A_prize+ab[1]*B_prize
        if cost<minimum:
            minimum=cost
            minimum_press=ab
    return minimum_press, minimum


if __name__ == "__main__":
    filename="day13.txt"
    instructions=read_instruction(filename)
    sum_prize=0
    for instruction in instructions:
        A,B,P=extract_values(instruction)
        #print(A,B,P)
        x_combinations=find_combinations(int(A[0]),int(B[0]), int(P[0])) 
        #print(x_combinations)
        y_combinations=find_combinations(int(A[1]),int(B[1]), int(P[1]))
        #print(y_combinations)
        common=[]
        for xcomb in x_combinations:
            if xcomb in y_combinations:
                common.append(xcomb)
        minimal_press, minimum=find_minimum(common)
        
        if len(minimal_press)>0:
            print(minimal_press, minimum)
            sum_prize+=minimum
        
    print(sum_prize)

