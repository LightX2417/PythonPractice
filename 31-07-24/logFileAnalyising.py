# Analyze a log file to find the most common IP addresses that accessed a server and the count of their accesses using the Counter class.

from collections import Counter

# Example log data
log_data = """
192.168.1.1 - - [28/Jul/2023:10:00:00] "GET /index.html HTTP/1.1" 200 1024
192.168.1.2 - - [28/Jul/2023:10:01:00] "POST /form.html HTTP/1.1" 200 2048
192.168.1.1 - - [28/Jul/2023:10:02:00] "GET /about.html HTTP/1.1" 200 512
192.168.1.3 - - [28/Jul/2023:10:03:00] "GET /index.html HTTP/1.1" 200 1024
192.168.1.2 - - [28/Jul/2023:10:04:00] "GET /contact.html HTTP/1.1" 200 1024
"""

# Extract IP addresses from log data
ip_addresses = [line.split()[0] for line in log_data.strip().split("\n")]
counter = Counter(ip_addresses)

# Find the most common IP addresses
most_common_ips = counter.most_common()

print("Most common IP addresses and their counts:")
for ip, count in most_common_ips:
    print(f"{ip}: {count}")
