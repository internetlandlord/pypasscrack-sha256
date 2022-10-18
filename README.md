# pypasscrack-sha256
SHA256 Password Cracker

(This tool has been developed in part using material from TCM's Python for Hackers course.)

This tool takes a command-line argument of a SHA256 hash digest, and uses a wordlist
(in this case, rockyou.txt) to generate hashes and compare against the CLI input.

Progress is logged to the console while hash cracking is performed

### Future additions
* Convert over to dual-command line arguments (specify a hash and a path to a wordlist)
* Other hashing algos (SHA-512)
* Detection of hash types based off 'signature' (?)
