#!/bin/bash

for file in /usr/share/seclists/Passwords/*; do
    echo "Using $file as wordlist:"
    stegseek --wordlist $file mb.jpeg
done