def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False


def fibonacci_search(arr, key):
    n = len(arr)
    fib_m_2 = 0  # (m-2)'th Fibonacci number
    fib_m_1 = 1  # (m-1)'th Fibonacci number
    fib = fib_m_1 + fib_m_2  # m'th Fibonacci number

    # Find the smallest Fibonacci number greater than or equal to n
    while fib < n:
        fib_m_2 = fib_m_1
        fib_m_1 = fib
        fib = fib_m_1 + fib_m_2

    offset = -1

    # Perform the search
    while fib > 1:
        # Check if fib_m_2 is a valid index
        i = min(offset + fib_m_2, n - 1)

        if arr[i] < key:
            fib = fib_m_1
            fib_m_1 = fib_m_2
            fib_m_2 = fib - fib_m_1
            offset = i
        elif arr[i] > key:
            fib = fib_m_2
            fib_m_1 = fib_m_1 - fib_m_2
            fib_m_2 = fib - fib_m_1
        else:
            return True

    # Compare the last element with key
    if fib_m_1 and offset + 1 < n and arr[offset + 1] == key:
        return True

    return False


# Input Roll Numbers in Sorted Order
roll_numbers = []
n = int(input("Enter the number of students: "))
print("Enter roll numbers (sorted order):")
for _ in range(n):
    roll_numbers.append(int(input()))

# Input Search Roll Number
search_roll = int(input("Enter the roll number to search: "))

# Perform Searches
print("Using Binary Search:")
if binary_search(roll_numbers, search_roll):
    print(f"Roll number {search_roll} attended the training program.")
else:
    print(f"Roll number {search_roll} did not attend the training program.")

print("Using Fibonacci Search:")
if fibonacci_search(roll_numbers, search_roll):
    print(f"Roll number {search_roll} attended the training program.")
else:
    print(f"Roll number {search_roll} did not attend the training program.")

    