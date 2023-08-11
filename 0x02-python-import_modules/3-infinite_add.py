#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    for i in sys.argv[1:]:
        count = count + int(i)
    print("{:d}".format(count))
