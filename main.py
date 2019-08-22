import random
import os
from functools import lru_cache

N = 9
LEI = 10
arr_out = [["*" for i in range(N)] for i in range(N)]
arr_in = [[0 for i in range(N)] for i in range(N)]
arr_tem = [[0 for i in range(N)] for i in range(N)]
arr_bj = [[0 for i in range(N)] for i in range(N)]


def showed(x, y):
    return arr_out[y][x] != '*'


def not_out(x, y):
    return x >= 0 and x < N and y >= 0 and y < N


def init():
    global arr_in, arr_out
    count = 0
    while count < LEI:
        x = random.randint(0, N - 1)
        y = random.randint(0, N - 1)
        if arr_in[y][x] == 1:
            continue
        arr_in[y][x] = 1
        count += 1
    for i in range(N):
        for j in range(N):
            jx(i, j)


def jx(x, y):
    global arr_tem, arr_in
    count = 0
    if arr_in[y][x] == 1:
        arr_tem[y][x] = -1
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
    for i in range(0, N + 1):
        print("\33[1;32m{}\33[0m".format(i), end=' ')
    print()
    for i in range(N):
        print("\33[1;32m{}\33[0m".format(i + 1), end=' ')
        for j in range(len(arr[i])):
            if arr_bj[j][i] == 1:
                print("\33[1;31m{}\33[0m".format(arr[j][i]), end=" ")
            elif arr_bj[j][i] == 2:
                print("\33[1;33m{}\33[0m".format(arr[j][i]), end=" ")
            else:
                print(arr[j][i], end=' ')
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
    for i in range(N):
        for j in range(N):
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
        print()
        show(arr_in)
        ipt_x, ipt_y = input("x y:").split()
        ipt_x, ipt_y = int(ipt_x) - 1, int(ipt_y) - 1

        arr_bj[ipt_y][ipt_x] = 2
        os.system("cls")
        show(arr_out)
        print()
        show(arr_in)
        print("x y:{} {}".format(ipt_x + 1, ipt_y + 1))
        try:
            what = int(input("展开1 标记2 取消3:"))
        except ValueError:
            print("输入错误！")
            continue
        arr_bj[ipt_y][ipt_x] = 0

        # ---input err---
        if ipt_x == -2 or ipt_y == -2:
            print("退出。")
            break
        elif not(not_out(ipt_x, ipt_y)):
            print("输入出界!")
            continue
        elif what < 1 or what > 3:
            print("执行类型错误！")
            continue
        elif what == 3:
            print("取消！")
            continue
        elif what == 2:
            arr_bj[ipt_y][ipt_x] = 1
            print("标记成功！")
            continue
        elif arr_out[ipt_y][ipt_x] != '*' and what == 1:
            print("已展开！")
            continue
        elif arr_in[ipt_y][ipt_x] == 1 and what == 1:
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
