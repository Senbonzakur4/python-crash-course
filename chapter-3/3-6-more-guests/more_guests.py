# 3.6. More Guests

guest_list = ["Khada Jhin", "Aaron Griffin", "Hatsune Miku", "2-D"]
message = "Hello, I'd like to invite you to my dinner tonight,"

print(f"\n{message} {guest_list[0]}.")
print(f"\n{message} {guest_list[1]}.")
print(f"\n{message} {guest_list[2]}.")
print(f"\n{message} {guest_list[3]}.\n")

print(f"\nUnfortunately, {guest_list[3]} can't make it to the dinner tonight.")
guest_list[3] = "Noodle"

print(f"\n{message} {guest_list[0]}.")
print(f"\n{message} {guest_list[1]}.")
print(f"\n{message} {guest_list[2]}.")
print(f"\n{message} {guest_list[3]}.\n")

print(f"\nI found a bigger table for the dinner.")
guest_list.insert(0, "Chemon" )
guest_list.insert(2, "Karely")
guest_list.append("Geralt of Rivia")

print(f"\n{message} {guest_list[0]}.")
print(f"\n{message} {guest_list[1]}.")
print(f"\n{message} {guest_list[2]}.")
print(f"\n{message} {guest_list[3]}.")
print(f"\n{message} {guest_list[4]}.")
print(f"\n{message} {guest_list[5]}.")
print(f"\n{message} {guest_list[6]}.\n")
