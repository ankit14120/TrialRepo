LOG_FILE = "../logs/syslog"
REPORT_FILE = "../reports/port_scan_report.txt"

def detect_portscan():
    suspicious_ips = set()

    with open(LOG_FILE, "r") as log:
        for line in log:
            if "SYN" in line or "connection attempt" in line:
                parts = line.split()
                suspicious_ips.add(parts[-1])

    with open(REPORT_FILE, "w") as report:
        for ip in suspicious_ips:
            report.write(f"Possible Port Scan detected from {ip}\n")

    print("[+] Port scan analysis completed")

if __name__ == "__main__":
    detect_portscan()
