#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) <= 1:
        print("0 arguments.")
    elif len(argv) > 1:
        if len(argv) == 2:
            counter = 0
            counting = 0
            for i in argv[1:]:
                counter += 1
            print("{} argument:".format(counter))
            for i in argv[1:]:
                counting += 1
                print("{0}: {1}".format(counting, i))
        elif len(argv) > 2:
            counter = 0
            counting = 0
            for i in argv[1:]:
                counter += 1
            print("{} arguments:".format(counter))
            for i in argv[1:]:
                counting += 1
                print("{0}: {1}".format(counting, i))
