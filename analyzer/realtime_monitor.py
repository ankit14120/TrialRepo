import time
import re

def follow(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line


def monitor_auth_log(file_path, callback):
    with open(file_path, "r", errors="ignore") as f:
        for line in follow(f):
            if "Failed password" in line:
                match = re.search(r"from ([0-9.]+)", line)
                if match:
                    callback("bruteforce", match.group(1))


def monitor_ufw_log(file_path, callback):
    with open(file_path, "r", errors="ignore") as f:
        for line in follow(f):
            if "DPT=" in line:
                match = re.search(r"DPT=(\d+)", line)
                if match:
                    callback("portscan", match.group(1))
