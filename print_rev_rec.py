def rev_rec(string_rev):
    not_list=[' ', '#','.']
    if(len(string_rev)>0):
        if(string_rev[-1] not in not_list):
            print(string_rev[-1])
        string_rev1=string_rev.rstrip(string_rev[-1])
        rev_rec(string_rev1)    


string_rev=input("Please enter the string you want to reverse \n")
rev_rec(string_rev)