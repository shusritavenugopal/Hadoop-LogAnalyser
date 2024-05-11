import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) >= 9:
        date = data[3].strip('[')
        status_code = data[8]
        bytes_transferred = data[9]
        print("%s\t%s\t%s" % (date, status_code, bytes_transferred))

