# 10.6 Addition 

try:
    num1 = int(input("\nEnter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}\n")
except ValueError:
    print("Invalid input! Please enter valid integers.\n")