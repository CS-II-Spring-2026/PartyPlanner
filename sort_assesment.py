#Jakub Novak
#Name list of 50 names
names = [
    "Olivia", "Liam", "Emma", "Noah", "Ava", "Sophia", "Mason", "Isabella", "Ethan", "Mia",
    "Lucas", "Charlotte", "Amelia", "Harper", "Elijah", "Evelyn", "James", "Abigail", "Benjamin", "Emily",
    "Alexander", "Ella", "Henry", "Scarlett", "Jackson", "Grace", "Sebastian", "Chloe", "Aiden", "Victoria",
    "Matthew", "Riley", "Samuel", "Aria", "David", "Lily", "Joseph", "Aubrey", "Carter", "Zoe",
    "Owen", "Penelope", "Wyatt", "Layla", "John", "Lillian", "Jacob", "Nora", "Luke", "Hazel"
]

#Sort the list of names in order
def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                # swap
                list[j], list[j + 1] = list[j + 1], list[j]

#Search for a name in the list
def search(list, target):
    low = 0
    high = len(list) - 1

    target = target.lower()

    while low <= high:
        mid = (low + high) // 2
        mid_value = list[mid].lower()

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
#Sort the list of names and search for a name
bubble_sort(names)
#Ask the user for a name to search
search_result = input("Enter a name to search: ")

result = search(names, search_result)
#Print the result of the search
if result != -1:
    #If the name is found, print the name
    print(search_result, "is on the list!")
else:
    #If the name is not found, print "not found"
    print(search_result, "is NOT on the list.")