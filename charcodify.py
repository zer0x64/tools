#!/usr/bin/env python3

def charcodify(code: str):
    chars = ''.join([(str(ord(x)) + ",") for x in code])
    chars = chars[0:len(chars)-1]
    return "eval(String.fromCharCode(" + chars + "))"

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Pack javascript code")
    parser.add_argument("code",
        nargs="?",
        default=sys.stdin,
        help="The code you want to pack")

    args = parser.parse_args()

    if isinstance(args.code, str):
        code = args.code
    else:
        code = args.code.read()

    print(charcodify(code))
