import socket
import argparse
import threading

def with_user_input(ip, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        s.connect((ip, port))
        print(f"{port} port is opened")
    except:
        print(f"{port} port is closed")
    s.close()

def with_range(ip, downrange, uprange):
    threads = []

    for i in range(downrange, uprange + 1):
        t = threading.Thread(target=with_user_input, args=(ip, i))
        t.start()      
        threads.append(t) 

    for t in threads:
        t.join()

def main():
    parser = argparse.ArgumentParser(description='Simple portscanner')
    parser.add_argument('ip', help='IP-address')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-p', '--port', type=int, help='Single port')
    group.add_argument('-r', '--range', help='Range of ports (For example: 20 100)')

    args = parser.parse_args()

    if args.port:
        with_user_input(args.ip, args.port)
    elif args.range:
        down, up = map(int, args.range.split('-'))
        with_range(args.ip, down, up)

main()
