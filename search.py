lst1 = [2, 4, 6, 7, 9, 19, 43, 82, 100]
'''1、二分查找
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
# def binary_search(lst, t):
#     length = len(lst)
#     if length == 0:
#         return False
#     mid = length // 2
#     if t == lst[mid]:
#         return True
#     elif t < lst[mid]:
#         return binary_search(lst[:mid],t)
#     else:
#         return binary_search(lst[mid+1:],t)
