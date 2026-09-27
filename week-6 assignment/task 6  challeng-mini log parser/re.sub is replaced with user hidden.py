import re

log = input("Enter server log: ")

result = re.sub(r"user=[A-Za-z0-9_]+", "user=<hidden>", log)

print(result)


'''output:
Enter server log: [2024-06-01 08:15:32] ERROR user=Sathish msg="Disk quota exceeded" [2024-06-01 08:16:05] INFO user=Sathish msg="Login successful" [2024-06-01 08:17:44] WARN user=Sathish msg="High memory usage"

[2024-06-01 08:15:32] ERROR user=<hidden> msg="Disk quota exceeded" [2024-06-01 08:16:05] INFO user=<hidden> msg="Login successful" [2024-06-01 08:17:44] WARN user=<hidden> msg="High memory usage"'''
