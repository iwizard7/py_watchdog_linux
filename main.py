import subprocess
import time

def ping_server(ip_address, count=100):
    command = f"ping -c {count} {ip_address}"
    return subprocess.call(command, shell=True)

def check_connection():
    while True:
        if ping_server('8.8.8.8', count=100) != 0:
            subprocess.call('reboot', shell=True)
        time.sleep(120)

check_connection()
