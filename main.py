import random
import os
from functools import lru_cache

arr_out = [["*" for i in range(9)] for i in range(9)]
arr_in = [[0 for i in range(9)] for i in range(9)]
arr_tem = [[0 for i in range(9)] for i in range(9)]


def showed(x, y):
    return arr_out[y][x] != '*'


def not_out(x, y):
    return x >= 0 and x < 9 and y >= 0 and y < 9


def init():
    global arr_in, arr_out
    count = 0
    while count < 10:
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if arr_in[y][x] == 1:
            continue
        arr_in[y][x] = 1
        count += 1
    for i in range(9):
        for j in range(9):
            jx(i, j)


def jx(x, y):
    global arr_tem, arr_in
    count = 0
    if arr_in[y][x] == 1:
        arr_tem[y][x] = 9
        return
    if not_out(x, y + 1) and arr_in[y + 1][x] == 1:
        count += 1
    if not_out(x + 1, y + 1) and arr_in[y + 1][x + 1] == 1:
        count += 1
    if not_out(x - 1, y + 1) and arr_in[y + 1][x - 1] == 1:
        count += 1
    if not_out(x + 1, y) and arr_in[y][x + 1] == 1:
        count += 1
    if not_out(x + 1, y - 1) and arr_in[y - 1][x + 1] == 1:
        count += 1
    if not_out(x - 1, y - 1) and arr_in[y - 1][x - 1] == 1:
        count += 1
    if not_out(x - 1, y) and arr_in[y][x - 1] == 1:
        count += 1
    if not_out(x, y - 1) and arr_in[y - 1][x] == 1:
        count += 1
    arr_tem[y][x] = count


def show(arr):
    for i in range(0, 10):
        print(i, end=' ')
    print()
    for i in range(9):
        print(i + 1, end=' ')
        for j in arr[i]:
            if j == 0:
                print(" ", end=" ")
            else:
                print(j, end=' ')
        print()


@lru_cache()
def zk(x, y):
    global arr_in, arr_out
    arr_out[y][x] = arr_tem[y][x]

    if not_out(x, y + 1) and arr_tem[y + 1][x] == 0 and not(showed(x, y + 1)):
        zk(x, y + 1)
    if not_out(x + 1, y + 1) and arr_tem[y + 1][x + 1] == 0 and not(showed(x + 1, y + 1)):
        zk(x + 1, y + 1)
    if not_out(x - 1, y + 1) and arr_tem[y + 1][x - 1] == 0 and not(showed(x - 1, y + 1)):
        zk(x - 1, y + 1)
    if not_out(x + 1, y) and arr_tem[y][x + 1] == 0 and not(showed(x + 1, y)):
        zk(x + 1, y)
    if not_out(x + 1, y - 1) and arr_tem[y - 1][x + 1] == 0 and not(showed(x + 1, y - 1)):
        zk(x + 1, y - 1)
    if not_out(x - 1, y - 1) and arr_tem[y - 1][x - 1] == 0 and not(showed(x - 1, y - 1)):
        zk(x - 1, y - 1)
    if not_out(x - 1, y) and arr_tem[y][x - 1] == 0 and not(showed(x - 1, y)):
        zk(x - 1, y)
    if not_out(x, y - 1) and arr_tem[y - 1][x] == 0 and not(showed(x, y - 1)):
        zk(x, y - 1)

    # pdb.set_trace()
    if not_out(x, y + 1) and arr_tem[y + 1][x] != -1:
        arr_out[y + 1][x] = arr_tem[y + 1][x]
    if not_out(x + 1, y + 1) and arr_tem[y + 1][x + 1] != -1:
        arr_out[y + 1][x + 1] = arr_tem[y + 1][x + 1]
    if not_out(x - 1, y + 1) and arr_tem[y + 1][x - 1] != -1:
        arr_out[y + 1][x - 1] = arr_tem[y + 1][x - 1]
    if not_out(x + 1, y) and arr_tem[y][x + 1] != -1:
        arr_out[y][x + 1] = arr_tem[y][x + 1]
    if not_out(x + 1, y - 1) and arr_tem[y - 1][x + 1] != -1:
        arr_out[y - 1][x + 1] = arr_tem[y - 1][x + 1]
    if not_out(x - 1, y - 1) and arr_tem[y - 1][x - 1] != -1:
        arr_out[y - 1][x - 1] = arr_tem[y - 1][x - 1]
    if not_out(x - 1, y) and arr_tem[y][x - 1] != -1:
        arr_out[y][x - 1] = arr_tem[y][x - 1]
    if not_out(x, y - 1) and arr_tem[y - 1][x] != -1:
        arr_out[y - 1][x] = arr_tem[y - 1][x]


def check():
    for i in range(9):
        for j in range(9):
            if arr_out[i][j] == '*' and arr_in[i][j] != 1:
                return False
    return True


def play():
    global arr_out, arr_in
    ipt_x = 0
    ipt_y = 0
    while True:
        os.system("pause")
        os.system("cls")
        show(arr_out)
        ipt_x, ipt_y = input("x y:").split()
        ipt_x, ipt_y = int(ipt_x) - 1, int(ipt_y) - 1
        # ---input err---
        if ipt_x == -2 or ipt_y == -2:
            print("退出。")
            break
        elif not(not_out(ipt_x, ipt_y)):
            print("输入出界!")
            continue
        elif arr_out[ipt_y][ipt_x] != '*':
            print("已展开！")
            continue
        elif arr_in[ipt_y][ipt_x] == 1:
            print("你输了！")
            show(arr_in)
            break
        # -------
        zk(ipt_x, ipt_y)
        rtn = check()
        if rtn:
            os.system("cls")
            print("你赢了！")
            show(arr_out)
            os.system("pause")
            break
        else:
            print("操作成功！")


init()
play()
