#!/usr/bin/python3
import sys
from calculator_1 import add, mul, sub, div
if __name__ == "__main__":
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <opearator> <b>")
        sys.exit(1)
    else:
        if args[2] != '*' and args[2] != '+' amd args[2] != '-' and args[2] != '/'):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            a = int(args[1])
            b = int(args[3])
            mth = 0
            if args[2] == '+':
                mth = add(a, b)
            elif args[2] == '-':
                mth = sub(a, b)
            elif args[2] == '*':
                mth = mul(a, b)
            else:
                mth = div(a, b)
            print("{} {} {} = {}".format(a, args[2], b, mth))
