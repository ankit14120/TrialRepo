import shutil
import os

LOG_DIR = "../logs"

def collect_logs():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    shutil.copy("/var/log/auth.log", f"{LOG_DIR}/auth.log")
    shutil.copy("/var/log/syslog", f"{LOG_DIR}/syslog")

    print("[+] Logs collected successfully")

if __name__ == "__main__":
    collect_logs()
