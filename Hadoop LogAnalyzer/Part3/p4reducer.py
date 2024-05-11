import sys

path_hits = {}

for line in sys.stdin:
    path, count = line.strip().split("\t")
    path_hits[path] = path_hits.get(path, 0) + int(count)

most_hit_path = max(path_hits, key=path_hits.get)
hit_count = path_hits[most_hit_path]

print("Most hit path: %s" % (most_hit_path))
print("(hits: %s)" % (hit_count))
