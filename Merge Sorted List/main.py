# Merge Sorted List

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]


def merge():
    listSize1 = len(list1)
    listSize2 = len(list2)
    result = []
    i = 0
    j = 0
    while i < listSize1 and j < listSize2:
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result = result+list1[i:]+list2[j:]
    print("The combined Sorted List :", str(result))


def main():
    merge()


main()
