#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc_len = len(sys.argv) - 1

    if argc_len == 0:
        my_var = 'arguments.'
    elif argc_len == 1:
        my_var = 'argument:'
    else:
        my_var = 'argument:'
    count = 1
    print("{} {}".format(argc_len, my_var))
    for i in sys.argv[1:]:
        print("{} {}".format(count, i))
        count += 1
