import re

def importmatrix(filename):
    f=open(filename)
    xmas_matrix=[]
    for line in f:
        xmas_matrix.append(line[:-1])
    f.close()
    return xmas_matrix



def make_columns(xmas_matrix):
    cols=[]
    for col in xmas_matrix[0][:]:
        cols.append(col)
    for line in xmas_matrix[1:]:
        for idx, value in enumerate(line[:]):#skips newline
            cols[idx]+=value
    return cols

def make_diagonal(xmas_matrix, flip=False):
    #diag=[]#len(cols)+len(row)-1
    #for row in xmas_matrix:
    #    diag.append(row[0])
    #for value in xmas_matrix[-1][1:]:
    #    diag.append(value)
    #for idx
    if flip:
        xmas_matrix.reverse()
    diag=[None]*((len(xmas_matrix)+len(xmas_matrix[0]))-1)#len(cols)+len(row)-1
    for i in range(len(diag)):
        for idx_row,row in enumerate(xmas_matrix):
            for idx_col, value in enumerate(row):
                if idx_row+idx_col==i:
                    if diag[i]==None:
                        diag[i]=value
                    else:
                        diag[i]+=value


    return diag

def counxmas_strings(xmas_matrix):
    xmas_rows=xmas_matrix.copy()
    xmas_cols=make_columns(xmas_matrix)
    xmas_diag=make_diagonal(xmas_matrix, False)
    xmas_diag2=make_diagonal(xmas_matrix, True)

    counts=[]

    count1=0
    count2=0
    for x in xmas_rows:
        count1+=len(re.findall('XMAS', x))
        count2+=len(re.findall('SAMX', x))
    counts.append(count1)
    counts.append(count2)
    count1=0
    count2=0
    for x in xmas_cols:
        count1+=len(re.findall('XMAS', x))
        count2+=len(re.findall('SAMX', x))
    counts.append(count1)
    counts.append(count2)
    count1=0
    count2=0
    for x in xmas_diag:
        count1+=len(re.findall('XMAS', x))
        count2+=len(re.findall('SAMX', x))
    counts.append(count1)
    counts.append(count2)
    count1=0
    count2=0
    for x in xmas_diag2:
        count1+=len(re.findall('XMAS', x))
        count2+=len(re.findall('SAMX', x))
    counts.append(count1)
    counts.append(count2)
    return counts

def find_horisontal(xmas_matrix, row, col, pos=True):
    sign=1
    if pos==False:
        sign=-1
    try:
        if xmas_matrix[row][col+1*sign]=='M':
            if xmas_matrix[row][col+2*sign]=='A':
                if xmas_matrix[row][col+3*sign]=='S':
                    if xmas_matrix[row][col]+xmas_matrix[row][col+1*sign]+xmas_matrix[row][col+2*sign]+xmas_matrix[row][col+3*sign]=='XMAS':
                        return 1
        return 0
    except:
        return 0
    
def find_vertical(xmas_matrix, row, col, pos=True):
    sign=1
    if pos==False:
        sign=-1
    try:
        if xmas_matrix[row+1*sign][col]=='M':
            if xmas_matrix[row+2*sign][col]=='A':
                if xmas_matrix[row+3*sign][col]=='S':
                    return 1   
        return 0
    except:
        return 0


def find_diag(xmas_matrix, row, col, pos_row=True, pos_col=True):
    sign_row=1
    sign_col=1
    if pos_row==False:
        sign_row=-1
    if pos_col==False:
        sign_col=-1
    try:
        if xmas_matrix[row+1*sign_row][col+1*sign_col]=='M':
            if xmas_matrix[row+2*sign_row][col+2*sign_col]=='A':
                if xmas_matrix[row+3*sign_row][col+3*sign_col]=='S':
                    if(xmas_matrix[row][col]+xmas_matrix[row+1*sign_row][col+1*sign_col] +xmas_matrix[row+2*sign_row][col+2*sign_col] +xmas_matrix[row+3*sign_row][col+3*sign_col])=="XMAS":
                        return 1
        return 0
    except:
        return 0


def count_xmas(xmas_matrix):
    count=0
    count_vertical1=[]
    count_vertical2=[]
    count_horisontal1=[]
    count_horisontal2=[]
    count_diag1=[]
    count_diag2=[]
    count_diag3=[]
    count_diag4=[]
    for rowidx,row in enumerate(xmas_matrix):
        for colidx,value in enumerate(row):
            if value=='X':
                
                count+=find_horisontal(xmas_matrix, rowidx, colidx, True)#left to right
                count+=find_horisontal(xmas_matrix, rowidx, colidx, False)#right to left
                count+=find_vertical(xmas_matrix, rowidx, colidx, True)#down
                count+=find_vertical(xmas_matrix, rowidx, colidx, False)#up
                count+=find_diag(xmas_matrix, rowidx, colidx, True, True)#left to right, down
                count+=find_diag(xmas_matrix, rowidx, colidx, True, False)#left to right, up
                count+=find_diag(xmas_matrix, rowidx, colidx, False, True)#right to left, down
                count+=find_diag(xmas_matrix, rowidx, colidx, False, False)#right to left, up

                
                count_vertical1.append(find_vertical(xmas_matrix, rowidx, colidx, True))
                count_vertical2.append(find_vertical(xmas_matrix, rowidx, colidx, False))
                count_horisontal1.append(find_horisontal(xmas_matrix, rowidx, colidx, True))
                count_horisontal2.append(find_horisontal(xmas_matrix, rowidx, colidx, False))
                count_diag1.append(find_diag(xmas_matrix, rowidx, colidx, True, True))
                count_diag2.append(find_diag(xmas_matrix, rowidx, colidx, True, False))
                count_diag3.append(find_diag(xmas_matrix, rowidx, colidx, False, True))
                count_diag4.append(find_diag(xmas_matrix, rowidx, colidx, False, False))
    print(sum(count_vertical1))
    print(sum(count_vertical2))
    print(sum(count_horisontal1))
    print(sum(count_horisontal2))
    print(sum(count_diag1))
    print(sum(count_diag2))
    print(sum(count_diag3))
    print(sum(count_diag4))
    return count

def find_masx(xmas_matrix):
    count=0
    for row in range(1,len(xmas_matrix)-1):
        for col in range(1,len(xmas_matrix[0])-1):
            value=xmas_matrix[row][col]
            sucesses=0
            if value=='A':
                if xmas_matrix[row-1][col-1]=='M' and xmas_matrix[row+1][col+1]=='S':
                    sucesses+=1
                if xmas_matrix[row+1][col+1]=='M' and xmas_matrix[row-1][col-1]=='S':
                    sucesses+=1
                if xmas_matrix[row+1][col-1]=='M' and xmas_matrix[row-1][col+1]=='S':
                    sucesses+=1
                if xmas_matrix[row-1][col+1]=='M' and xmas_matrix[row+1][col-1]=='S':
                    sucesses+=1
            if sucesses==2:
                count+=1
    return count




if __name__=='__main__':
    xmas_matrix=importmatrix("day4.txt")
    #xmas_matrix=importmatrix("test.txt")
    counts=find_masx(xmas_matrix)


    print(counts)
    
    



