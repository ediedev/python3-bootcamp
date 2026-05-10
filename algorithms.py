# =========================================
# 1. LINEAR SEARCH
# Use Case:
# Searching a student name in an unsorted list
# =========================================

students = ["John", "Sarah", "Mike", "Emma"]

target = "Mike"

for i in range(len(students)):
    if students[i] == target:
        print("Student found at index:", i)
        break



# =========================================
# 2. BINARY SEARCH
# Use Case:
# Searching in a sorted phone contact list
# =========================================

contacts = ["Alice", "Brian", "Cynthia", "David", "Emma"]

target = "David"

left = 0
right = len(contacts) - 1

while left <= right:
    mid = (left + right) // 2

    if contacts[mid] == target:
        print("Contact found at index:", mid)
        break

    elif contacts[mid] < target:
        left = mid + 1

    else:
        right = mid - 1



# =========================================
# 3. BUBBLE SORT
# Use Case:
# Sorting small classroom scores
# =========================================

scores = [45, 12, 89, 33, 67]

for i in range(len(scores)):
    for j in range(len(scores) - i - 1):

        if scores[j] > scores[j + 1]:
            scores[j], scores[j + 1] = scores[j + 1], scores[j]

print("Sorted scores:", scores)



# =========================================
# 4. SELECTION SORT
# Use Case:
# Selecting smallest product prices first
# =========================================

prices = [1200, 300, 750, 150, 500]

for i in range(len(prices)):

    min_index = i

    for j in range(i + 1, len(prices)):
        if prices[j] < prices[min_index]:
            min_index = j

    prices[i], prices[min_index] = prices[min_index], prices[i]

print("Sorted prices:", prices)



# =========================================
# 5. INSERTION SORT
# Use Case:
# Maintaining a live leaderboard
# =========================================

leaderboard = [50, 60, 70, 90, 100]

for i in range(1, len(leaderboard)):

    current = leaderboard[i]
    j = i - 1

    while j >= 0 and leaderboard[j] > current:
        leaderboard[j + 1] = leaderboard[j]
        j -= 1

    leaderboard[j + 1] = current

print("Sorted leaderboard:", leaderboard)



# =========================================
# 6. MERGE SORT
# Use Case:
# Sorting large genomic data records
# =========================================

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


genomic_counts = [500, 120, 900, 300, 450]

sorted_counts = merge_sort(genomic_counts)

print("Sorted genomic counts:", sorted_counts)
