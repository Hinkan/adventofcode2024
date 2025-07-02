from day1_a import read_lists

def similiarity_score(list1, list2):
    similiarity_score_sum=0
    for value in list1:
        occurances=list2.count(value)
        similiarity_score_sum=similiarity_score_sum+value*occurances
    return similiarity_score_sum
if __name__=="__main__":
    filename="day1.txt"
    list1, list2=read_lists(filename)

    #Typecast to int
    list1=[int(x) for x in list1]
    list2=[int(x) for x in list2]
    
    similarity=similiarity_score(list1, list2)

    print(similarity)