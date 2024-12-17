def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def get_top_five(scores):
    return scores[-1:-6:-1]  # Get the last 5 elements in reverse order

def main():
    n = int(input("Enter the number of students: "))
    percentages = []

    print("Enter the second-year percentages of students:")
    for _ in range(n):
        percentages.append(float(input()))

    # Insertion Sort
    insertion_sorted = percentages[:]
    insertion_sort(insertion_sorted)
    print("\nPercentages sorted using Insertion Sort:", insertion_sorted)
    print("Top five scores:", get_top_five(insertion_sorted))

    # Shell Sort
    shell_sorted = percentages[:]
    shell_sort(shell_sorted)
    print("\nPercentages sorted using Shell Sort:", shell_sorted)
    print("Top five scores:", get_top_five(shell_sorted))

if __name__ == "__main__":
    main()