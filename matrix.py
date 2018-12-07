'''螺旋矩阵'''

import itertools


def is_valid(matrix, row, col):
    '''检查对应位置的值是否有效'''
    try:
        return matrix[row][col] == None
    except IndexError:
        return False


def gen_matrix(n):
    '''生成矩阵'''
    matrix = [[None] * n for i in range(n)]
    arrows = itertools.cycle([
        (0, 1),   # 右
        (1, 0),   # 下
        (0, -1),  # 左
        (-1, 0)   # 上
    ])

    # 设置初始位置和方向
    row, col = 0, 0
    delta_row, delta_col = next(arrows)

    for num in range(1, n * n + 1):
        # 设置当前值
        matrix[row][col] = num

        # 计算下一次的位置
        if not is_valid(matrix, row + delta_row, col + delta_col):
            delta_row, delta_col = next(arrows)  # 调整方向
        row, col = row + delta_row, col + delta_col

    return matrix


def print_matrix(matrix):
    '''格式化打印矩阵'''
    max_num = len(matrix) ** 2
    length = len(str(max_num))
    fmt = lambda num: str(num).rjust(length)

    for row in matrix:
        line = ' '.join([fmt(num) for num in row])
        print(line)


if __name__ == '__main__':
    try:
        n = int(input('输入矩阵大小: '))
        if n < 0:
            raise ValueError
    except ValueError:
        print('请输入正确的数字！')
        exit(1)
    else:
        matrix = gen_matrix(n)
        print_matrix(matrix)
