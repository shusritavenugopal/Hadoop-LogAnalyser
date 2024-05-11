import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 5:
        request = data[5].strip('"')
        http_method = request.split()[0]
        if http_method.upper() == 'POST':  
            print("POST\t1")

