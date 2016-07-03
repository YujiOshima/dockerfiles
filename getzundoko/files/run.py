import sys
import http.client
import time

DESIRE = b"zun zun zun doko **kiyoshi** "

def main(server, port, loopnum):
    conn = http.client.HTTPConnection(server, port)
    for i in range(0, loopnum):
        result = b""
        for i in range(0, 5):
            conn.request("GET", "/")
            result += conn.getresponse().read() + b" "
            print(result)
            if result not in DESIRE:
                print("faild...")
                break
            time.sleep(0.01)
        if result == DESIRE:
            print("done!!")
            return 

if __name__ == '__main__':
    args = sys.argv
    server = "localhost"
    port = 80
    loopnum = 10
    if len(args) > 1:
        server = args[1]
    if len(args) > 2:
        port = args[2]
    if len(args) > 3:
        loopnum = int(args[3])
    print("connect "+server+":"+str(port))
    main(server, port, loopnum)
