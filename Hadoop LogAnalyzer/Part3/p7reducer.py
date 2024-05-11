import sys

count = 0
for line in sys.stdin:
    key, value = line.strip().split('\t')
    count += int(value)
print("Total requests with status code 404: %s" % (count))
