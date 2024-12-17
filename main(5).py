# Function for Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Function for Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Input Percentages
percentages = []
n = int(input("Enter the number of students: "))
if n <= 0:
    print("Number of students must be greater than 0.")
else:
    print("Enter the first-year percentages of students:")
    for _ in range(n):
        percentages.append(float(input()))

    # Perform Selection Sort
    selection_sorted = percentages[:]
    selection_sort(selection_sorted)
    print("\nTop 5 scores after Selection Sort:")
    print(selection_sorted[-5:]if len(selection_sorted) >= 5 else selection_sorted[::-1])

    # Perform Bubble Sort
    bubble_sorted = percentages[:]
    bubble_sort(bubble_sorted)
    print("\nTop 5 scores after Bubble Sort:")
    print(bubble_sorted[-5:] if len(bubble_sorted) >= 5 else bubble_sorted[::-1])
