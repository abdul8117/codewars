def comp(array1, array2):
    if array1 == None or array2 == None:
        return False

    a = []
    [a.append(x) for x in sorted(array1) if x not in a]

    b = []
    [b.append(x) for x in sorted(array2) if x not in b]

    
    # square every element in array1
    a = [x**2 for x in a]
    
    return a == b

