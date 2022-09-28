"""
    Given two array of numbers find if any of the elements of one array are in the second array

    e.g.
    case 1:
        ['a','b','c','d']
        ['z','x','c']
        return true
    case 2:
        ['a','b','c','d']
        ['z','x','y']
        return false     

"""
def findCommonNumbers1(array_1, array_2):
    """
    First approach to find if the element from the first array, exists in the second array
    This approach uses a brute force wayt to obtain the result. This means that the 
    Big O notation would be O(n^2) because there are 2 loops nested
    Args:
        array_1 (_type_): first array with numbers
        array_2 (_type_): Second array with numbers

    Returns:
        _type_: boolean
    """
    for i in range(len(array_1) ):    
        for j in range(len(array_2)):
            if array_1[i] == array_2[j]:
                return True
    
    return False

def findCommonNumbers2(array_1, array_2):
    """
    First approach to find if the element from the first array, exists in the second array
    This approach use one data Structure, Hash map or Dictionary in python, to store the values and validate in the second loop
    if that values exist in the structure
    Big O notation would be O(n). Spleating the loops reduce the time complexity
    Args:
        array_1 (_type_): _description_
        array_2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    obj = {}
    
    for i in range(len(array_1)):
        if not array_1[i] in obj:
            obj[array_1[i]] = True

    
    for i in range(len(array_2)):
        if array_2[i] in obj:
            return True

    return False

def main():
    array_1 = ['a','b','c','d']
    array_2 = ['z','x','c']

    # print(findCommonNumbers1(array_1=array_1, array_2=array_2))
    print(findCommonNumbers2(array_1=array_1, array_2=array_2))

if __name__ == '__main__':
    main()