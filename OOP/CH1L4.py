def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
    soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"




run_cases = [
    (
        {"damage": 10, "attacks_per_second": 3},
        {"damage": 20, "attacks_per_second": 1},
        "soldier 1 wins",
    ),
    (
        {"damage": 50, "attacks_per_second": 1},
        {"damage": 50, "attacks_per_second": 2},
        "soldier 2 wins",
    ),
]

submit_cases = run_cases + [
    (
        {"damage": 1, "attacks_per_second": 1},
        {"damage": 2, "attacks_per_second": 1},
        "soldier 2 wins",
    ),
    (
        {"damage": 100, "attacks_per_second": 2},
        {"damage": 50, "attacks_per_second": 4},
        "both soldiers die",
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print("Soldier one:")
    print(f"  damage: {input1['damage']}")
    print(f"  attacks_per_second: {input1['attacks_per_second']}")
    print("Soldier two:")
    print(f"  damage: {input2['damage']}")
    print(f"  attacks_per_second: {input2['attacks_per_second']}")
    print(f"Expected: {expected_output}")
    try:
        result = fight_soldiers(input1, input2)
        print(f"Actual:   {result}")
        if result != expected_output:
            print("Fail")
            return False
        actualSoldierOneDps = get_soldier_dps(input1)
        actualSoldierTwoDps = get_soldier_dps(input2)
        expectedSoldierOneDps = input1["damage"] * input1["attacks_per_second"]
        expectedSoldierTwoDps = input2["damage"] * input2["attacks_per_second"]
        if actualSoldierOneDps != expectedSoldierOneDps:
            print(f"Expected soldier one dps: {expectedSoldierOneDps}")
            print(f"Actual soldier one dps:   {actualSoldierOneDps}")
            return False
        if actualSoldierTwoDps != expectedSoldierTwoDps:
            print(f"Expected soldier two dps: {expectedSoldierTwoDps}")
            print(f"Actual soldier two dps:   {actualSoldierTwoDps}")
            return False
        print("Pass")
        return True
    except Exception as e:
        print(f"Error: {e}")
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
