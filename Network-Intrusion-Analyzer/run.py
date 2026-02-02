import os

print("[*] Running Network Intrusion Log Analyzer")

os.system("sudo python3 analyzer/log_collector.py")
os.system("python3 analyzer/brute_force_detector.py")
os.system("python3 analyzer/port_scan_detector.py")

print("[+] All analysis completed. Check reports folder.")
