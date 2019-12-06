#!/usr/bin/env python3

def charcodify(code):
    chars = ''.join([(str(ord(x)) + ",") for x in code])
    chars = chars[0:len(chars)-1]
    return "eval(String.fromCharCode(" + chars + "))"

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Pack javascript code")
    parser.add_argument("code", help="The code you want to pack")

    args = parser.parse_args()

    print(charcodify(args.code))
