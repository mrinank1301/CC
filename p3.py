# logic
def find_next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)
    print(result)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result

# main
arr = []
for i in range(5):
    arr.append(int(input("Enter the number: ")))

arr1 = find_next_greater_element(arr)
print(arr1)