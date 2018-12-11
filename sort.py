list1 = [7, 6, 2, 3, 9, 4, 8, 5, 1, 1, 1, 5]
'''1、插入排序
从左边第二个数开始，依次与前面的数相比较，直到找到一个比他小的数为止，插入到那里
时间复杂度：平均O(n^2)   最好：O(n)    最坏O(n^2)
稳定性：稳定
'''


def insert_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        index = i
        while index>0 and list[index-1]>temp:
            list[index] = list[index-1]
            index -= 1
        list[index] = temp
    print(list)


'''2、冒泡排序
从左到右，两两依次比较，如果大小顺序不对，则交换两数，
一次遍历把最后把大的数放到尾部之后，
对前面的数字继续进行遍历
'''


def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j]> list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    print(list)


'''3、选择排序
1、先把  第一个值赋给min， 让min和后边其余的值进行比较，若有小于min的值，则替换，最后把最小的值赋给第一个值
2、向后循环，以此类推
时间复杂度：平均O(n^2)
稳定性：不稳定
'''


def select_sort(list):
    for i in range(len(list)-1):
        index_min = list[i]
        for j in range(i+1, len(list)):
            if list[j]< index_min:
                list[j], index_min = index_min,list[j]
        list[i] = index_min
    print(list)


'''4、快速排序
先从数列中取出一个数作为基准数，
将比这个数大的数全部放到它的右边，小于或等于他的数放到左边
再对左右区间重复第二步，直到各区间只有一个数
'''


# quick_sort = lambda array: array if len(array) <= 1 else quit_sort([item for item in array[1:] if item < array[0]]) + [array[0]] + quit_sort([item for item in array[1:] if item > array[0]])


def quick_sort1(list):
    if len(list) <= 1:
        return list
    mid_index = len(list)//2
    mid_num = list.pop(mid_index)
    left_list = []
    mid_list = [mid_num]
    right_list =[]
    for i in list:
        if i <=mid_num:
            left_list.append(i)
        else:
            right_list.append(i)
    return quick_sort1(left_list)+mid_list+quick_sort1(right_list)


def quick_sort2(li, low, high):
    i = low
    j = high
    if i >= j:
        return li
    key = li[i]
    while i < j:
        while i < j and li[j] >= key:
            j -= 1
        li[i] = li[j]
        while i < j and li[i] <= key:
            i += 1
        li[j] = li[i]
    li[i] = key
    quick_sort2(li, low, i-1)
    quick_sort2(li, j+1, high)
    return li


'''5、桶排序
以空间换时间

先找到最大值，创建一个等大列表，
时间复杂度O(n)
'''


def bucket_sort(list):
    max_num = max(list)
    c = [0]*(max_num+1)
    d=[]
    for num in list:
        c[num]=1
    for i in range(len(c)):
        if c[i] == 1:
            d.append(i)
    return d


'''6、归并排序
采用分治方法，先分，再治
分：
治：
O(nlog(n))
'''


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i == len(left):
        for index in right[j:]:
            result.append(index)
    else:
        for index in left[i:]:
            result.append(index)

    return result


def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = int(len(list) / 2)
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)


'''7、堆排序
在堆的数据结构中，堆中的最大值总是位于根节点（在优先队列中使用堆的话堆中的最小值位于根节点）
最大堆调整（Max Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
创建最大堆（Build Max Heap）：将堆中的所有数据重新排序
堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算

'''


def big_endian(arr, start, end):
    root = start
    while True:
        child = root * 2 + 1  # 左孩子
        if child > end:  # 孩子比最后一个节点还大 也就意味着最后一个叶子节点了 就得跳出去一次循环已经调整完毕
            break
        if child + 1 <= end and arr[child] < arr[child + 1]:  # 为了始终让其跟子元素的较大值比较 如果右边大就左换右，左边大的话就默认
            child += 1
        if arr[root] < arr[child]:  # 父节点小于子节点直接换位置 同时坐标也得换这样下次循环可以准确判断是否为最底层是不是调整完毕
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:  # 父子节点顺序正常 直接过
            break


def heap_sort(arr):
    # 无序区大根堆排序
    first = len(arr) // 2 - 1
    for start in range(first, -1, -1):  # 从下到上，从右到左对每个节点进调整 循环得到非叶子节点
        big_endian(arr, start, len(arr) - 1)  # 去调整所有的节点
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]  # 顶部尾部互换位置
        big_endian(arr, 0, end - 1)  # 重新调整子节点的顺序  从顶开始调整
    return arr


def main():
    l = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
    print(heap_sort(l))  # 原地排序


if __name__ == "__main__":
    main()