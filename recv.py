from socket import *
import os
import time


def show(arr, N, arr_bj):
    for i in range(0, N + 1):
        print("\33[1;32m{:^2}\33[0m".format(i), end=' ')
    print()
    for i in range(N):
        print("\33[1;32m{:^2}\33[0m".format(i + 1), end=' ')
        for j in range(len(arr[i])):
            if arr_bj[j][i] == 1:
                print("\33[1;31m{:^2}\33[0m".format(arr[j][i]), end=" ")
            elif arr_bj[j][i] == 2:
                print("\33[1;33m{:^2}\33[0m".format(arr[j][i]), end=" ")
            else:
                print("{:^2}".format(arr[j][i]), end=' ')
        print()


s = socket()
s.connect(("192.168.124.6", 6306))
NAME = input("后缀：")
while True:
    try:
        s.send("s1.send(str(arr_{}).encode())".format(NAME).encode())
        data = s.recv(1024).decode()
        exec("arr={}".format(data))
        s.send("s1.send(str(arr_bj).encode())".format(NAME).encode())
        data = s.recv(1024).decode()
        exec("arr_bj={}".format(data))
        os.system("cls")
        show(arr, 9, arr_bj)
        time.sleep(1)
    except OSError:
        print("对方已结束！")
        exit(0)
    except KeyboardInterrupt:
        s.send("@bye@".encode())
        exit(0)
