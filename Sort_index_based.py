arr = [9, 2, 5, 8, 6, 4, 7, 3]

# Step 1: Extract subarray from index 2 to 5
sub = arr[2:6]  # [5, 8, 6, 4]

# Step 2: Sort the subarray
sub.sort()  # [4, 5, 6, 8]

# Step 3: Replace the original array's slice
arr[2:6] = sub

print("Updated array:", arr)
