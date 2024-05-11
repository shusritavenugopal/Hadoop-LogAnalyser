import sys

path_hits = {}

for line in sys.stdin:
    data = line.strip().split()
    if len(data) >= 9:
        request = data[6]
        if request:
            request = request.strip('"')
            path_hits[request] = path_hits.get(request, 0) + 1

for path, hits in path_hits.items():
    print("%s\t%s"%(path,hits))
