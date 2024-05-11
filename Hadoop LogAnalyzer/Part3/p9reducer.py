import sys
ip_data_flow = {}
for line in sys.stdin:
    ip_address, bytes_transferred = line.strip().split("\t")
    if bytes_transferred != "-":  
        ip_data_flow[ip_address] = ip_data_flow.get(ip_address, 0) + int(bytes_transferred)
sorted_ips = sorted(ip_data_flow.items(), key=lambda x: x[1], reverse=True)
for ip, data_flow in sorted_ips[:3]:
    print("%s\t%s" % (ip,data_flow))
