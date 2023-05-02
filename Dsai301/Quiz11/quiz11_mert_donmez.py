#Mert Donmez
#2016203039
def order_control(lst, a, b, c):
    
    if a not in lst or b not in lst or c not in lst:
        return 1
    
    if a in lst:
        a_index = lst.index(a) 

    if b in lst[a_index + 1:]:
        b_index = lst.index(b, a_index + 1) 
    else:
       return 2

    if c not in lst[b_index + 1:]:
        return 3

    return 5
# Example cases
liste = [1, 2, 3, 3, 4, 5, 6, 5]    
print(order_control(liste, 2, 3, 3)) #==5
print(order_control(liste, 2, 3, 2)) #==3
print(order_control(liste, 5, 6, 5)) #==5
print(order_control(liste, 3, 3, 3)) #==3
print(order_control(liste, 2, 3, 8)) #==1
print(order_control(liste, 2, 8, 3)) #==1
print(order_control(liste, 8, 3, 8)) #==1
print(order_control(liste, 4, 5, 6)) #==5