import re
def check_password(pw):
    failed = []
    if len(pw) < 8:
        failed.append("At least 8 characters")
    if not re.search(r"[A-Z]", pw):
        failed.append("At least one uppercase letter")
    if not re.search(r"[a-z]", pw):
        failed.append("At least one lowercase letter")
    if not re.search(r"\d", pw):
        failed.append("At least one digit")
    if not re.search(r"[!@#$%^&*]", pw):
        failed.append("At least one symbol from !@#$%^&*")
    return failed
passwords = [
    "Hello@123",
    "hello123",
    "HELLO@123",
    "HelloWorld",
    "Hi@1"
]
for password in passwords:
    result = check_password(password)
    if not result:
        print(password, "-> Strong password")
    else:
        print(password, "-> Failed:",result)
        output:
Hello@123 -> Strong password
hello123 -> Failed: ['At least one uppercase letter', 'At least one symbol from !@#$%^&*']
HELLO@123 -> Failed: ['At least one lowercase letter']
HelloWorld -> Failed: ['At least one digit', 'At least one symbol from !@#$%^&*']
Hi@1 -> Failed: ['At least 8 characters']

