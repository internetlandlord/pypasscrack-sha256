#!/bin/python3

from pwn import *
import sys

# input checker - very rudimentary validation
if len(sys.argv) != 2:
    print("Invalid argument.")
    print(">> {} <sha256sum>".format(sys.argv[0]))
    exit()

target_hash = sys.argv[1]

password_bank = "rockyou.txt"