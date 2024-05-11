import sys

total_data = 0

for line in sys.stdin:
    date, status_code, size = line.strip().split('\t')
    if date.startswith('19/Dec/2020'):
        total_data += int(size)
print("Total data requested on 19/Dec/2020:\t%s"%total_data)
