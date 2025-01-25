def findDuplicates(nums):
    result = []

    for num in nums:
        if nums.count(num) > 1:
            result.append(num)

    return result

def removeDuplicates(nums):
    return list(set(nums))


def countOccurrences(nums):
    return {num: nums.count(num) for num in set(nums)}