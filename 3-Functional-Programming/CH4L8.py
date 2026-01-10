# directions
# 1. create an integer variable to keep track of the total size
# 2. for each item i nthe list (use a loop here):
#       a. if the item is an int, add it to the total size
#       b. if the item is a list use the recursive call to "sum_nested_list"
#           to get the size of the that list. Add that size to the total size.
# 3. return the total sieze when you're done iterating
# 
# tips
# 
# 
# 
def sum_nested_list(lst):
    pass


run_cases = [
    ([1, 2, [3, 4]], 10),
    ([5, [6, 7], [[8, 9], 10]], 45),
]

submit_cases = run_cases + [
    ([], 0),
    ([1, [2], [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]], 55),
]


def test(input_list, expected_output):
    print("---------------------------------")
    print(f"Input list: {input_list}")
    print(f"Expected output: {expected_output}")
    result = sum_nested_list(input_list)
    print(f"Actual output: {result}")
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
