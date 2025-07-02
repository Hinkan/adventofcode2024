import itertools
import copy

#TODO probably because of ids longer than 1 integer fucks up when dping the string stuff
def read_file(filename):
    f=open(filename)
    string=""
    for line in f:
        string=line[:-1]
    return string

def to_verbose(disc_string):
    verbose_list=[]
    for i in range(int(len(disc_string)/2)):
        files=disc_string[i*2]
        empties=disc_string[i*2+1]
        
        for f in range(int(files)):
            verbose_list.append(i)
        
        for e in range(int(empties)):
            verbose_list+=str(".")
        
    return verbose_list

def hardcode(verbose_list):
    #num_operations=verbose_string.count(".")
    charlist=verbose_list
    j=len(verbose_list)-1
    for i in range(len(verbose_list)):
        if charlist[i]==".":
            while charlist[j]==".":
                j-=1
                if j<=i:
                    break
            charlist[i]=charlist[j]
            charlist[j]='.'
            j-=1
        if j<=i:
            break
    return charlist

def move_wholefiles(verbose_list):
    j=len(verbose_list)-1
    while j >0:
        if verbose_list[j]!=".":
            fileblock=[verbose_list[j]]
            j-=1
            while verbose_list[j]!="." and verbose_list[j]in fileblock :#find length of a block
                fileblock.append(verbose_list[j])
                j-=1
            moved=False
            i=0
            while i<j and not moved:
                empty_indx=[]
                if verbose_list[i]==".":
                    while verbose_list[i]==".":
                        empty_indx.append(i)
                        i+=1
                else:
                    i+=1
                if len(empty_indx)>=len(fileblock):
                    
                    for idx, k in enumerate(fileblock):
                        verbose_list[empty_indx[idx]]=k
                        verbose_list[j+idx+1]="."
                    
                    moved=True
        else:
            j-=1
    return verbose_list

if __name__ == "__main__":
    filename="day9.txt"
    disc_string=read_file(filename)
    if len(disc_string)%2:#ad trailing zero
        disc_string+=str(0)
    print(disc_string)
    verbose_list=to_verbose(disc_string)
    print(verbose_list)
    #sortedlist=hardcode(verbose_list)
    sortedlist=move_wholefiles(verbose_list)
    print(sortedlist)
    checksum=0
    for idx, value in enumerate(sortedlist):
        if value!=".":
            
            checksum+=idx*int(value)
        
    print(checksum)
    print(len(verbose_list))
    print(len(sortedlist))
    print(verbose_list.count("."))
    print(sortedlist.count("."))
