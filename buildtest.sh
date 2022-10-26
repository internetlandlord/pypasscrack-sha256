#!/bin/sh

# take input argument and sha256hash "as target password"
echo $1 | sha256sum > param

# run the program passing the varable as the first CLI arg
# hard-code the 2nd CLI arg to rockyou or something similar
