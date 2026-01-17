# for i in range(end - 1):
#     for j in range(end - i - 1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
# return nums



# less confusing version
def bubble_sort(nums):
    # set "swapping" to true
    swapping = True
    # set "end" to the length of the input list
    end = len(nums) - 1

    # while "swapping" is True
    while swapping:
        # set "swapping" to False
        swapping = False
        # for "i" from the first element to "end"
        for i in range(0, end):
            # if the "i"th element of the input list is greater than "i"th element:
            if nums[i] > nums[i + 1]:
                # swap the "i"th element and the "i+1"th element
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # set "swapping" to True
                swapping = True
    # return sorted list
    return nums

# still trying to figure out how this is supposed to be implemented
def confusing_bubble_sort(nums):

    swapping = True
    end = len(nums)

    while swapping:
        swapping = False
        for i in range(2, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1
    return nums


run_cases = [
    ([5, 7, 3, 6, 8], [3, 5, 6, 7, 8]),
    ([2, 1], [1, 2]),
]

submit_cases = run_cases + [
    ([], []),
    ([1], [1]),
    ([1, 5, -3, 2, 4], [-3, 1, 2, 4, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 3, 2, 5, 4], [1, 2, 3, 4, 5]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input:\n * {input1}")
    print(f"Expected: {expected_output}")
    result = bubble_sort(input1)
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
