import re

pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"

print(re.fullmatch(pattern, "_count2"))
print(re.fullmatch(pattern, "2fast"))
print(re.fullmatch(pattern, "total_sum"))
output:
<re.Match object; span=(0, 7), match='_count2'>
None
<re.Match object; span=(0, 9), match='total_sum'>

