def chocolate_dist(age_list):
    age_list.sort(reverse=True)
    #print(age_list)
    length=len(age_list)
    count_arr=[]
    #print(age_list)
    #print(length)
    for i in range(length):
        if(i==0):
            count_arr.append(1)
            continue
        if(age_list[i]==age_list[i-1]):
            count_arr.append(count_arr[i-1])
        else:
            count_arr.append(count_arr[i-1]+1)
        #print(count_arr)       
    print(sum(count_arr))

age_list=list(map(int,input("Please enter the age of children:\n").split(",")))
chocolate_dist(age_list)