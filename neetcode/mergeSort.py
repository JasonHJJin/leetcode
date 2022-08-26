def mergesort(array):

    arr_len = len(array)

    if arr_len == 1:
        return array

    mid_point = arr_len // 2

    a = mergesort(array[:mid_point])
    b = mergesort(array[mid_point:])

    return merge(a, b)

def merge(arr1, arr2):

    output = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            output.append(arr1[i])
            i += 1
        
        else:
            output.append(arr2[j])
            j += 1
    
    output.extend(arr1[i:])
    output.extend(arr2[j:])

    return output


array = [10, 5, 7, 3, 2, 6]
arr1 = [5, 7]
arr2 = [2, 3, 10, 6]
print(mergesort(array))
print(merge(arr1, arr2))