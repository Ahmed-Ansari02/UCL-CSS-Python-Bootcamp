import copy
lst = [[1,2,3],[1,2,3],[1,2,3]]
def fun(a):
    l = a
    l[0].append(4)
    

print(lst)
fun(lst)
print(lst)