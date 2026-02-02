import time

LOG_FILE = "/var/log/auth.log"

print("[*] Real-Time Monitoring Started (Press Ctrl+C to stop)")

with open(LOG_FILE, "r") as log:
    log.seek(0, 2)

    while True:
        line = log.readline()
        if line:
            if "Failed password" in line:
                print("[ALERT] Failed Login Attempt:", line.strip())
        time.sleep(0.3)
