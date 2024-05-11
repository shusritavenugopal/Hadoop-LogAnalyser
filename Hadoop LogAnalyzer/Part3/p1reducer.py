import sys

hit_count = 0

for line in sys.stdin:
    # Strip whitespace and split on tab character
    key, value = line.strip().split('\t')

    # Increment hit count
    hit_count += int(value)
    
print("Total hits to directory /images/smilies/ is %s\t" % hit_count)
