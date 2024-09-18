def majorityElement(nums):
    count = 0
    candidate = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


nums = [3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]
print(majorityElement(nums))
