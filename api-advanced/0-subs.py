#!/usr/bin/python3
"""
0-main
"""
import sys
from subprocess import check_output

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = check_output(["./0-subs.py", subreddit]).decode("utf-8").strip()
        print(result)
