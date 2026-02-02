import os
import time

print("\n==============================")
print(" Network Intrusion Log Analyzer")
print("==============================\n")

# 1. Collect Logs
print("[1] Collecting system logs...")
os.system("sudo python3 analyzer/log_collector.py")
time.sleep(1)

# 2. Brute Force Detection
print("[2] Running brute force detection...")
os.system("python3 analyzer/brute_force_detector.py")
time.sleep(1)

# 3. Port Scan Detection
print("[3] Running port scan detection...")
os.system("python3 analyzer/port_scan_detector.py")
time.sleep(1)

# 4. Ask for Real-Time Monitoring
choice = input("\nDo you want to start real-time monitoring? (y/n): ")

if choice.lower() == 'y':
    print("\n[*] Starting real-time monitoring (Press Ctrl+C to stop)...\n")
    os.system("sudo python3 analyzer/realtime_monitor.py")
else:
    print("\n[✔] Analysis completed. Reports generated successfully.")

print("\nCheck the 'reports/' folder for results.")
