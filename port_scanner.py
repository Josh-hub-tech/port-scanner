#!/usr/bin/env python3
import socket
import argparse

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((host, port))
        print(f"[+] Port {port} is OPEN")
    except (socket.timeout, ConnectionRefusedError):
        pass
    finally:
        sock.close()

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("host", help="Target host to scan (IP or domain)")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range (default: 1-1024, format: start-end)")
    args = parser.parse_args()

    host = args.host
    port_range = args.ports.split("-")
    start, end = int(port_range[0]), int(port_range[1])

    print(f"[*] Scanning {host} from port {start} to {end}...\n")
    for port in range(start, end+1):
        scan_port(host, port)

if __name__ == "__main__":
    main()
