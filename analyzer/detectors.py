from collections import Counter

def detect_bruteforce(ip_list, threshold=5):
    counts = Counter(ip_list)
    return {ip: c for ip, c in counts.items() if c >= threshold}


def detect_port_scan(port_list, threshold=10):
    counts = Counter(port_list)
    return {port: c for port, c in counts.items() if c >= threshold}
