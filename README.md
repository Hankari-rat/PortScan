# PortScan - A Simple and Fast Port Scanner

PortScan is a command-line tool written in Python for discovering open ports on a target host. It's designed to be a lightweight, fast, and easy-to-use utility for network reconnaissance, making it a great tool for penetration testers, system administrators, and cybersecurity enthusiasts.

## Features

- **Flexible Target Specification:** Scan targets using either an IP address or a hostname.
- **Customizable Port Scanning:**
    - Scan the most common ports for a quick and efficient check.
    - Specify a single port for a targeted query.
    - Define a range of ports (e.g., `1-1024`) for a comprehensive scan.
    - Provide a comma-separated list of specific ports.
- **Adjustable Timeout:** Control the scan speed and accuracy by setting a connection timeout.
- **User-Friendly Output:** Clean, that clearly indicates open ports.
- **Error Handling:** Gracefully handles hostname resolution errors and invalid inputs.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Hankari-rat/PortScan.git
    cd PortScan
    ```

2.  **(Recommended) Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

## Usage

The basic syntax is:
```bash
python portscan.py <target> [options]
```

### Examples

**1. Scan the most common ports on a target (default behavior):**
*This is the fastest way to get a quick overview of a host.*

```bash
python portscan.py scanme.nmap.org
```
  
**2. Scan a specific range of ports:**

```bash
python portscan.py 192.168.1.1 --ports 1-100
```
  

**3. Scan specific, non-sequential ports:**

```bash  
python portscan.py example.com -p 80,443,8080
```
  

**4. Perform a faster scan with a lower timeout:**

```bash    
python portscan.py <target> -t 0.2
```
  

## Disclaimer

This tool is intended for educational purposes and for use in authorized security testing scenarios only. Unauthorized scanning of networks is illegal. The user is responsible for their own actions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.