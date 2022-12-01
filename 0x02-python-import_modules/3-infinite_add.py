#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    counting = 0
    for i in range(1, len(argv)):
        counting += int(argv[i])
    print(counting)
