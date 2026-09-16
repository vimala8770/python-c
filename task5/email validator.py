import re
def is_valid_email(s):
    pattern = r"^[\w.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$"
    return re.fullmatch(pattern, s) is not None
emails = [
    "john@example.com",
    "user.name@gmail.com",
    "test123@yahoo.co",
    "a@b.c",
    "no-at-sign.com",
    "user@domain",
    "@gmail.com",
    "user@domain.toolong"
]

for email in emails:
    print(email, "->", is_valid_email(email))
    output:
john@example.com -> True
user.name@gmail.com -> True
test123@yahoo.co -> True
a@b.c -> False
no-at-sign.com -> False
user@domain -> False
@gmail.com -> False
user@domain.toolong -> False
