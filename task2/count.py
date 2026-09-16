import re
prices = "apples: $3.50, bananas: $1.20, mango: $4.75"
result = re.findall(r"\$\d+\.\d+", prices)
print("Number of prices:", len(result))
output:
Number of prices: 3
