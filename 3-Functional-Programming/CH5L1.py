def get_logger(formatter):
    # 1 define a new function "logger" inside "get_logger"
    # "logger" accepts two strings
    def logger(first, second):
        # 2 logger function should not return anything
        # it should print the result of calling the given formatter function
        # with the first and second strings as arguments
        print(formatter(first, second))

    # 3 return logger function
    return logger


# Don't edit below this line


def test(first, errors, formatter):
    print("Logs:")
    logger = get_logger(formatter)
    for err in errors:
        logger(first, err)
    print("====================================")


def colon_delimit(first, second):
    return f"{first}: {second}"


def dash_delimit(first, second):
    return f"{first} - {second}"


def main():
    db_errors = [
        "out of memory",
        "cpu is pegged",
        "networking issue",
        "invalid syntax",
    ]
    test("Doc2Doc FATAL", db_errors, colon_delimit)

    mail_errors = [
        "email too large",
        "non alphanumeric symbols found",
    ]
    test("Doc2Doc WARNING", mail_errors, dash_delimit)


main()
