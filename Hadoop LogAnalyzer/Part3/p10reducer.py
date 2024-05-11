import sys

total_bytes = 0

for line in sys.stdin:
    date, status_code, bytes_transferred = line.strip().split('\t')
    # Check if the status code is 200 and the date starts with '16/Jan/2022'
    if status_code == '200' and date.startswith('16/Jan/2022'):
        total_bytes += int(bytes_transferred)
print("The total data(in bytes) successfully(with status code 200) requested on 16/Jan/2022 is")
print(total_bytes)
