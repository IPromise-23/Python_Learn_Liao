# tcp_server.py
import socket
import threading
import time

# 定义处理客户端通信的函数（必须在调用前定义）
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')  # 发送欢迎消息
    while True:
        data = sock.recv(1024)  # 接收客户端数据，最多1024字节
        time.sleep(1)  # 模拟服务器处理耗时
        # 退出条件：客户端断开 或 发送exit
        if not data or data.decode('utf-8') == 'exit':
            break
        # 回复客户端
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()  # 关闭当前客户端连接
    print('Connection from %s:%s closed.' % addr)

# 服务器核心逻辑
if __name__ == '__main__':
    # 创建TCP Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定本地地址和端口（127.0.0.1仅本机访问，0.0.0.0可局域网访问）
    s.bind(('127.0.0.1', 9999))
    # 监听端口，队列大小5
    s.listen(5)
    print('Waiting for connection... (服务器已启动，监听9999端口)')
    
    # 无限循环接受客户端连接
    while True:
        sock, addr = s.accept()  # 阻塞等待新连接
        # 创建新线程处理该客户端
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()