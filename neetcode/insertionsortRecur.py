def insertRecur(list, n):

    if n <= 1:
        return

    insertRecur(list, n-1)

    lastItem = list[n-1]

    j = n - 2

    while j >= 0 and list[j] > lastItem:

        list[j+1] = list[j]
        j -= 1       

    list[j+1]  = lastItem




list = [5, 4, 3, 2, 1]
n  = len(list)
insertRecur(list, n)
output = []
for i in list:
    output.append(i)

print(output)
