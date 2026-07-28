import keyword

print("Total number of keywords:", len(keyword.kwlist))
print("List of Python keywords:")

for word in keyword.kwlist:
    print(word)
    output:
Total number of keywords: 35
List of Python keywords:
False
None
True
and
as
assert
async
await
break
class
continue
def
del
elif
else
except
finally
for
from
global
if
import
in
is
lambda
nonlocal
not
or
pass
raise
return
try
while
with
yield
