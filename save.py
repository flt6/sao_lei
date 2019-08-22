from socket import *
s = socket()
s.connect(("192.168.124.6", 6306))

try:
    s.send("s1.send(str(arr_{}).encode())".format("out").encode())
    data = s.recv(10000).decode()
    exec("arr_out={}".format(data))
    print("成功读取arr_out!")

    s.send("s1.send(str(arr_in).encode())".encode())
    data = s.recv(10000).decode()
    exec("arr_in={}".format(data))
    print("成功读取arr_in!")

    s.send("s1.send(str(arr_push).encode())".encode())
    data = s.recv(10000).decode()
    exec("arr_push={}".format(data))
    print("成功读取arr_push!")

    s.send("s1.send(str(arr_bj).encode())".encode())
    data = s.recv(10000).decode()
    exec("arr_bj={}".format(data))
    print("成功读取arr_bj!")

    s.send("s1.send(str(N).encode())".encode())
    data = s.recv(10000).decode()
    exec("N={}".format(data))
    print("成功读取N!")

    print("开始保存")
    with open("save.txt", "w", encoding="utf-8") as f:
        f.write("arr_out=")
        f.write(str(arr_out))
        print("成功保存arr_out")

        f.write("\narr_in=")
        f.write(str(arr_in))
        print("成功保存arr_in")

        f.write("\narr_push=")
        f.write(str(arr_push))
        print("成功保存arr_push")

        f.write("\narr_bj=")
        f.write(str(arr_push))
        print("成功保存arr_bj")

        f.write("\nN:")
        f.write(str(N))
        print("成功保存N")
except OSError:
    print("对方已结束！")
    exit(0)
except KeyboardInterrupt:
    s.send("@bye@".encode())
    exit(0)
