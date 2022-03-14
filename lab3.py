'''
In this lab we will be cracking passwords. You will be given a list of password digests
(hashes.txt) and you must determine the corresponding plain text password for each hash in
this file. All of the hashes in this lab were hashed using SHA256. All passwords are salted with
the randomly generated salt found in salt.txt . In python, the salt is applied and the message is
hashed like this:
hashlib.sha256((salt + password).encode())
For a more complete example, look at the included code in hash.py. I used this exact code to
create hashes.txt from a password list. I also included an additional example that you can try
with this program (example_passwords.txt and example_hashes.txt)
In addition, you may NOT use any password cracking tool to do this lab.
You must write your own password cracker to use.
It can be done in whatever language you feel comfortable with (I suggest Python)
You should at least implement a brute-force and a dictionary attack.
Additional attack types may be necessary to find all passwords

salt.txt contains aB6nkeF0He3nmb4AOhbO5aEljbveRpLn 
'''
import hashlib
from string import hexdigits
import sys

#read in salt.txt
def salt_input():
    salt_file = open("salt.txt", "r", errors="replace")
    salt = salt_file.read()
    salt = salt.strip("\n").strip()
    salt_file.close()
    return salt

#read in hashes.txt
def hash_input():
    hash_file = open("hashes.txt", "r", errors="replace")
    hashes = hash_file.readlines()
    hash_file.close()
    return hashes

#read rockyou.txt
def word_input():
    word_file = open("rockyou.txt", "r", errors="replace")
    words = word_file.readlines()
    word_file.close()
    return words

#crack the sha256 hashes with salt and the word list
def crack_hashes(salt, words, hashes):
    cracked_hashes = {}
    for hash in hashes:
        hash = hash.strip("\n").strip()
        for word in words:
            word = word.strip("\n").strip()
            if hashlib.sha256((salt + word).encode()).hexdigest() == hash:
                cracked_hashes[hash.strip()] = word.strip()
    return cracked_hashes


#write cracked words to cracked_hashes.txt in the form of "hash":"word"
def write_cracked(cracked_hashes):
    cracked_file = open("cracked_hashes.txt", "w")
    for hash in cracked_hashes:
        cracked_file.write(hash + ":" + cracked_hashes[hash] + "\n")
    cracked_file.close()

#create a main function
def main():
    salt = salt_input()
    words = word_input()
    hashes = hash_input()
    cracked_hashes = crack_hashes(salt, words, hashes)
    write_cracked(cracked_hashes)

main()