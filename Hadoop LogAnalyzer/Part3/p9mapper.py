import sys
for line in sys.stdin:
    data = line.strip().split()
    if len(data) >= 10:
        ip_address = data[0]  
        bytes_transferred = data[9]  
        print("%s\t%s" % (ip_address, bytes_transferred))
