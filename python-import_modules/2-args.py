#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    print("{} argument{}{}".format(n, "" if n == 1 else "s",
                                   ":" if n > 0 else "."))
    for i in range(1, n + 1):
        print("{}: {}".format(i, sys.argv[i]))
