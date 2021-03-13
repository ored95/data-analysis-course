#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, start) -> None:
        self.start = start

    def write(self, msg):
        print('{0}{1}'.format(self.start, msg))

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
