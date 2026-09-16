import re
def clean_text(html):
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", html)
    # Collapse spaces, tabs, and newlines
    text = re.sub(r"\s+", " ", text)
    # Remove spaces from beginning and end
    return text.strip()
html = """
<p>Hello    world!</p>
<b>This is a test.</b>
    Welcome to <i>Python</i>.
"""
print(clean_text(html))
output:
Hello world! This is a test. Welcome to Python.

