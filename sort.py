list1 = [7, 6, 2, 3, 9, 4, 8, 5, 1]
'''1、插入排序
从左边第二个数开始，依次与前面的数相比较，直到找到一个比他小的数为止，插入到那里
时间复杂度：平均O(n^2)   最好：O(n)    最坏O(n^2)
稳定性：稳定
'''
# def insert_sort(list):
#     for i in range(1, len(list)):
#         temp = list[i]
#         index = i
#         while index>0 and list[index-1]>temp:
#             list[index] = list[index-1]
#             index -= 1
#         list[index] = temp
#     print(list)
#
#
# insert_sort(list1)


'''2、冒泡排序
从左到右，两两依次比较，如果大小顺序不对，则交换两数，
一次遍历把最后把大的数放到尾部之后，
对前面的数字继续进行遍历
'''
# def bubble_sort(list):
#     for i in range(len(list)):
#         for j in range(len(list)-i-1):
#             if list[j]> list[j+1]:
#                 list[j],list[j+1] = list[j+1],list[j]
#     print(list)
#
#
# bubble_sort(list1)


'''3、选择排序
1、先把  第一个值赋给min， 让min和后边其余的值进行比较，若有小于min的值，则替换，最后把最小的值赋给第一个值
2、向后循环，以此类推
时间复杂度：平均O(n^2)
稳定性：不稳定
'''
# def select_sort(list):
#     for i in range(len(list)-1):
#         index_min = list[i]
#         for j in range(i+1, len(list)):
#             if list[j]< index_min:
#                 list[j], index_min = index_min,list[j]
#         list[i] = index_min
#     print(list)
#
#
# select_sort(list1)


'''4、快速排序
先从数列中取出一个数作为基准数，
将比这个数大的数全部放到它的右边，小于或等于他的数放到左边
再对左右区间重复第二步，直到各区间只有一个数
'''
# array = (3,1,2)
#
# quit_sort = lambda array: array if len(array) <= 1 else quit_sort([item for item in array[1:] if item < array[0]]) + [array[0]] + quit_sort([item for item in array[1:] if item > array[0]])
#
# print(quit_sort(array))


# def quick_sort(list):
#     if len(list)<=1:
#         return list
#     mid_index = len(list)//2
#     mid_num = list.pop(mid_index)
#     left_list = []
#     mid_list = [mid_num]
#     right_list =[]
#     for i in list:
#         if i <=mid_num:
#             left_list.append(i)
#         else:
#             right_list.append(i)
#     return quick_sort(left_list)+mid_list+quick_sort(right_list)
#
#
# print(quick_sort(list1))


'''5、桶排序
以空间换时间

先找到最大值，创建一个等大列表，
时间复杂度O(n)
'''

# def Bucket_sort(list):
#     max_num = max(list)
#     c = [0]*(max_num+1)
#     d=[]
#     for num in list:
#         c[num]=1
#     for i in range(len(c)):
#         if c[i] == 1:
#             d.append(i)
#     return d
#
#
# print(Bucket_sort(list1))


'''6、归并排序
采用分治方法，先分，再治
分：
治：
O(nlog(n))
'''


# def merge(left,right):
#     result = []
#     i = 0
#     j = 0
#     while i<len(left) and j<len(right):
#         if left[i]<right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     if i == len(left):
#         for index in right[j:]:
#             result.append(index)
#     else:
#         for index in left[i:]:
#             result.append(index)
#
#     return result
#
#
# def merge_sort(list):
#     if len(list) <= 1:
#         return list
#     mid = int(len(list) / 2)
#     left = merge_sort(list[:mid])
#     right = merge_sort(list[mid:])
#     return merge(left, right)
#
#
# print(merge_sort(list1))


'''7、二分查找
1、确定该期间的中间位置K
2、将查找的值T与array[k]比较。若相等，查找成功返回此位置；否则确定新的查找区域，继续二分查找。区域确定如下：
'''


# def binary_search(lst, t):
#     length = len(lst)
#     start = 0
#     end = length - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#         if t == lst[mid]:
#             return 'lst:index{}'.format(mid)
#         elif t < lst[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return False


'''递归方式'''


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


lst1 = [2, 4, 5, 6, 7, 9, 20]

print(binary_search(lst1, 9))
