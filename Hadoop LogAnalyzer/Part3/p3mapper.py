import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 5:
        request = data[5].strip('"')  # Extract the request line
        http_method = request.split()[0].upper()  # Extract the HTTP request method
        print("%s\t1" % http_method)  
