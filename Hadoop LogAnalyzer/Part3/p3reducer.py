import sys

method_count = {}

for line in sys.stdin:
    method, count = line.strip().split('\t')
    method_count[method] = method_count.get(method, 0) + int(count)

# Print method counts
print("The following are the HTTP request methods and their counts:")

for method, count in method_count.items():
    print("%s: %s" % (method, count))  
