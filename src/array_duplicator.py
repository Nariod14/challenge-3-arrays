def findDuplicates(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be an array of numbers and/or a strings")
    
    if not elemChecker(arr):
        raise ValueError("Input must be a list of numbers and/or a strings")
        
    result = []
    for num in arr:
        if arr.count(num) > 1:
            result.append(num)

    return list(set(result))



def removeDuplicates(arr):
    
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not elemChecker(arr):
        raise ValueError("Input must be a list of numbers and/or a strings")
    
    result = []
    for elem in arr:
        if elem not in result:
            result.append(elem)
            
    return result




def countOccurrences(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not elemChecker(arr):
        raise ValueError("Input must be a list of numbers and/or a strings")
    
    result = {}
    for num in arr:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    return result


def elemChecker(arr):
    for elem in arr:
        if not isinstance(elem, (int, str, float)):
            return False
    return True

    
