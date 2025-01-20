def liner_search(nums, num):
    cnt = 0
    for i in range(len(nums)):
        cnt += 1
        if nums[i] == num:
            return i, cnt



def binary_search(nums, num):
    low = 0
    high = len(nums) - 1
    cnt = 0

    while low <= high:
        cnt += 1
        mid = (low + high) // 2
        guess = nums[mid]

        if guess < num:
            low = mid + 1
        elif guess > num:
            high = mid - 1
        else:
            return mid, cnt

nums = [1, 5, 45, 32, 56, 14, 70, 90, 82, 100, 101, 110, 200]
nums.sort()

print(liner_search(nums, 101))
print(binary_search(nums, 101))



