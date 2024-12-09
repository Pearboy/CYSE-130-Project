import subprocess

# Function to scan target with nmap
def run_nmap(target):
    result = subprocess.run(['nmap', '-sV', target], capture_output=True, text=True)
    print(result.stdout)

run_nmap('127.0.0.1')  # Scan localhost

from scapy.all import TCP, IP, sniff

# Function to monitor packets using scapy
def monitor_packets(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(IP):
        print(f"Source IP: {pkt[IP].src}, Destination IP: {pkt[IP].dst}")

sniff(prn=monitor_packets, count=10)  # Capture 10 packets

