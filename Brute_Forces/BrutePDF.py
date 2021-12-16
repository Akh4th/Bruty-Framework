import time, pikepdf, os
from termcolor import colored as c
from datetime import datetime as d

# Loading files
wordlist = input(c("WORDLIST NAME : ", "green"))
pdf = input(c("LOCKED PDF FILE :", "green"))
# If wordlist doesnt exist aborts
if not os.path.isfile(wordlist):
    print(c("WORDLIST DOESNT EXIST !", "red"))
    print(c("ABORTING !!!", "yellow"))
    quit()


# Brute force function
def brute(password_file, locked_pdf):
    print(c("STARTED BRUTE FORCING :", "red"), c(locked_pdf, "green"), c(d.now().strftime("(%d/%m/%Y - %H:%M:%S)"), "blue"))
    time.sleep(1.5)
    with open(password_file, 'r') as file:
        passwords = file.readlines()
        tries = len(passwords)
    print(c("WORDLIST LOADED SUCCESSFULLY :", "red"), c(password_file,"green"))
    time.sleep(1.5)
    print(c("NUMBER OF TRIES AHEAD :", "red"), c(tries, "green"))
    for line in passwords:
        for passwd in line.split():
            try:
                with pikepdf.open(locked_pdf, password=passwd):
                    print(c("PASSWORD FOUND :", "red"), c(d.now().strftime("(%d/%m/%Y - %H:%M:%S)"), "blue"))
                    print(c("PASSWORD :", "red"), c(passwd, "green"))
                    return True
            except:
                continue
    return False


# Tries to unlock the PDF using the wordlist
# If there will be no correct password inside the file
# Script will quit.
if brute(wordlist,pdf) is False:
    print(c("NO MATCHING PASSWORD ON THE WORDLIST :", "red"), c(wordlist, "green"))
    time.sleep(1)
    print(c("PLEASE TRY ANOTHER WORDLIST !", "yellow"))
    quit()
