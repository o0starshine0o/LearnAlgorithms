import sys
import unittest


def merge(a, p, q, r):
    """ an assist function to merge two array that has been sorted

    :param a: a array to sort
    :param p: index of array, p <= q < r, A[p..q] and A[q+1..r] has been sorted
    :param q: index of array, p <= q < r, A[p..q] and A[q+1..r] has been sorted
    :param r: index of array, p <= q < r, A[p..q] and A[q+1..r] has been sorted
    """
    print('merge array', a, 'with p(%d) q(%d) r(%d)' % (p, q, r))
    # step 1 : get two sorted array
    left = a[p:q + 1]
    right = a[q + 1:r + 1]
    # step 2 : insert a max value as sentry
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    # step 3 : from p to r, merge array
    left_index = 0
    right_index = 0
    for index in range(p, r + 1):
        if left[left_index] <= right[right_index]:
            a[index] = left[left_index]
            left_index += 1
        else:
            a[index] = right[right_index]
            right_index += 1
    print('merge array result', a)
    return a


def merge_sort(a, p, r):
    """ merge sort

    :param a: a array to sort, a[p:r+1] need to be sorted
    :param p: index of array, p < r, if p >= r , the length of a is 1, return
    :param r: index of array, p < r, if p >= r , the length of a is 1, return
    """
    if p < r:
        q = int((p + r) / 2)
        # divider
        a = merge_sort(a, p, q)
        a = merge_sort(a, q + 1, r)
        # conquer
        merge(a, p, q, r)
    return a


if __name__ == '__main__':
    array = [2, 5, 6, 1, 3, 4, 8, 7]
    print('origin array : ', array)
    print('sorted array : ', merge_sort(array, 0, len(array) - 1))


class FunctionTest(unittest.TestCase):
    def test_merge(self):
        a = [9, 2, 5, 6, 1, 3, 4, 8, 7]
        self.assertEqual([9, 1, 2, 3, 4, 5, 6, 8, 7], merge(a, 1, 3, 6))
