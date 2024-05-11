import sys

total_post_requests = 0

for line in sys.stdin:
    # Split the input line into method and count
    method, count = line.strip().split('\t')
    # Check if the method is POST
    if method == 'POST':
        # Increment the total count of POST requests
        total_post_requests += int(count)

print("Total POST requests:\t%s" % total_post_requests)
