def simple_interest(principal,rate,time):
    si = (principal*rate*time)/100
    return si
p = int(input("enter principal:"))
r = float(input("enter rate:"))
t = float(input("enter time:"))
result = simple_interest(p,r,t)
print("simple_interest:", result)
output:
enter principal:20000
enter rate:3.6
enter time:2.4
simple_interest: 1728.0

