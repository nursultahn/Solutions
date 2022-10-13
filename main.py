from leetcode import Solutions as sl


def print_hello_world(name):
    print(f'Hello {name}')


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    operations = ["++X", "++X", "X++"]
    val = sl.finalValueAfterOperations(operations=operations)
    print(val)
