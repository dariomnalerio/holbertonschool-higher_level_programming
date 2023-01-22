#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argNum = len(argv)
    if argNum == 0:
        print('0 arguments.')
    elif argNum == 1:
        print('1 argument: {}' .format(argv[0]))
    else:
        print('{} arguments:' .format(argNum))
    for i, arg in enumerate(argv, start=1):
        print('{}: {}'.format(i, arg))
