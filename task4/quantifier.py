import re
pattern = r"^#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?$"
colors = ["#FFAA00", "#000", "#12AB", "#123456"]
for color in colors:
    if re.fullmatch(pattern, color):
        print(color, "-> Valid")
    else:
        print(color, "-> Invalid")
output:
#FFAA00 -> Valid
#000 -> Valid
#12AB -> Invalid
#123456 -> Valid
