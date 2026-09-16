import re
log = '[2024-06-01 08:15:32] ERROR  user=jsmith  msg="Disk quota exceeded"'
pattern = r'^\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s+(?P<level>ERROR|WARN|INFO)\s+user=(?P<user>\w+)\s+msg="(?P<msg>[^"]*)"$'
match = re.match(pattern, log)
print(match.groupdict())
output:
{'timestamp': '2024-06-01 08:15:32', 'level': 'ERROR', 'user': 'jsmith', 'msg': 'Disk quota exceeded'}
