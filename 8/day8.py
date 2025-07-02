import copy
def readmap(filename):
    f=open(filename)
    map=[]
    for line in f:
        map.append([x for x in line[:-1]])
    return map
def find_frequencies(map):
    frequency_list=[]
    for row in map:
        for value in row:
            if value not in frequency_list and value !=".":
                frequency_list.append(value)
    return frequency_list

def find_coordinates(map, freq):
    coordinates=[]
    for row_idx, row in enumerate(map):
        if freq in row:
            col_idxes=find_indices_of_values(row, freq)
            for col_idx in col_idxes:
                coordinates.append([row_idx, col_idx])
    return coordinates
def find_indices_of_values(lst, targets):
    #return [i for i, v in enumerate(lst) if v in targets]
    indexes=[]
    for i,v in enumerate(lst):
        if v in targets:
            indexes.append(i)
    return indexes

def find_antinodes(map, coordinates):
    minrow=0
    mincol=0
    maxrow=len(map)
    maxcol=len(map[0])

    for c1_idx,coordinate1 in enumerate(coordinates[:-1]):
        for coordinate2 in coordinates[c1_idx+1:]:
            distance_row=coordinate1[0]-coordinate2[0]
            distance_col=coordinate1[1]-coordinate2[1]
            newcord1=[coordinate1[0]+distance_row, coordinate1[1]+distance_col]
            newcord2=[coordinate2[0]-distance_row, coordinate2[1]-distance_col]
            if newcord1[0]>=minrow and newcord1[0]<maxrow:
                if newcord1[1]>=mincol and newcord1[1]<maxcol:
                    a=newcord1[0]
                    b=newcord1[1]
                    map[a][b]="#"
            if newcord2[0]>=minrow and newcord2[0]<maxrow:
                if newcord2[1]>=mincol and newcord2[1]<maxcol:
                    map[newcord2[0]][newcord2[1]]="#"
            print(f"row={newcord1[0]}, col={newcord1[1]}")
            print(f"row={newcord2[0]}, col={newcord2[1]}")
            print(map)
    return map

def coords_within(row, col, row_min, row_max, col_min, col_max):
    if row>=row_min and row<row_max:
        if col>=col_min and col<col_max:
            return True
    return False
def find_antinodes_harmonics(map, coordinates):
    minrow=0
    mincol=0
    maxrow=len(map)
    maxcol=len(map[0])

    for c1_idx,coordinate1 in enumerate(coordinates[:-1]):
        for coordinate2 in coordinates[c1_idx+1:]:
            distance_row=coordinate1[0]-coordinate2[0]
            distance_col=coordinate1[1]-coordinate2[1]
            start_row=coordinate1[0]
            start_col=coordinate1[1]
            map[start_row][start_col]="#"
            row=start_row+distance_row
            col=start_col+distance_col
            while coords_within(row, col, minrow, maxrow, mincol, maxcol):
                map[row][col]="#"
                row=row+distance_row
                col=col+distance_col
            row=start_row-distance_row
            col=start_col-distance_col
            while coords_within(row, col, minrow, maxrow, mincol, maxcol):
                map[row][col]="#"
                row=row-distance_row
                col=col-distance_col

    return map
if __name__ == "__main__":
    filename="day8.txt"
    map=readmap(filename)
    map_nodes=readmap(filename)

    print(map)
    frequency_list=find_frequencies(map)
    print(frequency_list)

    for freq in frequency_list:
        list_coordinates=find_coordinates(map, freq)
        print(list_coordinates)
        map_nodes=find_antinodes_harmonics(map_nodes, list_coordinates)

        
    print(map_nodes)
    sum_anitnodes=0
    for row in map_nodes:
        sum_anitnodes+=row.count("#")
    print(sum_anitnodes)
