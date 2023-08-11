#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    var_len = len(sys.argv) - 1
    if var_len != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if sys.argv[2] == '+':
        result = add(a, b)
    elif sys.argv[2] == '-':
        result = sub(a, b)
    elif sys.argv[2] == '*':
        result = mul(a, b)
    elif sys.argv[2] == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))
