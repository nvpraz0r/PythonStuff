class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        pass

    # don't touch below this line

    def fortify(self):
        self.armor *= 2




run_cases = [(Wall(), [50, 100, 200])]

submit_cases = run_cases + [
    (Wall(), [50, 100, 200, 400, 800, 1600, 3200]),
]


def test(wall, expected_outputs):
    print("---------------------------------")
    actual_outputs = []
    for _ in expected_outputs:
        cost = wall.get_cost()
        actual_outputs.append(cost)
        print(f"Wall cost: {cost}")
        wall.fortify()
        print("fortifying wall...")
    print(f"Expected: {expected_outputs}")
    print(f"Actual:   {actual_outputs}")

    if actual_outputs == expected_outputs:
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
