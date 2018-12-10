def input_multiline_float():
    line = int(input())
    result = []

    for _ in range(line):
        result.append([float(s) for s in input().split()])

    return result


def input_multiline_integer():
    line = int(input())
    result = []

    for _ in range(line):
        result.append([int(s) for s in input().split()])

    return result


def input_multiline_string():
    line = int(input())
    result = []

    for _ in range(line):
        result.append(input().split())

    return result


def input_singleline_integer():
    return [int(s) for s in input().split()]


def business_logic(input_data: list):
    print(input_data)
    pass


if __name__ == '__main__':
    input_data = input_singleline_integer()
    # input_data = input_multiline_string()
    # input_data = input_multiline_integer()
    # input_data = input_multiline_float()
    business_logic(input_data)
