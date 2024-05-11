import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 0:
        ip = data[0]
        if ip == "96.32.128.5":
            print("ip_96.32.128.5\t1")

