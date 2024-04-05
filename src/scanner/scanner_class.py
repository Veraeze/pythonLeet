import sys


class Scanner:
    def nextInt(self):
        return int(sys.stdin.readline())

    def nextDouble(self):
        return float(sys.stdin.readline())

    def nextLine(self):
        return str(sys.stdin.readline().strip())
