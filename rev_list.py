def rev_list(list_element):
    #method 1 - reversed()
    #return [element for element in reversed(list_element)]

    #method 2 - reverse() without creating another list
    #list_element.reverse()
    #return list_element

    #method3 - slicing
    new_list=list_element[::-1]
    return new_list

list_element=list(map(int,input("Please insert the elements of a list seperated with spaces:\n").split(" ")))
print(rev_list(list_element))
