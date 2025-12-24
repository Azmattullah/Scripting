# Write a script to list running processes consuming > X% CPU.
# To install psutil, run: pip install psutil


import psutil

CPU_THRESHOLD = 1  # Change X% here

print(f"Processes using more than {CPU_THRESHOLD}% CPU:\n")

for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    try:
        cpu_usage = proc.cpu_percent(interval=0.1)
        if cpu_usage > CPU_THRESHOLD:
            print(f"PID: {proc.pid}, Name: {proc.info['name']}, CPU: {cpu_usage}%")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass



