import socket
import argparse
import threading
from queue import Queue

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 5900, 8080]
print_lock = threading.Lock()

def scan(port, target_ip, timeout, queue_results):
    try:    
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                queue_results.put(port)
    except Exception as e:
        pass

def port_scannner(target, ports, timeout):
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[!] Cannot resolve '{target}': Unknown host")
        return
    
    if ports.lower() in ['common_ports', 'common']:
        ports_to_scan = COMMON_PORTS
    else:
        if '-' in ports:
            start_port, end_port = map(int, ports.split('-'))
            ports_to_scan = list(range(start_port, end_port + 1))
        elif ',' in ports:
            ports_to_scan = list(map(int, ports.split(',')))
            ports_to_scan = sorted(set(ports_to_scan))
        else:
            ports_to_scan = [int(ports)]
    
    results_queue = Queue()
    
    print("="*40)        
    print(f"[*] Scanning target: {target}")
    print(f"[*] IP address: {target_ip}")
    print(f"[*] {len(ports_to_scan)} ports to scan.")

    threads = []
    for port in ports_to_scan:
        t = threading.Thread(target=scan, args=(port,target_ip,timeout,results_queue))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
        
    open_ports = []
    while not results_queue.empty():
        open_ports.append(results_queue.get())

    print("="*40)       
    print("[+] Scan complete!")
    if open_ports:
        print(f"[+] Found {len(open_ports)} open ports")
        print("-"*40)
        for port in sorted(open_ports):
            print(f"[+] Port {port} is open")
    else:
        print("[-] No open ports found.")
    print("="*40)
            
def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("target", help="Target's IP address or hostname")
    parser.add_argument("-p", "--ports", type=str, default="common_ports" , help = "Ports to scan (comma-separated (for specific ports), minus-separated (for range) or 'common_ports' / 'common' for common ports)")
    parser.add_argument("-t", "--timeout", type=float, default=1.0, help="Timeout before declaring a ports closed (in seconds)")
    args = parser.parse_args()
    port_scannner(args.target, args.ports, args.timeout)
    
if __name__ == "__main__":
    main()