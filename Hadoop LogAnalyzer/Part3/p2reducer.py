import sys

count = 0
for line in sys.stdin:
    
    
    key, value = line.strip().split('\t')

    # Increment hit count
    count += int(value)

print("Total hits from IP 96.32.128.5:%s" % count)
