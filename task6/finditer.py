import re
log = """[2024-06-01 08:15:32] ERROR  user=jsmith  msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO   user=agarcia msg="Login successful"
[2024-06-01 08:17:44] WARN   user=jsmith  msg="High memory usage"
"""
pattern = r'^\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s+(?P<level>ERROR|WARN|INFO)\s+user=(?P<user>\w+)\s+msg="(?P<msg>[^"]*)"$'
entries = []
for match in re.finditer(pattern, log, re.MULTILINE):
    entries.append(match.groupdict())
print(entries)
