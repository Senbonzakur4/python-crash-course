# 10.7 Addition Calculator

print("\nWelcome to the addition calculator!")
while True:

    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}\n")
        if input("Press Enter to exit\n"
                 "Press any other key to continue: ").strip().upper() == '':
            print("Thank you for using the addition calculator. Goodbye!\n")
            break
    except ValueError:
        print("Invalid input! Please enter valid integers.\n")