
def distance_between_lists(list1, list2, sort=True):
    returnlist=[]
    if sort==True:
        list1.sort()
        list2.sort()
    
    for l1, l2 in zip(list1, list2):
        diff=l1-l2
        if diff<0:#if negative switch to positive
            diff=diff*-1
        returnlist.append(diff)
    return returnlist

def read_lists(filename):
    f= open(filename)
    list1=[]
    list2=[]
    for line in f:
        split=line.split()
        list1.append(split[0])
        list2.append(split[1])
    f.close()
    return list1, list2
    

if __name__=="__main__":
    filename="day1.txt"
    list1, list2=read_lists(filename)
    #Typecast to int
    list1=[int(x) for x in list1]
    list2=[int(x) for x in list2]
    distances=distance_between_lists(list1, list2, True)
    print(distances)
    print(sum(distances))