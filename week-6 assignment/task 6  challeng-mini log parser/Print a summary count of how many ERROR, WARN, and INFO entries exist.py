import re

log = input("Enter server log: ")

pattern = r'\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s+(?P<level>ERROR|WARN|INFO)\s+user=(?P<user>[A-Za-z0-9_]+)\s+msg="(?P<msg>[^"]*)"'

matches = re.finditer(pattern, log)

error_count = 0
warn_count = 0
info_count = 0

for match in matches:
    level = match.group("level")

    if level == "ERROR":
        error_count += 1
    elif level == "WARN":
        warn_count += 1
    elif level == "INFO":
        info_count += 1

print("ERROR:", error_count)
print("WARN:", warn_count)
print("INFO:", info_count)


'''output:
Enter server log: [2024-06-01 08:15:32] ERROR user=Sathish msg="Disk quota exceeded" [2024-06-01 08:16:05] INFO user=Sathish msg="Login successful" [2024-06-01 08:17:44] WARN user=Sathish msg="High memory usage"

ERROR: 1
WARN: 1
INFO: 1'''
