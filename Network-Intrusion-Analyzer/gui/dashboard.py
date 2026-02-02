import tkinter as tk
import os

def run_analysis():
    os.system("sudo python3 analyzer/log_collector.py")
    os.system("python3 analyzer/brute_force_detector.py")
    os.system("python3 analyzer/port_scan_detector.py")
    status.set("✔ Analysis Completed. Reports Generated.")

app = tk.Tk()
app.title("Network Intrusion Log Analyzer")
app.geometry("400x250")

tk.Label(app, text="Cyber Forensics Dashboard", font=("Arial", 16)).pack(pady=15)

tk.Button(app, text="Run Log Analysis", width=25, command=run_analysis).pack(pady=10)

status = tk.StringVar()
tk.Label(app, textvariable=status).pack(pady=10)

app.mainloop()
