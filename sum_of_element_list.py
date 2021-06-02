def sum_of_ele(ele_list):
    #method1 - using built in function
    #return sum(ele_list)
    #method 2 - using for loop
    total=0
    for i in range(len(ele_list)):
        total+=ele_list[i]
    return total


ele_list=list(map(int,input("Please enter the numbers seperated by a + symbol to find the sum of the numbers:\n").split("+")))
print(sum_of_ele(ele_list))
