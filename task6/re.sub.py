import re

log = """[2024-06-01 08:15:32] ERROR  user=jsmith  msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO   user=agarcia msg="Login successful"
[2024-06-01 08:17:44] WARN   user=jsmith  msg="High memory usage"
"""

redacted_log = re.sub(r'user=\w+', 'user=<hidden>', log)

print(redacted_log)
output:
[2024-06-01 08:15:32] ERROR  user=<hidden>  msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO   user=<hidden> msg="Login successful"
[2024-06-01 08:17:44] WARN   user=<hidden>  msg="High memory usage"


