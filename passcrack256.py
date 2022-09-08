#!/bin/python3

from hashlib import sha256
from pwn import *
import sys

# input checker - very rudimentary validation
if len(sys.argv) != 2:
    print("Invalid argument.")
    print(">> {} <sha256sum>".format(sys.argv[0]))
    exit()

target_hash = sys.argv[1]

password_bank = "rockyou.txt"
attempts = 0

# loop for hash cracking
with log.progress("Attempting to crack: {}\n".format(target_hash)) as p:
    with open(password_bank, "r", encoding='latin-1') as password_list:
        for password in password_list:
            
            # remove newlines as they contaminate hash digest calculations
            password = password.strip("\n").encode('latin-1')
            password_hash = sha256sumhex(password)
            
            # prints attempt number, password and password hash digest
            p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))
            
            if password_hash == target_hash:
                p.success("Password hash found after {} attempts, '{}' hashes to <{}>.".format(attempts, password.decode('latin-1'), password_hash))
                exit()
            attempts += 1
        p.failure("Password hash not found.")
