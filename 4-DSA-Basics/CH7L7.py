def is_balanced(input_str):
    open_paren = 0
    close_paren = 0

    s = Stack()
    
    for ch in input_str:
        s.push(ch)

    for i in range(s.size()):
        
        if s.peek() == "(":
            open_paren += 1

        if s.peek() == ")":
            close_paren += 1

        s.pop()

    return open_paren == close_paren

# 

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def pop(self):
        if len(self.items) == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item

# 

run_cases = [
    ("(", False),
    ("()", True),
    ("(())", True),
]

submit_cases = run_cases + [
    ("()()", True),
    ("(()))", False),
    ("((())())", True),
    ("(()(()", False),
    (")(", False),
    (")()(()", False),
    ("())(()", False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expected: {expected_output}")
    result = is_balanced(input1)
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
