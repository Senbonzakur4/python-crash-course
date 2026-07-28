# 7.3 Multiples of Ten

multiple = int(input("\nEnter a number, and I'll tell you if it's a multiple of ten: ")
               )

if multiple % 10 == 0:
    print(f"\n{multiple} is a multiple of ten.\n")
else:
    print(f"\n{multiple} is not a multiple of ten.\n")