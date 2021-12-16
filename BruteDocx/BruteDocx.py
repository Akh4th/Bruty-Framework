import msoffcrypto as ms
import io, time, datetime, os
from termcolor import colored as c

global t0

docx = input(c("LOCKED DOCX FILE : ", "red"))
wordlist = input(c("WORDLIST FILE : ", "red"))
# If wordlist doesnt exist aborts
if not os.path.isfile(wordlist):
    print(c("WORDLIST DOESNT EXIST !", "red"))
    print(c("ABORTING !!!", "yellow"))
    quit()
counts = len(list(open(wordlist, "r").readlines()))
dec = io.BytesIO()
now = datetime.datetime.now()

print(c("*" * 5, "blue"), c("READING " + wordlist, "yellow"), c("*" * 5, "blue"))
time.sleep(1)
print(c("TOTAL PASSWORDS AMOUNT :", 'red'), c(counts, 'green'))
time.sleep(2)
print(c("BRUTE FORCE STARTED :", 'red'), c(now.strftime("%d/%m/%Y at %H:%M:%S"), "green"))
time.sleep(2)


def brute(doc,passwords):
    t0 = time.time()
    with open(passwords, "r") as words:
        for word in words.readlines():
            for passwd in word.split():
                try:
                    with open(doc, "rb") as file:
                        filed = ms.OfficeFile(file)
                        filed.load_key(passwd)
                        filed.decrypt(dec)
                        print("\n" + c("*" * 10, 'green'), c("PASSWORD FOUND", 'red'), c("*" * 10, 'green'))
                        time.sleep(1)
                        print(c("TOTAL TIME :", 'blue'), c(time.time() - t0, 'green'))
                        time.sleep(1)
                        print(c("PASSWORD :", "red"), c(passwd, "green"))
                        return True
                except:
                    continue
    return False


if not brute(docx, wordlist):
    print(c("NO MATCHING PASSWORD TO DOCX FILE ", "red"), c(docx, "green"), c("FROM THE WORDLIST"), c(wordlist, "green"))
    print(c("TOTAL TIME :", 'red'), c(time.time() - t0, 'green'))
    quit()
