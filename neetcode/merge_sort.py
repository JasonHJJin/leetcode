from mergeSort import merge


def merge_sort(arr):

    arr_len = len(arr)

    if arr_len == 1:
        return arr

    mid_point = arr_len // 2

    a = merge_sort(arr[:mid_point])
    b = merge_sort(arr[mid_point:])

    return merge(a,b)

def merge(arr1, arr2):

    output = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            output.append(arr1[i])
            i += 1
        else:
            output.append(arr2[i])
            j += 1

    output.extend(arr1[i:])
    output.extend(arr2[j:])

    return output


if __name__ == '__main__':

    print(merge_sort([3,2,5,1,6,7]))

    