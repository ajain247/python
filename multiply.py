#import numpy
from functools import reduce
def prod_of_ele(ele_list):

    #method - traversal
    """
    total=1
    for i in range(len(ele_list)):
        total*=ele_list[i]
    return total
    """
    #method2 - numpy
    """
    return numpy.prod(ele_list)
    """
    #method3- lambda and reduce

    return reduce((lambda x,y:x*y),ele_list)



ele_list=list(map(int,input("Please enter the numbers seperated by a * symbol to find the product of the numbers:\n").split("*")))
print(prod_of_ele(ele_list))