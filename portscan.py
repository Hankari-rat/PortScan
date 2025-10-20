import socket
import argparse

common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 5900, 8080]

def port_scannner(target, ports, timeout):
    if ports == "common_ports" or ports == "common":
        ports_to_scan = common_ports
    else:
        if '-' in ports:
            start_port, end_port = map(int, ports.split('-'))
            ports_to_scan = list(range(start_port, end_port + 1))
        elif ',' in ports:
            ports_to_scan = list(map(int, ports.split(',')))
            ports_to_scan = sorted(set(ports_to_scan))
        else:
            ports_to_scan = [int(ports)]
        
    print("="*40)        
    print(f"Scanning target: {target}")
    print(f"{len(ports_to_scan)} ports to be scanned")
    print("="*40)
    for port in ports_to_scan:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port}: Open")
            sock.close()
        else:
            sock.close()
    print("="*40)       
    print("Scan complete.")
            
def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("target", help="Target's IP address or hostname")
    parser.add_argument("-p", "--ports", type=str, default="common_ports" , help = "Ports to scan (comma-separated (for specific ports), minus-separated (for range) or 'common_ports' / 'common' for common ports)")
    parser.add_argument("-t", "--timeout", type=float, default=1.0, help="Timeout before declaring a ports closed (in seconds)")
    args = parser.parse_args()
    port_scannner(args.target, args.ports, args.timeout)
    
if __name__ == "__main__":
    main()