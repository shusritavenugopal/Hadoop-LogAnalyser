import sys

ip_count = {}

for line in sys.stdin:
    ip, count = line.strip().split('\t')
    ip_count[ip] = ip_count.get(ip, 0) + int(count)

most_accessed_ip = max(ip_count, key=ip_count.get)
access_count = ip_count[most_accessed_ip]

print("Total hits from IP: %s" %(most_accessed_ip))
print("Access Count: %s" % (access_count))

