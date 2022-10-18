#!/bin/python3

# ---------- Python SHA-256 Password Cracker
# Takes two arguments from the command line, the hash digest
# and a path to a wordlist for comparing hashes against it.

# ---------- Imported Modules
from hashlib import sha256
from pwn import *
import sys

# Input validation for command-line arguments
if len(sys.argv) != 2: #FIXME: change this to reflect updated password_bank argument
    print("Invalid argument.")
    print(">> {} <sha256sum>".format(sys.argv[0]))
    exit()

# initializations and declarations
target_hash = sys.argv[1]
password_bank = "rockyou.txt" #FIXME: turn this into sys.argv[2]
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
