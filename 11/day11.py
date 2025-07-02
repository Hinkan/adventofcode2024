
def read_stones(filename):
    f=open(filename)
    stones=[]
    for line in f:
        stones=[int(x) for x in line.split()]
    return stones



def apply_rule(stone):
    temp=str(stone)
    if stone==0:
        stone=1
        return [stone]
        
    elif not len(temp)%2:
        
        s1=""
        s2=""
        for i in range(len(temp)):
            if i< len(temp)/2:
                s1+=temp[i]
            else:
                s2+=temp[i]
        return [int(s1), int(s2)]
    else:
        return [stone*2024]
            

from collections import defaultdict

def oneblink(stones):
    newstones=[]
    for stone in stones:
            newstone=apply_rule(stone)
            for i in newstone:
                newstones.append(i)
    return newstones

def process_input(filename):
    """Acquire input data"""
    with open(filename) as file:
        input = file.read().splitlines()

    stones = defaultdict(int)
    for stone in input[0].split():
        stone = int(stone)
        stones[stone] += 1

    return stones     

def blink():
    stonework = dict(stones)
    for stone, count in stonework.items():
        if count == 0: continue
        if stone == 0:
            stones[1] += count
            stones[0] -= count
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            new_len = int(len(stone_str) / 2)
            stone_1 = int(stone_str[:new_len])
            stone_2 = int(stone_str[new_len:])
            stones[stone_1] += count
            stones[stone_2] += count
            stones[stone] -= count
        else:
            stones[stone * 2024] += count
            stones[stone] -= count
    return


def blink_times(blinks):
    for i in range(blinks):
        blink()
        print(i,len(stones))
    return 
if __name__ == "__main__":
    #the idea is to just count instances not individual stones etc, order is not important
    #        20             20:1
    #       2   0           2:1, 0:1
    #    2048     1         2048:1, 1:1
    #  20   48     2048     20:1, 48:1, 2048:1
    # 2 0  4  8   20  48    2:1 0:1, 4:1, 8:1, 20:1, 48:1
    #4048 1 8096 16172 2 0 4 8 



    #failed on part 2 https://www.reddit.com/r/adventofcode/comments/1hbm0al/comment/m1hmola/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    #maxblink=75
    #filename="day11.txt"
    #stones=read_stones(filename)
    #print(stones)
    #stones=[20]
    #for blink in range(maxblink):
    #    stones=oneblink(stones)
    #    print(stones)
    







#-----------------------------------------------------------------------------------------

    filename = 'day11.txt'
    #filename = 'sample.txt'

    stones = process_input(filename)

    blink_times(75)

    print()
    print('Stones =', sum(stones.values()))

        