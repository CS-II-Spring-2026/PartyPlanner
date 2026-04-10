names = [
    "Olivia", "Liam", "Emma", "Noah", "Ava", "Sophia", "Mason", "Isabella", "Ethan", "Mia",
    "Lucas", "Charlotte", "Amelia", "Harper", "Elijah", "Evelyn", "James", "Abigail", "Benjamin", "Emily",
    "Alexander", "Ella", "Henry", "Scarlett", "Jackson", "Grace", "Sebastian", "Chloe", "Aiden", "Victoria",
    "Matthew", "Riley", "Samuel", "Aria", "David", "Lily", "Joseph", "Aubrey", "Carter", "Zoey",
    "Owen", "Penelope", "Wyatt", "Layla", "John", "Lillian", "Jack", "Nora", "Luke", "Hazel"
]

def SearchName():
    target = input("Enter a name to search for: ")
    low = 0
    high = len(names) - 1
    found_index = -1
    for i in range(len(names)):
        if names[i] == target:
            found_index = i+1
            break

    if found_index != -1:
        print(f"Name in the Group: {found_index}/50")
    else:
        print("Not found")

#Sort the data using Bubble Sort
def BubbleSort(names):
    n = len(names)

    for i in range(n):
        for j in range (n-i-1):
            if names[j] > names[j+1]:
                temp = names[j]
                names[j] = names[j+1]
                names[j+1] = temp
    print(f"Sorted Names: {names}")



#Use Binary Search to find the target
def BinarySearch(array):
    target = input("Enter a name to search for: ")
    low = 0
    high = len(array) - 1
    found_index = -1
    for i in range(len(names)):
        if names[i] == target:
            found_index = i+1
            break

    if found_index != -1:
        print(f"Name in the Group: {found_index}/50")
    else:
        print("Not found")


#Menu to show the names in the group
flag = True
while flag == True:
    print("----Selection Menu----")
    print("----Make a selection----")
    print("1. See the names in the group")
    print("2. Sort the names in the group")
    print("3. Search for a name in the group")
    print("4. Quit")
    selection = input("Enter your selection: ")

    #Selections and what they go to
    if selection == "1":
        SearchName()
    elif selection == "2":
        BubbleSort(names)   
    elif selection == "3":
        BinarySearch(names)
    elif selection == "4":
        flag = False
        print("Goodbye!")