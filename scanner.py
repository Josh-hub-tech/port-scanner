#!/usr/bin/env python3
"""Simple threaded TCP port scanner.
Author: Joshua-hub-tech (starter project)
Use only on systems you own or have permission to test.
"""

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

def scan_port(host, port, timeout=1.0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            if result == 0:
                return port, True
    except Exception:
        pass
    return port, False

def parse_ports(ports_str):
    """Parse a ports string like '22,80,443' or '1-1024' or combination '22,80,100-200'"""
    ports = set()
    parts = ports_str.split(',')
    for part in parts:
        part = part.strip()
        if '-' in part:
            a,b = part.split('-', 1)
            ports.update(range(int(a), int(b)+1))
        else:
            if part:
                ports.add(int(part))
    return sorted(p for p in ports if 0 < p <= 65535)

def run_scan(host, ports, threads, timeout):
    open_ports = []
    start = datetime.now()
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(scan_port, host, p, timeout): p for p in ports}
        for fut in as_completed(futures):
            port, is_open = fut.result()
            if is_open:
                print(f"[+] Port {port} open")
                open_ports.append(port)
    duration = datetime.now() - start
    return open_ports, duration

def main():
    parser = argparse.ArgumentParser(description='Simple threaded TCP port scanner')
    parser.add_argument('--host', required=True, help='Target hostname or IP')
    parser.add_argument('--start', type=int, help='Start of port range (e.g., 1)')
    parser.add_argument('--end', type=int, help='End of port range (e.g., 1024)')
    parser.add_argument('--ports', help='Comma-separated ports/ranges (e.g., 22,80,443,1000-2000)')
    parser.add_argument('--threads', type=int, default=100, help='Number of threads (default: 100)')
    parser.add_argument('--timeout', type=float, default=1.0, help='Socket timeout seconds (default: 1.0)')
    parser.add_argument('--output', help='Save results to file (optional)')
    args = parser.parse_args()

    target = args.host
    if args.ports:
        ports = parse_ports(args.ports)
    else:
        start = args.start or 1
        end = args.end or 1024
        ports = list(range(start, end+1))

    print(f"Scanning {target} ports: {len(ports)} (threads={args.threads}, timeout={args.timeout})")
    open_ports, duration = run_scan(target, ports, threads=args.threads, timeout=args.timeout)
    print(f"Scan completed in {duration}. Open ports: {open_ports}")

    if args.output:
        with open(args.output, 'w') as f:
            f.write(f"Scan target: {target}\n")
            f.write(f"Scanned ports: {len(ports)}\n")
            f.write(f"Open ports: {open_ports}\n")
            f.write(f"Duration: {duration}\n")
        print(f"Results saved to {args.output}")

if __name__ == '__main__':
    main()
