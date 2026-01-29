# X. Lorem Ipsum
#
# lorem ipsum dolor sit amet
#
# lorem ipsum dolor sit amet
#
def twoSumBruteForce(nums: List[int], target: int) -> List[int]:
    """
    Time: O(n^2)
    :param nums:
    :type nums:
    :param target:
    :type target:
    :return:
    :rtype:
    """

    # main loop through nums
    for i in range(len(nums)):
        # loop through a second time
        for j in range(i + 1, len(nums)):
            # determine if the sum of i and j equal the target
            if nums[i] + nums[j] == target:
                # return the indices when a valid combo found
                return [i, j]

    # return nothing if failed to find valid combo
    return [0,0]


# secondary solution (more efficient)
def twoSumHashMap(nums: List[int], target: int) -> List[int]:
    """
    Time: O(n)
    :param nums:
    :type nums:
    :param target:
    :type target:
    :return:
    :rtype:
    """

    # create the dictionary (hashmap)
    map = {}

    # populate the map
    for i, n in enumerate(nums):
        map[n] = i

    for i, n in enumerate(nums):
        diff = target - n
        if diff in map and map[diff] != i:
            return [i, map[diff]]

    return []

def main():
    # 
    nums = [2,11,15,13,19,23,25,33,31,41,51,61,71,81,91,101,201,301,401,7]
    target = 9

    result = twoSumHashMap(nums, target)

    print(result)


if __name__ == '__main__':
    main()