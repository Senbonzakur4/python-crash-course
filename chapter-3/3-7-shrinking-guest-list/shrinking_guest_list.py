# 3.7. Shrinking Guest List

guest_list = ["Khada Jhin", "Aaron Griffin", "Hatsune Miku", "2-D"]
message = "Hello, I'd like to invite you to my dinner tonight,"
uninvited = ""

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

print(f"\n{message} {guest_list[0]}.") # Chemon
print(f"\n{message} {guest_list[1]}.") # Khada Jhin
print(f"\n{message} {guest_list[2]}.") # Karely
print(f"\n{message} {guest_list[3]}.") # Aaron Griffin
print(f"\n{message} {guest_list[4]}.") # Hatsune Miku
print(f"\n{message} {guest_list[5]}.") # Noodle
print(f"\n{message} {guest_list[6]}.\n") # Geralt of Rivia

print(f"\nThe dinner table that I bought won't arrive in time for the dinner so I can only invite two guests.")
uninvited = guest_list.pop(3)
print(f"\nI'm sorry, {uninvited}, but you can't come to dinner tonight.")
uninvited = guest_list.pop(1)
print(f"\nI'm sorry, {uninvited}, but you can't come to dinner tonight.")
uninvited = guest_list.pop(4)
print(f"\nI'm sorry, {uninvited}, but you can't come to dinner tonight.")
uninvited = guest_list.pop(3)
print(f"\nI'm sorry, {uninvited}, but you can't come to dinner tonight.")
uninvited = guest_list.pop(0)
print(f"\nI'm sorry, {uninvited}, but you can't come to dinner tonight.")

print(f"\nYou're still invited, {guest_list[0]}.")
print(f"\nYou're still invited, {guest_list[1]}.")

del guest_list[0]
del guest_list[0]

print(f"\n{guest_list}\n")

