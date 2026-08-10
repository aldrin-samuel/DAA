import random

comparison_count = 0


def min_max_dc(arr, low, high):
    global comparison_count

    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        comparison_count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    mid = (low + high) // 2

    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)

    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin

    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax

    return overall_min, overall_max


def min_max_naive(arr):
    mn = arr[0]
    mx = arr[0]

    comparisons = 0

    for x in arr[1:]:
        comparisons += 1
        if x < mn:
            mn = x

        comparisons += 1
        if x > mx:
            mx = x

    return mn, mx, comparisons


# ---------- Demo ----------
arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

comparison_count = 0

mn, mx = min_max_dc(arr, 0, len(arr) - 1)
dc_comparisons = comparison_count

_, _, naive_comparisons = min_max_naive(arr)

print("Array:", arr)
print("Minimum:", mn)
print("Maximum:", mx)
print("Divide & Conquer Comparisons:", dc_comparisons)
print("Naive Comparisons:", naive_comparisons)

print("\n{:>8} {:>12} {:>15} {:>18}".format(
    "Size",
    "DC Comps",
    "Naive Comps",
    "Formula (3n/2-2)"
))

print("-" * 60)

for size in [10, 100, 1000, 10000]:
    arr = [random.randint(1, 10000) for _ in range(size)]

    comparison_count = 0

    mn, mx = min_max_dc(arr, 0, len(arr) - 1)
    dc = comparison_count

    _, _, naive = min_max_naive(arr)

    formula = 3 * size // 2 - 2

    print("{:>8} {:>12} {:>15} {:>18}".format(
        size,
        dc,
        naive,
        formula
    ))