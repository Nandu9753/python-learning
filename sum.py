def two_sum(nums, sum):
    num_indices = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = sum - num

        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i

    # If no solution is found
    return None

# Example usage
nums = [2, 7, 11, 15]
sum = 13
result = two_sum(nums, sum)
print(result)  # Output: [0, 1]
