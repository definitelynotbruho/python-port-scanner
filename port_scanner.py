import socket

def with_user_input():
    ip = input("Input IP: ")
    port = int(input("Input the port: "))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        s.connect((ip, port))
        print("Port is opened")
    except:
        print("Port is closed")
    s.close()

def with_range():
    ip = input("Input IP")
    downrange, uprange = map(int, input("Input a range: ").split())
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
    ans = int(input("Select a mode of port scanner: Single (1) or Range (2): \n"))
    if ans == 1:
        with_user_input()
    elif ans == 2:
        with_range()
    else:
        print("Unkown command!")

if __name__ == "__main__":
    main()

