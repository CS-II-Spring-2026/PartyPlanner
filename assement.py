# names list
names = [
"Olivia", "Liam", "Emma", "Noah", "Ava", "Sophia", "Mason", "Isabella", "Ethan", "Mia",
"Lucas", "Charlotte", "Amelia", "Harper", "Elijah", "Evelyn", "James", "Abigail", "Benjamin", "Emily",
"Alexander", "Ella", "Henry", "Scarlett", "Jackson", "Grace", "Sebastian", "Chloe", "Aiden", "Victoria",
"Irhad", "Dominic", "Bah", "Aria", "David", "Lily", "Joseph", "Aubrey", "Carter", "Zoey",
"Owen", "Penelope", "Wyatt", "Layla", "John", "Lillian", "Jack", "Nora", "Luke", "Hazel"
]

# sorting
n = len(names)

for i in range(n):
    for j in range(0, n - i - 1):
        if names[j] > names[j + 1]:
            temp = names[j]
            names[j] = names[j + 1]
            names[j + 1] = temp

print("Sorted Guest List:")
print(names)

# search input
search_name = input("Enter a name to search for: ")

# search setup
low = 0
high = len(names) - 1
found = False

# search loop
while low <= high:
    mid = (low + high) // 2

    if names[mid] == search_name:
        print(search_name, "is on the guest list at position", mid)
        found = True
        break
    elif names[mid] > search_name:
        high = mid - 1
    else:
        low = mid + 1

# not found
if found == False:
    print(search_name, "is NOT on the guest list")