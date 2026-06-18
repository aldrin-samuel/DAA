array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_value = int(input("Enter the element to search for: "))
for i in range(len(array)):
    if array[i] == input_value:
        print(f"Element found at index: {i}")
        break
else:    print("Element not found in the array.")