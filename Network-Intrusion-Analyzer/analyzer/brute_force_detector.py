LOG_FILE = "../logs/auth.log"
REPORT_FILE = "../reports/brute_force_report.txt"

def detect_bruteforce():
    attempts = {}

    with open(LOG_FILE, "r") as log:
        for line in log:
            if "Failed password" in line:
                ip = line.split("from")[1].split()[0]
                attempts[ip] = attempts.get(ip, 0) + 1

    with open(REPORT_FILE, "w") as report:
        for ip, count in attempts.items():
            if count >= 5:
                report.write(f"Brute Force Attack detected from {ip} ({count} attempts)\n")

    print("[+] Brute force analysis completed")

if __name__ == "__main__":
    detect_bruteforce()
