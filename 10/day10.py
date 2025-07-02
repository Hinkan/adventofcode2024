import itertools

def read_map(filename):
    f=open(filename)
    map=[]
    for line in f:
        map.append([int(x) for x in line[:-1]])
    return map

def find_trailheads(map):
    cords=[]
    for row_idx, row in enumerate(map):
        for col_idx, value in enumerate(row):
            if value==0:
                cords.append([row_idx, col_idx])
    return cords


def check_edge(map, new_row, new_col):
    if new_row==0 or new_row==len(map)-1:
        return True
    if new_col==0 or new_col==len(map[0])-1:
        return True
    return False

def next_treck(map, row, col, height, peaks_reached, peakheight=9):
    if map[row][col]==peakheight:
        peaks_reached.append([row, col])
    else:
        max_row=len(map)
        max_col=len(map[0])

        if row+1<max_row:
            if map[row+1][col]==height:
                next_treck(map, row+1, col, height+1, peaks_reached)
        if row-1>=0:
            if map[row-1][col]==height:    
                next_treck(map, row-1, col, height+1, peaks_reached)
        if col+1<max_col:
            if map[row][col+1]==height:    
                next_treck(map, row, col+1, height+1, peaks_reached)   
        if col-1>=0:
            if map[row][col-1]==height:
                next_treck(map, row, col-1, height+1, peaks_reached)
    

def remove_duplicate_peaks(peaklist):
    peaklist.sort()
    return(list(k for k, _ in itertools.groupby(peaklist)))
        

if __name__ == "__main__":
    filename="day10.txt"
    map=read_map(filename)
    trailheads=find_trailheads(map)
    #print(map)
    #print(trailheads)
    peaks_reached_list=[]
    sum_peaks=0
    for head in trailheads:
        peaks_reached=[]
        next_treck(map, head[0], head[1],1, peaks_reached)
        unique_peaks=remove_duplicate_peaks(peaks_reached)
        peaks_reached_list.append(unique_peaks)
        sum_peaks+=len(peaks_reached)
    #print(peaks_reached_list)

    #for head, peak in zip(trailheads, peaks_reached_list):
    #    print(f'trailhead cords{head}\t peaks{peak}')
    print(f'total peaks:{sum_peaks}')