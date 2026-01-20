def selection_sort(nums):

    # for each index
    for i in range(len(nums)):
        # set smallest_idx to the current index
        smallest_idx = i
        # for each index from i + 1 to the end of the list
        for j in range(i + 1, len(nums)):
            # if the number at the inner index is smaller than the number at "smallest_idx"
            if nums[j] < nums[smallest_idx]:
                # set "smallest_idx" to the inner index
                smallest_idx = j
        # swap the number at the outer loop index with the number at "smallest_idx"
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    # return the sorted list
    return nums


# 
# 
# 


run_cases = [
    ([5, 3, 8, 6, 1, 9], [1, 3, 5, 6, 8, 9]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
]

submit_cases = run_cases + [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([15, 12, 8, 7, 5, 3, 1], [1, 3, 5, 7, 8, 12, 15]),
    ([10, 5, 3, 7, 2, 8, 1], [1, 2, 3, 5, 7, 8, 10]),
    ([], []),
    ([1], [1]),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input}")
    print(f"Expected: {expected_output}")
    result = selection_sort(input)
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
