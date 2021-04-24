import random
import os
import threading
from socket import *

N = 16
LEI = 40
arr_out = [["*" for i in range(N)] for i in range(N)]
arr_in = [[0 for i in range(N)] for i in range(N)]
arr_push = [[0 for i in range(N)] for i in range(N)]
arr_bj = [[0 for i in range(N)] for i in range(N)]
ENABLE_REMOUTE = False
s = socket()
reload = False


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


def show(arr):
    global N
    for i in range(0, N + 1):
        print("\33[1;32m{:^2}\33[0m".format(i), end=' ')
    print()
    for i in range(0,N):
        print("\33[1;32m{:^2}\33[0m".format(i + 1), end=' ')
        for j in range(0,N):
            if arr_bj[j][i] == 1:
                print("\33[1;31m{:^2}\33[0m".format(arr[j][i]), end=" ")
            elif arr_bj[j][i] == 2:
                print("\33[1;33m{:^2}\33[0m".format(arr[j][i]), end=" ")
            elif arr[j][i] == 0:
                print("{:^2}".format('░'), end=' ')
            else:
                print("{:^2}".format(arr[j][i]), end=' ')
        print()


def get(x, y):
    count = 0
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
    return count


def check01(x, y, n=0):
    return not_out(x, y) and arr_in[y][x] == n and not(showed(x, y))


def zk01(x, y):
    if check01(x, y + 1):
        arr_out[y + 1][x] = get(x, y + 1)
    if check01(x + 1, y):
        arr_out[y][x + 1] = get(x + 1, y)
    if check01(x - 1, y):
        arr_out[y][x - 1] = get(x - 1, y)
    if check01(x, y - 1):
        arr_out[y - 1][x] = get(x, y - 1)

    if check01(x + 1, y - 1):
        arr_out[y - 1][x + 1] = get(x + 1, y - 1)
    if check01(x - 1, y - 1):
        arr_out[y - 1][x - 1] = get(x - 1, y - 1)
    if check01(x - 1, y + 1):
        arr_out[y + 1][x - 1] = get(x - 1, y + 1)
    if check01(x + 1, y + 1):
        arr_out[y + 1][x + 1] = get(x + 1, y + 1)


def zk(x, y):
    global arr_in, arr_out
    arr_out[y][x] = get(x, y)
    push = True
    while push:
        push = False
        for i in range(N):
            for j in range(N):
                if showed(i, j) and arr_push[j][i] == 0 and arr_out[j][i] == 0:
                    arr_push[j][i] = 1
                    push = True
                    if check01(i + 1, j) and arr_push[j][i + 1] == 0:
                        arr_out[j][i + 1] = get(i + 1, j)
                        zk01(i + 1, j)
                    if check01(i - 1, j) and arr_push[j][i - 1] == 0:
                        arr_out[j][i - 1] = get(i - 1, j)
                        zk01(i - 1, j)
                    if check01(i, j + 1) and arr_push[j + 1][i] == 0:
                        arr_out[j + 1][i] = get(i, j + 1)
                        zk01(i, j + 1)
                    if check01(i, j - 1) and arr_push[j - 1][i] == 0:
                        arr_out[j - 1][i] = get(i, j - 1)
                        zk01(i, j - 1)


def check():
    for i in range(N):
        for j in range(N):
            if arr_out[i][j] == '*' and arr_in[i][j] != 1:
                return False
    return True


def sock():
    global arr_bj, arr_in, arr_out, arr_push, s
    s.bind(("192.168.124.6", 6306))
    s.listen(1)
    while True:
        s1, _ = s.accept()
        t = threading.Thread(target=sock_1, args=(s1,))
        t.setDaemon(True)
        t.start()


def sock_1(s1):
    global arr_in, arr_out, arr_push, arr_bj, reload
    while True:
        data = s1.recv(10000).decode()
        if data == "@bye@":
            s1.send("@bye@".encode())
            return
        else:
            exec(data)


def play():
    global arr_out, arr_in, reload
    ipt_x = 0
    ipt_y = 0
    while True:
        os.system("pause")
        os.system("cls")
        show(arr_out)
        try:
            ipt_x, ipt_y = input("x y:").split()
            ipt_x, ipt_y = int(ipt_x) - 1, int(ipt_y) - 1
        except Exception:
            print("输入错误！")
        arr_bj[ipt_y][ipt_x] = 2
        os.system("cls")
        show(arr_out)
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
        if reload:
            break

if ENABLE_REMOUTE:
    t = threading.Thread(target=sock)
    t.setDaemon(True)
    t.start()

init()
# init_from_file()
while True:
    play()
    print("reload!")
    if not(reload):
        print("\n\n\n")
        ipt = input("是否继续(YES/no):")
        if ipt == "no":
            break
    else:
        reload = False
