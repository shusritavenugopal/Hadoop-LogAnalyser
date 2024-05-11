import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 8:
        status_code = data[8]
        if status_code == '404':
            print("404\t1")


