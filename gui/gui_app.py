import tkinter as tk
from tkinter import messagebox
import threading
from collections import Counter

from analyzer.log_parser import parse_auth_log, parse_ufw_log
from analyzer.detectors import detect_bruteforce, detect_port_scan
from analyzer.visualizer import plot_bar
from analyzer.realtime_monitor import monitor_auth_log, monitor_ufw_log

AUTH_LOG = "logs/auth.log"
UFW_LOG = "logs/ufw.log"

bruteforce_data = Counter()
portscan_data = Counter()
monitoring = False


def realtime_callback(event_type, value):
    if event_type == "bruteforce":
        bruteforce_data[value] += 1
    elif event_type == "portscan":
        portscan_data[value] += 1


def start_monitoring():
    global monitoring
    if monitoring:
        return

    monitoring = True

    threading.Thread(
        target=monitor_auth_log,
        args=(AUTH_LOG, realtime_callback),
        daemon=True
    ).start()

    threading.Thread(
        target=monitor_ufw_log,
        args=(UFW_LOG, realtime_callback),
        daemon=True
    ).start()

    messagebox.showinfo("Monitoring", "Real-time monitoring started")


def show_results():
    brute = detect_bruteforce(list(bruteforce_data.elements()))
    ports = detect_port_scan([int(p) for p in portscan_data.elements()])

    if brute:
        plot_bar(brute, "Real-Time Brute Force Detection", "IP Address", "Attempts")

    if ports:
        plot_bar(ports, "Real-Time Port Scan Detection", "Port", "Hits")

    if not brute and not ports:
        messagebox.showinfo("Status", "No intrusion patterns detected yet")


def analyze_static():
    failed_ips = parse_auth_log(AUTH_LOG)
    ports = parse_ufw_log(UFW_LOG)

    brute = detect_bruteforce(failed_ips)
    scan = detect_port_scan(ports)

    if brute:
        plot_bar(brute, "Static Brute Force Detection", "IP Address", "Attempts")

    if scan:
        plot_bar(scan, "Static Port Scan Detection", "Port", "Hits")


root = tk.Tk()
root.title("Network Intrusion Log Analyzer")
root.geometry("420x300")

tk.Button(root, text="Analyze Logs (Static)", width=25, command=analyze_static).pack(pady=10)
tk.Button(root, text="Start Real-Time Monitoring", width=25, command=start_monitoring).pack(pady=10)
tk.Button(root, text="Show Real-Time Results", width=25, command=show_results).pack(pady=10)

root.mainloop()
