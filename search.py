# 1、顺序查找    无序查找    O(n)
'''
从第一个元素m开始逐个与需要查找的元素x进行比较，当比较到元素值相同(即m=x)时返回元素m的下标，
如果比较到最后都没有找到，则返回-1。
'''


def sequential_search(lst, key):
    length = len(lst)
    for i in range(length):
        if lst[i] == key:
            return i
        else:
            return False


# 2、二分查找    有序查找    O(log2**n)
'''
1、确定该期间的中间位置K
2、将查找的值T与array[k]比较。若相等，查找成功返回此位置；否则确定新的查找区域，继续二分查找。
'''


def binary_search1(lst, t):
    length = len(lst)
    start = 0
    end = length - 1

    while start <= end:
        mid = (start + end) // 2
        if t == lst[mid]:
            return 'lst:index{}'.format(mid)
        elif t < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


def binary_search(lst, t):
    length = len(lst)
    if length == 0:
        return False
    mid = length // 2
    if t == lst[mid]:
        return True
    elif t < lst[mid]:
        return binary_search(lst[:mid],t)
    else:
        return binary_search(lst[mid+1:],t)


# 3、插值查找    有序查找    O(n)
'''
插值查找是根据要查找的关键字key与查找表中最大最小记录的关键字比较后的 查找方法，
其核心就在于插值的计算公式 (key-a[low])/(a[high]-a[low])*(high-low)。
'''


def interpolation_search(lst, key):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = start + int((end - start) * (key - lst[start]) / (lst[end] - lst[start]))
        if key == lst[mid]:
            return f'lst:index:{mid}'
        elif key < mid:
            end = mid - 1
        else:
            start = mid + 1
    return False


# 4、斐波那契查找  有序数列    O(log2n)


if __name__ == '__main__':
    list1 = [2, 4, 5, 8, 10, 20, 26, 30]
    # print(interpolation_search(list1, 8))
