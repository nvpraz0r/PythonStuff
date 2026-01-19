import time

def merge_sort(nums):
    # if the length of nums is less than 2, it's already sorted so return it
    if len(nums) < 2:
        return nums
    # split the array into two halves down the middle
    # call merge_sort() twice, once on each half
    first = merge_sort(nums[: len(nums) // 2])
    second = merge_sort(nums[len(nums) // 2 :])
    # return the result of calling merge (sorted left side, sorted right side) on the results of the merge sort calls
    return merge(first, second)

def merge(first, second):
    # create a new final list of integers
    final = []
    # set i and j equal to zero
    # they will be used to keep track of indexes in the input lists
    i , j = 0 , 0
    # use a loop to compare the current elements of first and second
    while i < len(first) and j < len(second):
        # if an element in first is less than or equal to its respective element in second
        # add it to the final list and increment i
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        # otherwise add the item in second to the final list and increment j        
        else:
            final.append(second[j])
            j += 1
    # after comparing all the items there may be some items left over
    # in either first or second add those extra items to the final list
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    # return the final list
    return final


# 
# 
# 


run_cases = [([3, 2, 1], [1, 2, 3]), ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])]

submit_cases = run_cases + [
    ([], []),
    ([7], [7]),
    ([4, -7, 1, 0, 5], [-7, 0, 1, 4, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expected: {expected_output}")
    start = time.time()
    result = merge_sort(input1)
    end = time.time()
    timeout = 1.00
    if (end - start) < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
        if result == expected_output:
            print(f"Actual: {result}")
            print("Pass")
            return True
        print(f"Actual: {result}")
        print("Fail")
        return False
    else:
        print(f"test took longer than {timeout * 1000} milliseconds!")
        print(f"Actual: {result}")
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
