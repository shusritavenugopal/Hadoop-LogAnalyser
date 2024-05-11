import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 0:
        ip = data[0]
        print("%s\t1" % ip)


