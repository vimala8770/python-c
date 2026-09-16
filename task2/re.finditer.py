import re
paragraph = "NASA and USA are working with ISRO on a successful space mission."
for match in re.finditer(r"\b[A-Za-z]{7,}\b", paragraph):
    print(match.group(), match.start())
    output:
working 17
successful 40
mission 57
