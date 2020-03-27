a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def common(lst1,lst2):
    return list(set(lst1) & set(lst2))

e = common(a,b)
print(e)
    
