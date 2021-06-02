def list_rev(a):
    temp = a[0]
    a[0] = a[-1]
    a[-1] = temp
    return a

input_list=list(input("Please enter the list"))
output_list=list_rev(input_list)
print(output_list)