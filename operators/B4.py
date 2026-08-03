
percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance %: "))
eligible = percentage > 75 and attendance > 90
print("Eligible for scholarship:", eligible)
OUTPUT:
Enter percentage: 80
Enter attendance %: 95
Eligible for scholarship: True
Enter percentage: 90
Enter attendance %: 85
Eligible for scholarship: False
