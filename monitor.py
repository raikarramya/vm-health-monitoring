import psutil
from alert import send_alert
from service_recovery import recover_service
from config import *

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

if cpu > CPU_THRESHOLD:
    send_alert(f"High CPU Usage: {cpu}%")

if memory > MEMORY_THRESHOLD:
    send_alert(f"High Memory Usage: {memory}%")

if disk > DISK_THRESHOLD:
    send_alert(f"High Disk Usage: {disk}%")

for service in SERVICES:
    recover_service(service)
