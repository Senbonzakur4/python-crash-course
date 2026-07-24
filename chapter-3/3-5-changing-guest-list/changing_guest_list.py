# 3.5. Changing Guest List

guest_list = ["Khada Jhin", "Aaron Griffin", "Hatsune Miku", "2-D"]
message = "Hello, I'd like to invite you to my dinner tonight,"

print(f"\n{message} {guest_list[0]}.")
print(f"\n{message} {guest_list[1]}.")
print(f"\n{message} {guest_list[2]}.")
print(f"\n{message} {guest_list[3]}.\n")

print(f"Unfortunately, {guest_list[3]} can't make it to the dinner tonight.\n")
guest_list[3] = "Noodle"

print(f"\n{message} {guest_list[0]}.")
print(f"\n{message} {guest_list[1]}.")
print(f"\n{message} {guest_list[2]}.")
print(f"\n{message} {guest_list[3]}.\n")