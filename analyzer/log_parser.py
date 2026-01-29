import re

def parse_auth_log(file_path):
    failed_ips = []
    with open(file_path, "r", errors="ignore") as f:
        for line in f:
            if "Failed password" in line:
                match = re.search(r"from ([0-9.]+)", line)
                if match:
                    failed_ips.append(match.group(1))
    return failed_ips


def parse_ufw_log(file_path):
    ports = []
    with open(file_path, "r", errors="ignore") as f:
        for line in f:
            if "DPT=" in line:
                match = re.search(r"DPT=(\d+)", line)
                if match:
                    ports.append(int(match.group(1)))
    return ports
