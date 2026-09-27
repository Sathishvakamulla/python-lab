import re

log = input("Enter server log: ")

pattern = r'\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s+(?P<level>\w+)\s+user=(?P<user>\w+)\s+msg="(?P<msg>[^"]*)"'

matches = re.finditer(pattern, log)

for match in matches:
    print("Timestamp:", match.group("timestamp"))
    print("Level:", match.group("level"))
    print("User:", match.group("user"))
    print("Message:", match.group("msg"))
    print()

'''output:
Enter server log: [2024-06-01 08:15:32] ERROR  user=jsmith  msg="Disk quota exceeded" [2024-06-01 08:16:05] INFO   user=agarcia msg="Login successful" [2024-06-01 08:17:44] WARN   user=jsmith  msg="High memory usage"

Timestamp: 2024-06-01 08:15:32
Level: ERROR
User: sai
Message: Disk quota exceeded

Timestamp: 2024-06-01 08:16:05
Level: INFO
User: sathish
Message: Login successful

Timestamp: 2024-06-01 08:17:44
Level: WARN
User: syam
Message: High memory usage
