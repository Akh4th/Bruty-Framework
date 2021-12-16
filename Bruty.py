import time
from termcolor import colored as c

left = c("[", "red")
right = c("]", "red")
picks = ["1", "2", "3", "4", "*"]
mistakes = 0

print(c("STARTING BRUTY BY", "red"), c("Akh4th", "green"), c("!\n", "red"))
time.sleep(1.5)
for i in range(11):
    x = "*" * i
    time.sleep(0.5)
    print("[" + c("*" * i, "green") + c("*" * (10-i), "red") + "]" + c(f" {i*10}% loaded", "blue"))
time.sleep(0.5)
print(c("\nBRUTY LOADED SUCCESSFULLY !\n", "green"))
time.sleep(2)

print(c("What kind of file would you like to brute force :", "red"))
print(left + c("1","green") + right + " ZIP FILE\t\t\t" + left + c("2","green") + right + " PDF FILE")
print(left + c("3","green") + right + " DOCX FILE\t\t\t" + left + c("4","green") + right + " TEMPORARY UNAVAILABLE")
print(left + c("*", "green") + right + " CREATE WORDLIST")
pick = input()
while pick not in picks:
    pick = input(c("WRONG INPUT ! ", "red"))
    mistakes ++ 1
    if mistakes == 3:
        print(c("Too many wrong inputs.\n ABORTING !!!", "red"))
        quit()
try:
    if pick == "1":
        print(c("\nSTARTING BruteZip.py !", "red"))
        time.sleep(1.5)
        exec(open("BruteZip/BruteZip.py").read())
    elif pick == "2":
        print(c("\nSTARTING BrutePDF.py !", "red"))
        time.sleep(1.5)
        exec(open("BrutePDF/BrutePDF.py").read())
    elif pick == "3":
        print(c("\nSTARTING BruteDocx.py !", "red"))
        time.sleep(1.5)
        exec(open("BruteDocx/BruteDocx.py").read())
    elif pick == "4":
        # print(c(" ", "red"))
        # time.sleep(1.5)
        # exec(open("").read())
        print(c("I SAID TEMPORARY UNAVAILABLE RIGHT ?!", "red"))
        quit()
    else:
        print(c("\nSTARTING wordy.py !", "red"))
        time.sleep(1.5)
        exec(open("wordList/wordy.py").read())
except Exception as e:
    print(c(left + "!!!" + right + " ERROR PLEASE TRY AGAIN !", "red"))
    print(c("Exception : " + str(e), "blue"))
    mistakes ++ 1
    if mistakes == 3:
        print(c("Too many mistakes were made.\n ABORTING !!!", "red"))
        quit()