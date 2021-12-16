import datetime
import time
import zipfile as z
from termcolor import colored as c


# Files :
zip_file = input(c("LOCKED ZIP FILE : ", "green"))  # File you want to brute force !
wordlist = input(c("WORDLIST FILE : ", "green"))  # File to import passwords from !
# Global Definitions
target = z.ZipFile(zip_file)
now = datetime.datetime.now()
counts = len(list(open(wordlist, 'rb').readlines()))
# Prints
print(c("*" * 5, "blue"), c("READING " + wordlist, "yellow"), c("*" * 5, "blue"))
time.sleep(1)
print(c("TOTAL PASSWORDS AMOUNT :", 'red'), c(counts, 'green'))
time.sleep(2)
print(c("BRUTE FORCE STARTED :", 'red'), c(now.strftime("%d/%m/%Y at %H:%M:%S"), "green"))
time.sleep(2)


# The brute force function !
def brute(passwd, file):
    t0 = time.time()
    with open(passwd, 'rb') as lis:
        for line in lis.readlines():
            for word in line.split():
                try:
                    file.extractall(pwd=word)
                    print("\n" + c("*" * 10, 'green'), c("PASSWORD FOUND", 'red'), c("*" * 10, 'green'))
                    print(c("TOTAL TIME :", 'blue') , c(time.time()-t0, 'green'))
                    print(c("PASSOWRD :", 'blue'), c(word.decode(), 'green'))
                    return True
                except:
                    continue
    return False


# In case that the password does not exist in the wordlist file
# The function will eventually return False.
if brute(wordlist, target) is False:
    print(c("NO MATCHING PASSWORD TO ZIP FILE ", 'red'), c(zip_file, 'green'), c("FROM THE WORDLIST", 'red'),
          c(wordlist, 'green'))
    print(c("TOTAL TIME :", 'red'), c(time.time() - t0, 'green'))
    quit()
