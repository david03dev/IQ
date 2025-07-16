def find_subsets(current, remaining, result):
    if not remaining:
        result.append(current)
        return
    # Include the first element
    find_subsets(current + [remaining[0]], remaining[1:], result)
    # Exclude the first element
    find_subsets(current, remaining[1:], result)

# Given list
data = [5, 6, 2, 8]
result = []
find_subsets([], data, result)

# Print subsets
for s in result:
    print(s)
