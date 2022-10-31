#!/bin/python3

# ---------- Python SHA-256 Password Cracker
# Takes two arguments from the command line, the hash digest
# and a path to a wordlist for comparing hashes against it.
#FIXME: Works for SHA-256, 64 rounds - what is the built-in sha256sum consist of?

# ---------- Imported Modules
from hashlib import sha256
from pwn import *
import sys

# ---------- Input validation for command-line arguments
if len(sys.argv) != 3:
    print("Invalid argument.")
    print(">> {} <sha256sum> </path/to/wordlist.txt>".format(sys.argv[0]))
    exit()

# ---------- Initializations and declarations
target_hash = sys.argv[1]
password_bank = sys.argv[2]
attempts = 0

# ---------- Hash cracking process loop
with log.progress("Attempting to crack: {}\n".format(target_hash)) as p:
    with open(password_bank, "r", encoding='latin-1') as password_list:
        for password in password_list:
            
            # remove newlines from listed passwords to prevent digest contamination:
            password = password.strip("\n").encode('latin-1')
            password_hash = sha256sumhex(password)
            
            # prints attempt number, password and password hash digest
            p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))
            
            if password_hash == target_hash:
                p.success("Matching hash found after {} attempts! '{}' hashes to <{}>.".format(attempts, password.decode('latin-1'), password_hash))
                exit()
            attempts += 1
        p.failure("Password hash not found.")
