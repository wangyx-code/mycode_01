#!/usr/bin/python3

"""
向上、向下移动
"""
"""
4. (选做)完成2048核心算法
    -- 向上移动函数
       (1)创建矩阵转置函数
       (2)调用矩阵转置函数
       (3)调用向左移动函数
       (4)调用矩阵转置函数
    -- 向下移动函数
       (1)调用矩阵转置函数
       (2)调用向右移动函数
       (3)调用矩阵转置函数
"""
def zero_to_end():
    """
        向左移动
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)

def merge():
    """
        合并相同元素
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)
def move_left():
    """
        所有行向左移动
    """
    global list_merge
    for line in map:
        list_merge = line
        merge()
def move_right():
    """
        所有行向右移动
    """
    global list_merge
    for line in map:
        list_merge = line[::-1]
        merge()
        line[::-1] = list_merge

def matrux_transpose():
    # 矩阵转置
    for i in range(len(map)):
        for j in range(1,len(map)):
            if j > i:
                map[i][j],map[j][i]=map[j][i],map[i][j]

def move_up():
    # 所有行向上移动
    matrux_transpose()
    move_left()
    matrux_transpose()
def move_down():
    # 所有行向下移动
    matrux_transpose()
    move_right()
    matrux_transpose()
list_merge = [2, 0, 0, 2]
map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [4, 4, 4, 2],
]
move_up()
print(map)
