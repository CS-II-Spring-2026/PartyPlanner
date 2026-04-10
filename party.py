#DANILO VULANOVIC

# LIST OF THE NAMES FOR PARTY

names = [
    "Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Sophia",
    "William", "Isabella", "James", "Mia", "Benjamin", "Charlotte", "Lucas",
    "Amelia", "Henry", "Harper", "Alexander", "Evelyn", "Michael", "Abigail",
    "Daniel", "Emily", "Matthew", "Ella", "Joseph", "Elizabeth", "Samuel",
    "Camila", "David", "Luna", "Carter", "Sofia", "Owen", "Avery", "Wyatt",
    "Mila", "John", "Aria", "Jack", "Scarlett", "Luke", "Penelope", "Jayden",
    "Layla", "Dylan", "Chloe", "Grayson", "Victoria"
]

# SORTING IN SELECT METHOD

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j].lower() < arr[min_idx].lower():  
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# BINARY SEARCH FUNCTION (case-insensitive)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    found_index = -1
    target = target.lower()

    while low <= high:
        mid = (low + high) // 2
        if arr[mid].lower() == target:
            found_index = mid
            break
        elif arr[mid].lower() < target:
            low = mid + 1
        else:
            high = mid - 1

    return found_index

# MAIN FUNCTION

def main():
    sorted_names = selection_sort(names.copy())

    names.sort()  

    target = input("Put your Target here: ")

    found_index = binary_search(names, target)

    if found_index != -1:
        print(f"Found index is {found_index}")
    else:
        print("Not found")

    print(sorted_names)

# RUN PROGRAM
main()