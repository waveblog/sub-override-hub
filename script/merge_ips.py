import requests
import os
import re

# URLs of the IP lists
urls = [
    "https://raw.githubusercontent.com/teishahbc/bgp-cn-ip/refs/heads/main/cn_as4134_as56040_ipv4.txt",
    "https://raw.githubusercontent.com/teishahbc/bgp-cn-ip/main/cn_other_asns_ipv4.txt",
    "https://ruleset.skk.moe/Clash/ip/china_ip.txt"
]

# Output directory and file
output_dir = "../mergecnip"
output_file = os.path.join(output_dir, "china_ip.txt")

# Set to store unique IPs and CIDRs
unique_ips = set()

# Regex to find IP/CIDR patterns, ignoring comments
ip_pattern = re.compile(r"^\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2})?)\s*(?:#.*)?$")

print("Starting IP address processing...")

for url in urls:
    try:
        print(f"Fetching data from {url}...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        
        content = response.text
        lines = content.splitlines()
        
        count = 0
        for line in lines:
            # Ignore empty lines and lines that are only comments
            if line.strip() and not line.strip().startswith('#'):
                 # Add the cleaned line to the set
                unique_ips.add(line.strip())
                count += 1
        print(f"Found and added {count} entries from {url}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        continue

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    print(f"Creating directory: {output_dir}")
    os.makedirs(output_dir)

# Sort the IPs for consistent output
sorted_ips = sorted(list(unique_ips))

# Write the result to the output file
try:
    with open(output_file, 'w', encoding='utf-8') as f:
        for ip in sorted_ips:
            f.write(ip + '\n')
    print(f"Successfully merged {len(sorted_ips)} unique IPs into {output_file}")
except IOError as e:
    print(f"Error writing to file {output_file}: {e}")
