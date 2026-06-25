import time
import random


def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and target >= arr[low] and target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if arr[pos] == target:
            return pos, comparisons

        elif arr[pos] < target:
            low = pos + 1

        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():
    sizes = [1000, 5000, 10000, 50000, 100000]

    print("\nPerformance Comparison")
    print("-" * 75)
    print(
        f"{'Size':<10}"
        f"{'IS Time(ms)':<15}"
        f"{'BS Time(ms)':<15}"
        f"{'IS Comparisons':<18}"
        f"{'BS Comparisons':<18}"
    )
    print("-" * 75)

    for size in sizes:

        arr = list(range(size))
        target = random.choice(arr)

        # Interpolation Search Timing
        start = time.perf_counter()

        for _ in range(100):
            idx_is, comp_is = interpolation_search(arr, target)

        is_time = (time.perf_counter() - start) * 1000 / 100

        # Binary Search Timing
        start = time.perf_counter()

        for _ in range(100):
            idx_bs, comp_bs = binary_search(arr, target)

        bs_time = (time.perf_counter() - start) * 1000 / 100

        print(
            f"{size:<10}"
            f"{is_time:<15.6f}"
            f"{bs_time:<15.6f}"
            f"{comp_is:<18}"
            f"{comp_bs:<18}"
        )


# Main Program
arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
target = 35

index, comparisons = interpolation_search(arr, target)

print("Array:", arr)
print("Searching for:", target)

if index != -1:
    print("Element found at index:", index)
    print("Comparisons:", comparisons)
else:
    print("Element not found")

performance_analysis()