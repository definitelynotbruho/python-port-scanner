import socket
import argparse

def with_user_input(ip, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        s.connect((ip, port))
        print("Port is opened")
    except:
        print("Port is closed")
    s.close()

def with_range(ip, downrange, uprange):
    for i in range(downrange, uprange + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((ip, i))
            print(f"Port {i} is opened")
        except:
            print(f"Port {i} is closed")
        s.close()

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

if __name__ == "__main__":
    main()
