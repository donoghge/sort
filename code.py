# def func(n):
#     for i in range(n+1):
#         m_list = list('*' for j in range(i))
#         m = ' '.join(m_list)
#         print((n-i)*' '+m)
# func(4)


# l1 = [1,1,3,4,3,4,5,3,7,1,6]
# number = 2
# def func(code,num):
#     index = []
#     for i in code:
#         if code.count(i)>num:
#             index.append(i)
#     print(list(set(index)))
# func(l1,number)


# str1 = 'get_user_name'
# def func(str1):
#     l1 = str1.split('_')
#     index = []
#     index.append(l1[0])
#     for i in range(1,len(l1)):
#         l = l1[i].title()
#         index.append(l)
#     print(''.join(index))
# func(str1)

# A = ('a', 'b', 'c', 'd')
# del A[2]
# ''' 异常， 元组无序'''

# D = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
#
# for key, value in D.items():
#     print(key, value)

# 斐波那契
# def fib(count):
#     prev = 0
#     curr = 1
#     for i in range(count):
#         prev, curr = curr, prev + curr


# 多进程调用

# from multiprocessing import Process
#
#
# def run(name, description):
#     while True:
#         print("%s is a %s  man!" % (name, description))
#
#
# if __name__ == '__main__':
#
#     p = Process(target=run, args=('sunck', 'rock'))
#     p.start()
#
#     while True:
#         print('sunck is a nice man')


# 多线程调用
# import threading
#
#
# def work(seq):
#     print(seq)
#
#
# if __name__ == '__main__':
#     th1 = threading.Thread(target=work, args=(1,), name='th2')
#
#     th1.start()
#
#     th1.join()

