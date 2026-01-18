# Simple Port Scanner for Security Analysis
# Usage: python port_scanner.py <target_ip>

import socket
import sys

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        s.close()
    except:
        print(f"Port {port}: FILTERED")

def main():
    if len(sys.argv) != 2:
        print("Usage: python port_scanner.py <target_ip>")
        sys.exit(1)
    
    target = sys.argv[1]
    print(f"Scanning target: {target}")
    
    for port in range(1, 1025):
        scan_port(target, port)

if __name__ == "__main__":
    main()
