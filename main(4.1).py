def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return True
    return False

def sentinel_search(arr, key):
    n = len(arr)
    last = arr[n - 1]
    arr[n - 1] = key
    i = 0

    while arr[i] != key:
        i += 1

    arr[n - 1] = last
    if i < n - 1 or arr[n - 1] == key:
        return True
    return False

roll_number = []
n = int(input("Enter number of students: "))
print("Enter Roll numbers: ")
for i in range(n):
    roll_number.append(int(input()))

search_roll = int(input("Enter the roll number to search: "))

print("Using Linear Search:")
if linear_search(roll_number, search_roll):
    print(f"Roll number {search_roll} attended the training program.")
else:
    print(f"Roll number {search_roll} did not attend the training program.")

print("Using Sentinel Search:")
if sentinel_search(roll_number, search_roll):
    print(f"Roll number {search_roll} attended the training program.")
else:
    print(f"Roll number {search_roll} did not attend the training program.")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    