def fizz_buzz(n: int) -> List[str]:
    
    result = []

    # 
    for i in range(n):
        # 
        num = i + 1

        # 
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        # 
        elif num % 3 == 0:
            result.append("Fizz")
        # 
        elif num % 5 == 0:
            result.append("Buzz")
        # 
        else:
            result.append(str(num))

    # 
    return result


def main():
    fizz_buzz(5)


if __name__ == '__main__':
    main()