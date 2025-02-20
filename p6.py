import heapq

def max_product_of_three_distinct(nums):
    # Use a set to remove duplicates
    nums = list(set(nums))

    if len(nums) < 3:
        raise ValueError("The list must contain at least three distinct numbers.")

    # Use a min-heap to keep track of the three largest elements
    max_heap = []
    
    for num in nums:
        heapq.heappush(max_heap, num)
        if len(max_heap) > 3:
            heapq.heappop(max_heap)

    # Extract the three largest elements
    a, b, c = heapq.heappop(max_heap), heapq.heappop(max_heap), heapq.heappop(max_heap)

    return a * b * c

# Example Usage
nums = [10, 3, 5, 6, 20, 10, 6]
print(max_product_of_three_distinct(nums))  # Output: 1200
