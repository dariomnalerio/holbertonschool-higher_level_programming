#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argNum = len(argv)
    sum = 0
    for i in range(0, argNum):
        sum += int(argv[i])
    print(sum)