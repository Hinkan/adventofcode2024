def read_map(filename):
    f=open(filename)
    map=[]
    for line in f:
        map.append([x for x in line[:-1]])
    return map

def test_neighbors(map, row, col, cordlist):
    #TODO return the number of neighbors
    row_min=0
    col_min=0
    row_max=len(map)
    col_max=len(map[0])
    num_neighbors=4
    neighbors=0
    crop=map[row][col]
    cordlist.append([row, col])
    if row+1<row_max:
        if [row+1, col] not in cordlist:
            if map[row+1][col]==crop:
                neighbors+=test_neighbors(map, row+1, col, cordlist)
                num_neighbors-=1
        else:
            num_neighbors-=1
    if row-1>=row_min:
        if [row-1, col] not in cordlist:
            if map[row-1][col]==crop:
                neighbors+=test_neighbors(map, row-1, col, cordlist)
                num_neighbors-=1
        else:
            num_neighbors-=1
    if col+1<col_max:
        if [row, col+1] not in cordlist:
            if map[row][col+1]==crop:
                neighbors+=test_neighbors(map, row, col+1, cordlist)
                num_neighbors-=1
        else:
            num_neighbors-=1
    if col-1>=col_min:
        if [row, col-1] not in cordlist:
            if map[row][col-1]==crop:
                neighbors+=test_neighbors(map, row, col-1, cordlist)
                num_neighbors-=1
        else:
            num_neighbors-=1
    return neighbors+num_neighbors
    #return cordlist, neighbors



def make_farmplots(map):
    crops=[]
    plot_cords=[]
    tested_cords=[]#set of plot_cords
    neighbors_list=[]
    for row_idx, row in enumerate(map):
        for col_idx, crop in enumerate(row):
            cordlist=[]
            if [row_idx, col_idx] not in tested_cords:
                
                neighbors=test_neighbors(map, row_idx, col_idx, cordlist)
                plot_cords.append(cordlist)

                tested_cords+=cordlist
                crops.append(crop)
                neighbors_list.append(neighbors)
    return crops, plot_cords, neighbors_list
            



if __name__ == "__main__":
    filename=("day12_test2.txt")
    map=read_map(filename)
    crops, plot_cords, neighbors_list=make_farmplots(map)
    price=0
    for c,p,nl in zip(crops, plot_cords, neighbors_list):
        Area=len(p)
        price+=Area*nl
        #print(c,Area, nl,p)
    print(f'total price:{price}')
