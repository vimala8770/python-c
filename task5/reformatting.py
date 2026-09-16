import re
text = """
My birthday is 15/08/2002.
The meeting is on 25/12/2024.
The project started on 01/01/2025.
"""
pattern = r"(\d{2})/(\d{2})/(\d{4})"
dates = re.findall(pattern, text)
print("Extracted dates:")
for date in dates:
    print(date)
new_text = re.sub(pattern, r"\3-\2-\1", text)
print("\nReformatted text:")
print(new_text)
output:
Extracted dates:
('15', '08', '2002')
('25', '12', '2024')
('01', '01', '2025')

Reformatted text:

My birthday is 2002-08-15.
The meeting is on 2024-12-25.
The project started on 2025-01-01.


