# Longest Subarray with Sum = K
arr = [1, 2, 3, 1, 1, 1, 1]
def longest_subarray_with_sum_k(arr, k):
    # Hash map to store the first occurrence of the prefix sum
    prefix_sum_map = {}
    running_sum = 0
    max_len = 0
    
    for i in range(len(arr)):
        running_sum += arr[i]
        
        # If the running sum is equal to k, we found a subarray from index 0 to i
        if running_sum == k:
            max_len = i + 1
        
        # If (running_sum - k) is found in the map, we have a valid subarray
        if (running_sum - k) in prefix_sum_map:
            max_len = max(max_len, i - prefix_sum_map[running_sum - k])
        
        # Store the first occurrence of the running_sum in the map
        if running_sum not in prefix_sum_map:
            prefix_sum_map[running_sum] = i
    
    return max_len
print(longest_subarray_with_sum_k(arr, 3))

# find second largest element in the array
def second_largest(arr):
    if len(arr) < 2:
        return None

    first = arr[0]
    second = arr[1]

    if second > first:
        first, second = second, first

    for i in range(2, len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif first > arr[i] > second: 
            second = arr[i]

    return second

print(second_largest([3, 2, 1, 7, 8, 9]))


# 2. Move Zeros to End
arr = [0, 1, 0, 3, 12]
def move_zeros(arr):
    non_zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0
move_zeros(arr)
print(arr)

# two sum problem

arr = [2, 7, 11, 15]
target = 9
def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1 , len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
print(two_sum(arr, target))


# Unsorted array 

arr = [3, 2, 1, 7, 8, 9]

# short these array withou using sort function

def sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
sort(arr)
print(arr)

# short decending order

def sort_decending(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
sort_decending(arr)
print(arr)



# Arry in python 

arr = [3,2,1,7,8,9]


# element remove 
def remove(arr):
    for i in arr:
        if i == 7:
            arr.remove(i)
remove(arr)
print(arr)


# element search

def sreach(arr):
    for i in arr:
        if i == 7:
            return True
    return False
print(sreach(arr))

# Reverse the array 

print(arr[::-1])

# sum of all elemnets 

def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
print(sum(arr))

# find the length of the array withouy using len 

def lenth(arr):
    count = 0
    for i in arr:
        count += 1
    return count
print(lenth(arr))

# element add withou  using append
def add_element(arr):
    arr += [55]
add_element(arr)

def add(arr):
    arr.append(56)
add(arr)
print(arr)
