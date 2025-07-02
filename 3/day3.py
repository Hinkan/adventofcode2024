import re

def reduce_string(longstring):
    finder=0
    returnstring=""
    dontindex=[]
    doindex=[0]
    while finder != -1:
        finder=longstring.find("don't()", finder)
        dontindex.append(finder)
        finder=longstring.find("do()", finder)
        doindex.append(finder)

    for do in doindex:
        dont=-1
        for donte in dontindex:
            if do-donte<0:
                dont=donte
                break


        returnstring+=longstring[do:dont]
    
    return returnstring


if __name__=="__main__":
    f=open("day3.txt")
    longstring=f.read()
    regex_do="do()"
    regex_dont="don't()"
    #search=re.search(regex_dont, longstring)
    #print(search.start())
    #splitstring=re.split(regex_dont, longstring)
    #shortstring=splitstring[0]
    #for split in splitstring[1:]:
    #    dosplit=re.split(regex_do, split)
    #    if len(dosplit)==3:
    #        shortstring=shortstring+dosplit[2]
    #        print(dosplit)

    reduced_string=reduce_string(longstring=longstring)
    print(f'original legtn{len(longstring)}\t shortended length{len(reduced_string)}')
    found=None        

    indexes_dont=[]
    indexes_do=[0]


    regex='mul\(\d+,\d+\)'
    allmuls=re.findall(regex, reduced_string)
    sum=0
    reg2='\d+'
    for mul in allmuls:
        numbers=re.findall(reg2, mul)
        sum=sum+int(numbers[0])*int(numbers[1])

    print(sum)


