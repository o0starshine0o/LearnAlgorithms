def insert_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        # insert a[j] into the sorted sequence a[1...j-1]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    return a


def insert_sort_desc(a):
    for j in range(1, len(a)):
        key = a[j]
        # insert a[j] into the sorted sequence a[1...j-1]
        i = j - 1
        while i >= 0 and a[i] < key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    return a


def add_binary(a, b):
    result = []
    extra = 0
    for i in range(len(a) - 1, -2, -1):
        temp = a[i] + b[i] + extra
        extra = 0 if temp / 2 < 0 else 1
        result.insert(0, temp % 2)
    return result


def recursion_insert_sort(a, n):
    """ using recursion to apply insert sort

    :param a: a sorted array from min to max
    :param n: index of a, a[0, n-1] is sorted
    """
    if n > 0:
        # step 1 : get the sorted array
        a = recursion_insert_sort(a, n - 1)
        # step 2 : insert a[n] into a[0, n-1]
        an = a[n]
        i = n - 1
        while i >= 0 and a[i] > an:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = an
    return a


if __name__ == '__main__':
    array = [5, 2, 4, 6, 1, 3]
    print('origin array : ', array)
    print('sorted array : ', insert_sort(array))
    print('sorted array desc: ', insert_sort_desc(array))
    print('recursion_insert_sort: ', recursion_insert_sort(array, len(array) - 1))

    one = [1, 1, 1]
    two = [1, 0, 1]
    print('add binary : ', add_binary(one, two))
