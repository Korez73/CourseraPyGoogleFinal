#!/usr/bin/env python3


#This script is step 5 on the final.
#Health check

import psutil
import shutil
import socket

def is_cpu_ok():
    cpu_pct = psutil.cpu_percent()
    is_ok = cpu_pct < 80.0
    return is_ok

def is_diskspace_ok(drive):
    total, used, free = shutil.disk_usage(drive)

    pct_free = (free / total)*100
    is_ok = 20.0 < pct_free
    return is_ok


def is_memory_ok():

    THRESHOLD = 500 # 500MB
    available = int(psutil.virtual_memory().available / (1024*1024))
    is_ok = THRESHOLD < available
    return is_ok


def is_url_resolving():
    ip_addr = socket.gethostbyname("localhost")
    return ip_addr == "127.0.0.1"


def send_email_alert(subject):
    print("Something bad happened:{}".format(subject))

if __name__ == "__main__":
    if not is_cpu_ok():
        send_email_alert("Error - CPU usage is over 80%")

    disk = "C:\\"
    if not is_diskspace_ok(disk):
        send_email_alert("Error - Available disk space is less than 20%")

    if not is_memory_ok():
        send_email_alert("Error - Available memory is less than 500MB")

    if not is_url_resolving():
        send_email_alert("Error - localhost cannot be resolved to 127.0.0.1")

    string = "all done"
