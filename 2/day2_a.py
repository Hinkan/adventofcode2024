
def read_safetyreports(filename):
    f= open(filename)
    list1=[]
    for line in f:
        split=line.split()
        split_int=[int(x)for x in split]
        list1.append(split_int)
    f.close()
    return list1



def check_safety(reportlist):
    last_level=reportlist[0]#first value
    last_leveldifference=0#first derivate
    for level in reportlist[1:]:

        leveldifference=level-last_level#positvie=increasing, negative =decreasing
        if leveldifference==0 or leveldifference<-3 or leveldifference>3:#within safe differences
            return False
        if leveldifference*last_leveldifference<0:#check for switching sign of  derivate
            return False
        

        last_level=level
        last_leveldifference=leveldifference
    
    return True
    
def safety_dampener(reportlist):
    for idx in range(len(reportlist)):
        pruned_list=reportlist.copy()
        pruned_list.pop(idx)
        if check_safety(pruned_list):
            return True
    return False
 
if __name__=="__main__":
    filename="day2.txt"

    lists=read_safetyreports(filename)
    #lists=[[1,2,3,2,5,6]]
    safecounter=0
    for safetyreport in lists:
        if check_safety(safetyreport):
            safecounter+=1
        else:
            if safety_dampener(safetyreport):
                safecounter+=1

    print(safecounter)
