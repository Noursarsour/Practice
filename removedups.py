#Remove Duplicates from Sorted Array
nums = [1,1,2]
def removeDuplicates(nums):
        if not nums:
            return 0
    
    # Initialize a pointer for unique elements
        i = 0
    
    # Traverse the sorted list from the second element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # Found a new unique element
                i += 1             # Move pointer for unique elements
                nums[i] = nums[j]   # Update the element at index i with the unique value
    
    # Return the number of unique elements (i + 1 because i is zero-indexed)
        return i + 1
print(removeDuplicates(nums))